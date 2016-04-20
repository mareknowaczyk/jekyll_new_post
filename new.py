#!/usr/bin/python
import yaml
import sys, getopt
import datetime
import re
import os
from optparse import OptionParser

TEMPLATE = """---
layout: post
title:  "%s"
date: %s +0200
category: %s
tags: [%s]
---
"""

JEKYLL_CONFIG_YAML = [ "_config.yml", "_config.yaml" ]
JEKYLL_CATEGORIES_OPTION = "category_list"
JEKYLL_CATEGORIES_FILE_OPTION = "categories_config_file"
DEFAULT_CATEGORIES_YAML = "_data/categories.yml"

def parse_options(show_help=False):
    parser = OptionParser(get_usage())
    parser.add_option("-f", "--force", action="store_true", dest="force", default=False)
    parser.add_option("-c", "--category-list", action="store_true", dest="category_list", default=False)
    if show_help:
        parser.print_help()
        return ()
    else:
        return parser.parse_args()

def get_jekyll_config():
    res = False
    for cfg in JEKYLL_CONFIG_YAML:
        res = res or os.path.isfile(cfg)
        if res:
            break
    if not res:
        return {}
    try:
        res = load_config(cfg)
    except:
        print("Cannot parse %s YAML config gile" % cfg )
    return res

def get_category_list(options, args):
    config = get_jekyll_config()
    if JEKYLL_CATEGORIES_OPTION in config:
        categories = config[JEKYLL_CATEGORIES_OPTION]
    else:
        if JEKYLL_CATEGORIES_FILE_OPTION in config:
            category_config_file = config[JEKYLL_CATEGORIES_FILE_OPTION]
        else:
            category_config_file = DEFAULT_CATEGORIES_YAML
        try:
            categories = load_config(category_config_file)
        except:
            print("cannot parse Yaml file %s" % yml_file)
            sys.exit(2)
    return categories

def parse_category(options, args):
    categories = get_category_list(options, args)
    category_names = [c['name'] for c in categories]
    category_name = args[0]
    if options.category_list or (not category_name in category_names):
        if not options.category_list:
            print("Unknow category '%s'." % category_name)
        print "\n  ".join( ["Available categories:"] + category_names )
        exit()
    try:
        category = [c for c in categories if c['name'] ==  category_name][0]
    except:
        print("There was problem with retrieving category for %s" % category_name)
        sys.exit(4)
    return category

def load_config(yaml_filename):
    with open(yaml_filename) as f:
        yml_content = f.read()
    return yaml.load(yml_content)

def get_usage():
    return """usage: %prog <category> <title> [<tag1> <tag2> .. <tagn>]
  - available categories can be defined in:
        * _config.yml as '"""+JEKYLL_CATEGORIES_OPTION+"""'
        * or category config file defined in _config.yml as '"""+JEKYLL_CATEGORIES_FILE_OPTION+"""'
        * or '_data/categories.yml'
        """
def new_post(category, title, tags, forced):
    now = datetime.date.today()
    file_date = datetime.date.today().strftime("%Y-%m-%d")
    full_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    file_title = re.sub(
        r"[^a-zA-Z0-9]",
        r"-",
        title.lower())
    filename = "%s-%s.md" % (file_date, file_title)
    full_filepath = category['dir']+'/'+filename
    show_overwrite_message = False
    if os.path.isfile(full_filepath):
        if (not forced):
            raise Exception("File '%s' exists and will be NOT overwritten." % full_filepath)
        else:
            show_overwrite_message = True
    with open(full_filepath, 'w') as f:
        f.write(TEMPLATE % (title, full_date, category['name'],", ".join(tags))
        )
    if show_overwrite_message:
        print "File '%s' was overwritten" % full_filepath

if __name__ == "__main__":
    options, args = parse_options()
    if len(args) < 2:
        print("not enough parameters")
        parse_options(True)
        sys.exit(1)
    category = parse_category(options, args)
    title = args[1]
    tags = args[2:]
    try:
        new_post(category, title, tags, options.force)
    except Exception as e:
        print e
