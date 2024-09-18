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
def about():
    return controller.generate(rank_engine.generate_markdown_list(config.blog_folder, 3))

@app.route('/about')
def home():
    return controller.access(config.home_page)

@app.route('/drive/', defaults={'subpath': ''})
@app.route('/drive/<path:subpath>')
def download(subpath):
    path = pfilter.concatenate("drive", subpath)
    if path == None:
        abort(403)
    if os.path.isdir(path):
        return controller.generate(rank_engine.generate_file_list(path, subpath))
    return send_file(path, as_attachment=True)
    

@app.route('/a/<string:article>')
def blog(article):
    path = pfilter.concatenate("blog", article)
    if path == None:
        abort(403)
    return controller.access(path + '.md')

@app.route('/s/<string:content>')
def download_resources(content):
    path = pfilter.concatenate("", "static")
    if path == None:
        abort(403)
    return send_from_directory(path, content, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
