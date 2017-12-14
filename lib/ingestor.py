import os

class Ingestor:
    def __init__(self):
        pass

    def ingest(self, filepath):
        try:
            file = open(filepath, 'r')
        except Exception:
            print("Unable to parse " + filepath)

        name, ext = os.path.splitext(filepath)
        ext = ext[1:]


    def invoke_parser(self):
        pass


ing = Ingestor()
ing.ingest("foo.txt")


    











