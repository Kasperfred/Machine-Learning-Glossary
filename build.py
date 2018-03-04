import yaml
from jinja2 import Template
import string
import htmlmin
import distutils.dir_util

def import_definitions(path='definitions.yml'):
    with open(path, "r") as f:
        content = f.read()
        definitions = yaml.load(content)
    return definitions

def sort_and_categorize_definitions(definitions):
    sorted_terms = sorted(definitions, key=lambda x: x)
    categorized_terms = {x:[] for x in string.ascii_uppercase}
    for x in sorted_terms: categorized_terms[x[0].upper()].append({**{"name":x},**definitions[x]})
    return categorized_terms

def get_sources(definitions):
    sources = []
    for i in definitions:
        try: 
            sources.append(definitions[i]['source'])
        except: 
            pass
    return sources

def render_template(categorized_definitions, sources=None, template="templates/default.html"):
    with open(template, 'r') as f:
        template = Template(f.read())
    
    html = template.render(content=categorized_definitions, sources=sources)
    minified_html = htmlmin.minify(html)
    return minified_html

def export_html(html, path="build/export.html"):
    distutils.dir_util.mkpath("/".join(path.split("/")[:-1]))
    with open(path, "w+") as f:
        f.write(html)
    return path

if __name__ == "__main__":
    definitions = import_definitions()
    categorized_definitions = sort_and_categorize_definitions(definitions)
    sources = get_sources(definitions)
    html = render_template(categorized_definitions, sources)
    export_html(html)
    

    