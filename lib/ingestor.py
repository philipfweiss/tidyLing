import os
from constants import supported_filetypes

class Ingestor:
    def __init__(self):
        pass

    def ingest(self, filepath):
        try:
            file = open(filepath, 'r')
            name, ext = os.path.splitext(filepath)
            ext = ext[1:]
            if ext in supported_filetypes:
                self.invoke_parser(file, ext)

        except Exception:
            print("Unable to parse " + filepath)


    def invoke_parser(self, file, ext):
        print("parser invoked!")


ing = Ingestor()
ing.ingest("foo.tex")


    











