# Markdown JSON Include

This is an extension to [Python-Markdown](https://pythonhosted.org/Markdown/) to include JSON content.

[json_include](https://github.com/Exabyte-io/json_include) is used underneath to resolve files inclusion.


## Installation

```bash
git clone git@github.com:Exabyte-io/markdown-include.git
cd markdown-include
pip install -e .
```

## Configuration

- **include_syntax**: regex to find the include statement. Defaults to `\{!\s*(.+?)\s*!\}`.
- **base_path**: Default location from which to evaluate relative paths for the include statement.

## Usage

Add `{!PATH_TO_JSON_FILE!}` into your markdown. `PATH_TO_JSON_FILE` is relative to `base_path` config parameter. The statement will be replaced by resolved version of the JSON file. 

This module can be used in a program in the following ways:

```python
import markdown
html = markdown.markdown(source, extensions=['markdown_include.include'])
```

```python
import markdown
from markdown_include.include import MarkdownInclude

markdown_include = MarkdownInclude(configs={'base_path':'/srv/content/', 'include_syntax': '\{!\s*(.+?)\s*!\}'})
html = markdown.markdown(source, extensions=[markdown_include])
```
