from flask import Flask, render_template, send_file, send_from_directory, abort
import os
import config
import engine
import pfilter

md_engine = engine.md_engine(config.template_html)
controller = engine.controller(md_engine)
rank_engine = engine.rank_engine()

app = Flask(__name__)

@app.route('/')
def home():
    html = controller.access(config.home_page)
    files = rank_engine.ranking(config.blog_folder)
    html = controller.generate_list(files, files[0] if len(files) else "", html)
    return html

@app.route('/about')
def about():
    return controller.access(config.about_page)

@app.route('/list')
def list():
    html = controller.generate(rank_engine.generate_markdown_list(config.blog_folder))
    return html

@app.route('/drive/', defaults={'subpath': ''})
@app.route('/drive/<path:subpath>')
def download(subpath):
    path = pfilter.concatenate("drive", subpath)
    if path == None:
        abort(403)
    try:
        if os.path.isdir(path):
            return controller.generate(rank_engine.generate_file_list(path, subpath))
        return send_file(path, as_attachment=True)
    except FileNotFoundError:
        abort(404)
    

@app.route('/a/<string:article>')
def blog(article):
    path = pfilter.concatenate("blog", article)
    if path == None:
        abort(403)
    try:
        html = controller.access(path + '.md')
        files = rank_engine.ranking(config.blog_folder)
        html = controller.generate_list(files, article + '.md', html)
        return html
    except FileNotFoundError:
        abort(404)

@app.route('/s/<string:content>')
def download_resources(content):
    path = pfilter.concatenate("", "static")
    if path == None:
        abort(403)
    try:
        return send_from_directory(path, content, as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
