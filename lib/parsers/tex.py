from .base import BaseParser
from TexSoup import TexSoup
class TexParser(BaseParser):
    def parse(self, file):
        soup = TexSoup(file)
        soup.count('begin {exe}')
        # examples = list(soup.find_all('ex'))
        # for example in examples:
        #     print(example.contents)
        #

