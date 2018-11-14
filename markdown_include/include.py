from __future__ import print_function

import re
import json
import os.path

import json_include
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class MarkdownInclude(Extension):
    def __init__(self, configs={}):
        self.config = {
            'base_path': ['.', 'Default location from which to evaluate relative paths for the include statement.'],
            'include_syntax': ['\{!\s*(.+?)\s*!\}', 'regex to find the include statement.'],
        }
        for key, value in configs.items(): self.setConfig(key, value)

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('include', IncludePreprocessor(md, self.getConfigs()), '_begin')


class IncludePreprocessor(Preprocessor):
    """
    """

    def __init__(self, md, config):
        super(IncludePreprocessor, self).__init__(md)
        self.base_path = config['base_path']
        self.include_syntax = re.compile(config['include_syntax'])

    def run(self, lines):
        done = False
        while not done:
            for line in lines:
                loc = lines.index(line)
                m = self.include_syntax.search(line)

                if m:
                    try:
                        path_ = self.get_absolute_path(m.group(1))
                        text = json.dumps(self.get_json(path_), indent=4).split("\n")
                    except Exception as e:
                        print(e)
                        lines[loc] = self.include_syntax.sub('', line)
                        break

                    line_split = self.include_syntax.split(line)
                    if len(text) == 0:
                        text.append('')
                    for i in range(len(text)):
                        text[i] = text[i].rstrip('\r\n')
                    text[0] = line_split[0] + text[0]
                    text[-1] = text[-1] + line_split[2]
                    lines = lines[:loc] + text + lines[loc + 1:]
                    break
            else:
                done = True
        return lines

    def get_absolute_path(self, path_):
        """
        Returns the absolute path to the json file.

        Args:
            path_ (str): absolute or relative path to the json file to include.

        Returns:
            str
        """
        path_ = os.path.expanduser(path_)
        if not os.path.isabs(path_):
            path_ = os.path.normpath(os.path.join(self.base_path, path_))
        return path_

    def get_json(self, path):
        """
        Returns a json with inclusion references resolved.

        Args:
            path (str): path to the json file.

        Returns:
             dict
        """
        dirName = os.path.dirname(path)
        baseName = os.path.basename(path)
        return json.loads(json_include.build_json(dirName, baseName))


def makeExtension(*args, **kwargs):
    return MarkdownInclude(kwargs)
