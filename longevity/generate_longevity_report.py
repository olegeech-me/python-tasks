#!/usr/bin/env python

import os
import yaml
from jinja2 import Environment, FileSystemLoader

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = Environment(loader = FileSystemLoader(templates_dir))
template = env.get_template('index.rst.j2')
data = yaml.load(open('data_template.yaml'))
print "data to put: ", data

# write template
filename = os.path.join(root, 'rendered', 'index.rst')
with open(filename, 'w') as fh:
    fh.write(template.render(data))

# print results
with open(filename,'r') as fh:
    print "resulted document:\n", fh.read()


