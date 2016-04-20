# Jekyll post generator

Simple python script that create posts in jekyll project.

## About

- Script  written in `python`.
- New posts are created with actual date & time in post category's directory.
- Posts in `jekyll` can be placed in different subdirectories. This script handles this situation by explicity defined posts categories.

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

Categories must be defined in one of these options:
* in jekylls *_config.yml*, as the **category_list** option,
* in `yml` file pointed in *_config.yml*, as the **categories_config_file** option,
* in *_data/categories.yml* *(default)*.

In order to selected category, post will be placed in directory assigned to it.

## Examples
* **Categories configuration**:
  * *_config.yml*
  ```
  ...
  category_list:
    - name : post
      dir : _posts/
  ...
  ```
  * *_config.yml* with defined separated categories file:
    * *_config.yml*
    ```
    ...
    categories_config_file: _categories.yml
    ...
    ```
    * *_categories.yml*
    ```
      - name : post
        dir : _posts/
    ```
  * *default configuration* - if none of above is specified, script assume that categories are defined in *_data/categories.yml*. Example content
  ```
   - name : post
     dir : _posts/
  ```
* **New post**:
  In default configuration, command for new post, launched at 2016-04-01 12:34:

  ```python new.py post "This is new post" new-tag```

  will produce new post *2016-04-01-this-is-new-post.md* in *_posts* directory with following content:

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
