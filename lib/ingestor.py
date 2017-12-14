import os
from constants import supported_filetypes
from parsers.base import *
from parsers.tex import *

class Ingestor:
    def __init__(self):
        pass

    def ingest(self, filepath):
        try:
            # file = open(filepath, 'r')
            file = "foo"
            name, ext = os.path.splitext(filepath)
            ext = ext[1:]
            if ext in supported_filetypes:
                self._invoke_parser(file, ext)

        except Exception:
            print("Unable to parse " + filepath)


    def _invoke_parser(self, file, ext):
        print("raa")
        bp = TexParser()
        print("ree")



ing = Ingestor()
ing.ingest("foo.tex")


    











