# Jekyll post generator

Simple python script that create posts in jekyll project.

## About

Script  written in `python`.

New posts are created with actual date & time in post category's directory.

## Usage

Launch following command in terminal:

```
python new.py category title [tag_1 tag_2 .. tag_n]
Usage: new.py <category> <title> [<tag1> <tag2> .. <tagn>]
  - available categories options defined in '_data/categories.yml'

Options:
  -h, --help   show this help message and exit
  -f, --force
```

Categories are defined in `_data/categories.yml`.
In order to selected category, post will be placed in directory assigned to category.

## Example

Content of `categories.yml` for standard `jekyll` project *(all posts in _posts directory)* is as follow:

```
- name : post
  dir : _posts/
```

Command for new post, launched at 2016-04-01 12:34:

<pre>python new.py post "This is new post" new</pre>

will produce new post `2016-04-01-this-is-new-post.md` in `_posts` directory with following content:

```
---
layout: post
title:  "This is new post"
date: 2016-04-01 12:34:00 +0200
category: post
tags: [new]
---
```

## Requirements

* python 2.7+
* python yaml library ( [PyYAML](http://pyyaml.org/wiki/PyYAML) 3.11+ )
