#!/usr/bin/python
import yaml
import sys, getopt
import datetime
import re

TEMPLATE = """---
layout: post
title:  "%s"
date: %s +0200
category: %s
tags: [%s]
---
"""

def load_config(yaml_filename):
    with open(yaml_filename) as f:
        yml_content = f.read()
    return yaml.load(yml_content)

def show_usage():
    print("""
    new.py <category> <title> [<tag1> <tag2> .. <tagn>]
        - available categories options defined in '_data/categories.yml'
    """
    )

def new_post(category, title, tags):
    now = datetime.date.today()
    file_date = datetime.date.today().strftime("%Y-%m-%d")
    full_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    file_title = re.sub(
        r"[^a-zA-Z0-9]",
        r"-",
        title.lower())
    filename = "%s-%s.md" % (file_date, file_title)
    with open(category['dir']+'/'+filename, 'w') as f:
        f.write(TEMPLATE % (title, full_date, category['name'],", ".join(tags))
        )

if __name__ == "__main__":
    yml_file = "_data/categories.yml"
    try:
        categories = load_config(yml_file)
    except:
        print("cannot parse Yaml file %s" % yml_file)
        sys.exit(2)
    category_names = [c['name'] for c in categories]
    try:
        category_name = sys.argv[1]
        title = sys.argv[2]
    except:
        print("not enough parameters")
        show_usage()
        sys.exit(1)
    if not category_name in category_names:
        print("Unknow category %s." % category_name)
        print("Available options (defined in _data/categories.yml) are: ")
        print("\n".join(category_names))
        sys.exit(3)
    try:
        category = [c for c in categories if c['name'] ==  category_name][0]
    except:
        print("There was problem with retrieving category for %s" % category_name)
        sys.exit(4)
    tags = sys.argv[3:]
    new_post(category, title, tags)
