import os
from .parsers.base import *
from .parsers.tex import *

class Ingestor:
    def __init__(self):
        self.parsermap = {
            ".tex": TexParser,
        }

    def ingest(self, filepath):
        file = open(filepath, 'r')
        name, ext = os.path.splitext(filepath)

        if ext in self.parsermap:
            return self._invoke_parser(file, ext)

        return []


    def _invoke_parser(self, file, ext):
        parser = self.parsermap[ext]()
        return parser.parse(file)




    











