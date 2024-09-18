from flask import Flask, render_template, send_from_directory
import config
import engine
import pfilter

md_engine = engine.md_engine(config.template_html)
controller = engine.controller(md_engine)
rank_engine = engine.rank_engine(config.blog_folder)

app = Flask(__name__)

@app.route('/')
def about():
    return controller.generate(rank_engine.generate_markdown_list(3))

@app.route('/about')
def home():
    return controller.access(config.home_page)


@app.route('/a/<string:article>')
def dynamic_route(article):
    path = pfilter.concatenate("blog", article)
    return controller.access(path + '.md')

@app.route('/s/<string:content>')
def download_resources(content):
    path = pfilter.concatenate("", "static")
    return send_from_directory(path, content, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
