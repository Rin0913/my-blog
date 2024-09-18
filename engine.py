import commonmark
import os

class controller():
    def __init__(self, md_engine):
        self.md_engine = md_engine

    def generate(self, markdown_text):
        intermediate_output = self.md_engine.markdown_to_html(markdown_text)
        return self.md_engine.generate_html(intermediate_output)
        
    def access(self, markdown_path):
        md_text = ""
        with open(markdown_path, 'r') as f:
            md_text = f.read()
        return self.generate(md_text)

class md_engine():
    def __init__(self, template_html):
        self.template_html = template_html

    def markdown_to_html(self, markdown_text):
        parser = commonmark.Parser()
        renderer = commonmark.HtmlRenderer()
        ast = parser.parse(markdown_text)
        output = renderer.render(ast)
        return output

    def generate_html(self, intermediate_output):
        html_text = ""
        with open(self.template_html, 'r') as f:
            html_text = f.read()
        return html_text.replace("<flask-render>", intermediate_output)

class rank_engine():
    def __init__(self, folder):
        self.folder = folder

    def ranking(self):
        all_files = [f for f in os.listdir(self.folder) if os.path.isfile(os.path.join(self.folder, f))]

        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(self.folder, x)), reverse=True)
        return all_files

    def generate_markdown_list(self, no=-1):
        files = self.ranking()
        text = []
        remove_extension = lambda filename: os.path.splitext(filename)[0]
        for f in files:
            if no == 0:
                break
            f = remove_extension(f)
            text.append(f"[{f}](/a/{f})")
            no -= 1
        return "<hr/>".join(text)
