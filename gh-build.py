import os
import codecs

from glob import glob
from markdown import markdown

from jinja2 import Environment, FileSystemLoader

TEMPLATES_DIRECTORY = 'templates'
ROOT_TEMPLATE_NAME = 'layout.html'
PAGE_TEMPLATE_NAME = 'page.html'


def build_pages(base_directory):
    root_files = glob('%s/*.markdown' % base_directory)
    
    template_env = Environment(loader=FileSystemLoader("%s/%s" % (base_directory, TEMPLATES_DIRECTORY)))
    
    for filename in root_files:
        build_page(filename, template_env.get_template(ROOT_TEMPLATE_NAME))
        
    pages_files = glob('%s/pages/*.markdown' % base_directory)
    
    for filename in pages_files:
        build_page(filename, template_env.get_template(PAGE_TEMPLATE_NAME))
        
    
def build_page(filename, template):
    name, ext = os.path.splitext(filename)
    with codecs.open(filename, encoding='utf-8', mode='r') as f:
        markdown_text = f.read()
        
    html = markdown(markdown_text, ['extra'], output_format='html5')
    with codecs.open("%s.html" % name, encoding='utf-8', mode='w') as f:
        f.write(template.render(content = html))
            


if __name__ == '__main__':
    build_pages(os.getcwd())