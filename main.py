from flask import Flask, render_template, send_file, send_from_directory, abort, request
import os
import mimetypes
import config
import engine
import pfilter
import json

md_engine = engine.md_engine(config.template_html, config.title_mapping)
controller = engine.controller(md_engine)
rank_engine = engine.rank_engine()

app = Flask(__name__)

@app.route('/')
def home():
    html = controller.access(config.home_page)
    files = rank_engine.ranking(config.blog_folder)
    html = controller.generate_list(files, "", html, 10)
    return html

@app.route('/about')
def about():
    return controller.access(config.about_page)

@app.route('/index')
def index():
    return controller.access(config.index_page)

@app.route('/list')
def list():
    html = controller.generate(rank_engine.generate_markdown_list(config.blog_folder))
    return html

@app.route('/sitemap.xml')
def sitemap():
    sitemap = ['/', '/index', '/about', '/list']
    for f in rank_engine.ranking(config.blog_folder):
        sitemap.append("/a/" + os.path.splitext(f)[0])
    result = '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    for i in sitemap:
        result += f'<url><loc>{config.base_url + i}</loc><changefreq>weekly</changefreq></url>'
    result += "</urlset>"
    return result

@app.route('/robots.txt')
def robots():
    try:
        with open(config.robots_txt) as f:
            return f.read()
    except FileNotFoundError:
        abort(404)
    
@app.route('/drive/', defaults={'subpath': ''})
@app.route('/drive/<path:subpath>')
def download(subpath):
    path = pfilter.concatenate(config.drive_folder, subpath)
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
    path = pfilter.concatenate(config.blog_folder, article)
    if path == None:
        abort(403)
    try:
        html = controller.access(path + '.md')
        files = rank_engine.ranking(config.blog_folder)
        html = controller.generate_list(files, article + '.md', html)
        return html
    except FileNotFoundError:
        abort(404)

@app.route('/b/<path:article>')
def browser(article):

    def is_text_file(file_path):
        mime_type, _ = mimetypes.guess_type(file_path)
        if mime_type and mime_type.startswith('text'):
            return True
        return False

    path = pfilter.concatenate(config.share_folder, article)

    if path == None:
        abort(403)
    try:
        if is_text_file(path):
            html = controller.access(path)
            html = controller.generate_list([], "", html)
            return html
        return send_file(path, as_attachment=False)
    except FileNotFoundError:
        abort(404)

@app.route('/s/<path:path>')
def download_resources(path):
    path = pfilter.concatenate("static/", path)
    if path == None:
        abort(403)
    try:
        return send_file(path, as_attachment=False)
    except FileNotFoundError:
        abort(404)

@app.after_request
def add_url(response):
    if 499 >= response.status_code >= 400:
        html = controller.access(config.error404_page)
        files = rank_engine.ranking(config.blog_folder)
        html = controller.generate_list(files, "", html, 10)
        response.set_data(html)

    if 'text/html' in response.content_type:
        url = request.url_root.rstrip('/') + request.path
        html = response.get_data(as_text=True)
        html = html.replace("<flask-meta>", f'<link rel="canonical" href="{url}" />')
        response.set_data(html)
    return response

if __name__ == '__main__':
    app.run(debug=True)
