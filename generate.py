#!/usr/bin/python

import pathlib
from jinja2 import Environment, PackageLoader
import models
import os
import shutil
env = Environment(loader=PackageLoader('models', 'templates'))

STATIC_DIR = './static/'
OUTPUT_DIR = './_output/'

static_dir_path = pathlib.Path(STATIC_DIR)
output_dir_path = pathlib.Path(OUTPUT_DIR)

shutil.copytree(static_dir_path, output_dir_path)

template = env.get_template('blog-entry.html')
resume = env.get_template('resume.html')
portfolio = env.get_template('portfolio.html')
about = env.get_template('about.html')
labs = env.get_template('labs.html')

with open(os.path.join(OUTPUT_DIR, 'resume.html'), 'w') as html:
    html.write(resume.render())
    
with open(os.path.join(OUTPUT_DIR, 'portfolio.html'), 'w') as html:
    html.write(portfolio.render())
    
with open(os.path.join(OUTPUT_DIR, 'about.html'), 'w') as html:
    html.write(about.render())
    
with open(os.path.join(OUTPUT_DIR, 'lab.html'), 'w') as html:
    html.write(labs.render())

articles = []
for n in models.posts:
    condition = False

    articles.append({
        'title'   : n["data"].title,
        'url'     : n["data"].url,
        'current' : condition
    })
    
for post in models.posts:
    g = post["data"].spit_dict()
    a = list(articles)
    
    for x in a:
        i = a.index(x)
    
        if x["url"] == g["url"]:
            a[i]["current"] = True

        else:
            a[i]["current"] = False
    
    g["posts"] = a
                
    with open(os.path.join(OUTPUT_DIR, g["url"]), 'w') as html:
        html.write(template.render(g))
        
    if models.posts[len(models.posts)-1] == post:
        with open(os.path.join(OUTPUT_DIR, 'index.html'), 'w') as html:
                html.write(template.render(g))
