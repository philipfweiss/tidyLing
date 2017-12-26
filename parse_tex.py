#/usr/bin/env python3

import argparse
import re

from parsers import gb4e_parse, examples_parse


def main():
  parser = argparse.ArgumentParser(description='Extract linguistic examples from TeX-files')
  parser.add_argument('file_path', metavar='TEX_FILE', help='path to TeX file')
                      
  args = parser.parse_args()
  
  f = open(args.file_path, 'r')
  file_content = f.read()

  file_content = cleanup_tex(file_content)

  example_blocks = extract_example_blocks(file_content)

  for eb in example_blocks:    
    examples = extract_examples(eb)
    for e in examples.keys():
      print("{}: {}".format(e, examples[e]))
      



BEGIN_PATTERN=re.compile('(\\\\begin\\s*[{]([a-zA-Z0-9]+)[}])')
END_PATTERN=re.compile('(\\\\end\\s*[{]([a-zA-Z0-9]+)[}])')



def cleanup_tex(file_content):
  
  file_content = BEGIN_PATTERN.sub("\\\\begin{\g<2>}", file_content)
  file_content = END_PATTERN.sub("\\\\end{\g<2>}", file_content)
  return file_content


'''
    Extracts all \begin{exe} ... \end{exe} blocks
    using the grammar defined in parsers/examples.peg.
'''
def extract_example_blocks(file_content):
  parsed = examples_parse(file_content)  
  examples = []
  
  for ex in parsed.elements[0].elements:
    examples.append(ex.exampleBody.text)
  
  return examples
    

def extract_examples(exe_block):
  parsed = gb4e_parse(exe_block)
  
  
  examples = {}
  for i, ex in enumerate(parsed.body):
    num = str(i+1)
    examples[num] = ex.string.text
    
    #check for xlist
    if ex.elements[4].text != "":
      for j, subex in enumerate(ex.elements[4].elements[1].elements):
        num2 = "{}.{}".format(num, str(j+1))
        examples[num2] = subex.string.text
  
  return examples


if __name__ == '__main__':
  main()  