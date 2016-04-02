# Jekyll post generator

Simple python script that create posts in jekyll project.

## About

Script  written in `python`.

New posts are created with actual date & time in post category's directory.

## Usage

Launch following command in terminal:

<pre>
python new.py category title [tag_1 tag_2 .. tag_n]
</pre>

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

##

### TODO
- define `categories.yml` alternative name and directory in `config.yml`
- read default _data folder from `config.yml`
- read default _posts folder from `config.yml`
- prevent posts overwriting (if new post has the same date and title, it overwrites existing post without asking)
- define post template in `config.yml'
- define timezone in `config.yml`
