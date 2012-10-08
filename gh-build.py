import os
import codecs

from glob import glob
from markdown import markdown

from jinja2 import Environment, FileSystemLoader, PackageLoader, TemplateNotFound

TEMPLATES_DIRECTORY = 'templates'
ROOT_TEMPLATE_NAME = 'root.html'
PAGE_TEMPLATE_NAME = 'page.html'


def build_pages(base_directory):
    print "Building pages in %s" % base_directory
    root_files = glob(os.path.join(base_directory, '*.markdown'))
    pages_built = 0
    if os.path.isdir(os.path.join(base_directory, TEMPLATES_DIRECTORY)):
        print "Found local template directory"
        template_env = Environment(loader=FileSystemLoader(os.path.join(base_directory, TEMPLATES_DIRECTORY)))
    else:
        print "No Template directory found, using default"
        template_env = Environment(loader=PackageLoader('gh-build', 'templates'))
    
    for filename in root_files:
        try:
            template = template_env.get_template(ROOT_TEMPLATE_NAME)
        except TemplateNotFound:
            print "root.html template missing in local directory, falling back to default"
            template_env = Environment(loader=PackageLoader('gh-build', 'templates'))
            template = template_env.get_template(ROOT_TEMPLATE_NAME)
        
        build_page(filename, base_directory, template)
        pages_built += 1
        
    pages_files = glob(os.path.join(base_directory, 'pages', '*.markdown'))
    
    for filename in pages_files:
        build_page(filename, base_directory, template_env.select_template([PAGE_TEMPLATE_NAME, ROOT_TEMPLATE_NAME]))
        pages_built += 1
        
    print "%s pages built" % pages_built
        
    
def build_page(filename, base_directory, template):
    name, ext = os.path.splitext(filename)
    with codecs.open(filename, encoding='utf-8', mode='r') as f:
        markdown_text = f.read()
        
    html = markdown(markdown_text, ['extra'], output_format='html5')
    with codecs.open("%s.html" % name, encoding='utf-8', mode='w') as f:
        f.write(template.render(content = html))
        
    print "Built page: %s.html" % os.path.relpath(name, base_directory)
            


if __name__ == '__main__':
    build_pages(os.getcwd())