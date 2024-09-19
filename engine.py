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

    def generate_list(self, all_files, title, origin_html):
        lst = []

        if title in all_files:
            idx = all_files.index(title)
            f = lambda x: os.path.splitext(x)[0]
            for i in range(-2, 4):
                if 0 <= idx + i < len(all_files): lst.append(f(all_files[idx + i]))
        html_text = []

        for f in lst:
            html_text.append(f"- [{f}](/a/{f})")
        html_text = self.md_engine.markdown_to_html("\n".join(html_text))
        if html_text: html_text = "<hr/>" + html_text
        return origin_html.replace("<flask-list>", html_text)

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
    def ranking(self, folder):
        all_files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and os.path.splitext(f)[1] == '.md']

        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
        return all_files

    def file_ranking(self, folder):
        all_files = [f for f in os.listdir(folder)]

        all_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)), reverse=True)
        return all_files

    def generate_markdown_list(self, path, no=-1):
        files = self.ranking(path)
        text = []
        for f in files:
            if no == 0:
                break
            if os.path.splitext(f)[1] != '.md':
                continue
            f = os.path.splitext(f)[0]
            text.append(f"- [{f}](/a/{f})")
            no -= 1
        return "\n".join(text)

    def generate_file_list(self, path, fake_path):
        files = self.file_ranking(path)
        text = ["- [.]({fake_path}/..)"]
        for f in files:
            f = os.path.splitext(f)[0]
            text.append(f"- [{f}](/drive/{fake_path}/{f})")
        return "\n".join(text)

