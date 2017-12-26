from collections import defaultdict
import re


class TreeNode(object):
    def __init__(self, text, offset, elements=None):
        self.text = text
        self.offset = offset
        self.elements = elements or []

    def __iter__(self):
        for el in self.elements:
            yield el


class TreeNode1(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode1, self).__init__(text, offset, elements)
        self.exampleBody = elements[1]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    def _read_document(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['document'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            address2 = self._read_example()
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address3 = FAILURE
            remaining1, index3, elements2, address4 = 0, self._offset, [], True
            while address4 is not FAILURE:
                index4, elements3 = self._offset, []
                address5 = FAILURE
                index5 = self._offset
                chunk0 = None
                if self._offset < self._input_size:
                    chunk0 = self._input[self._offset:self._offset + 11]
                if chunk0 == '\\begin{exe}':
                    address5 = TreeNode(self._input[self._offset:self._offset + 11], self._offset)
                    self._offset = self._offset + 11
                else:
                    address5 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"\\\\begin{exe}"')
                self._offset = index5
                if address5 is FAILURE:
                    address5 = TreeNode(self._input[self._offset:self._offset], self._offset)
                    self._offset = self._offset
                else:
                    address5 = FAILURE
                if address5 is not FAILURE:
                    elements3.append(address5)
                    address6 = FAILURE
                    if self._offset < self._input_size:
                        address6 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address6 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('<any char>')
                    if address6 is not FAILURE:
                        elements3.append(address6)
                    else:
                        elements3 = None
                        self._offset = index4
                else:
                    elements3 = None
                    self._offset = index4
                if elements3 is None:
                    address4 = FAILURE
                else:
                    address4 = TreeNode(self._input[index4:self._offset], index4, elements3)
                    self._offset = self._offset
                if address4 is not FAILURE:
                    elements2.append(address4)
                    remaining1 -= 1
            if remaining1 <= 0:
                address3 = TreeNode(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            else:
                address3 = FAILURE
            if address3 is not FAILURE:
                elements0.append(address3)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['document'][index0] = (address0, self._offset)
        return address0

    def _read_example(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['example'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        remaining0, index2, elements1, address2 = 0, self._offset, [], True
        while address2 is not FAILURE:
            index3, elements2 = self._offset, []
            address3 = FAILURE
            index4 = self._offset
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 11]
            if chunk0 == '\\begin{exe}':
                address3 = TreeNode(self._input[self._offset:self._offset + 11], self._offset)
                self._offset = self._offset + 11
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"\\\\begin{exe}"')
            self._offset = index4
            if address3 is FAILURE:
                address3 = TreeNode(self._input[self._offset:self._offset], self._offset)
                self._offset = self._offset
            else:
                address3 = FAILURE
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                if self._offset < self._input_size:
                    address4 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('<any char>')
                if address4 is not FAILURE:
                    elements2.append(address4)
                else:
                    elements2 = None
                    self._offset = index3
            else:
                elements2 = None
                self._offset = index3
            if elements2 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode(self._input[index3:self._offset], index3, elements2)
                self._offset = self._offset
            if address2 is not FAILURE:
                elements1.append(address2)
                remaining0 -= 1
        if remaining0 <= 0:
            address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
            self._offset = self._offset
        else:
            address1 = FAILURE
        if address1 is not FAILURE:
            elements0.append(address1)
            address5 = FAILURE
            address5 = self._read_exampleBody()
            if address5 is not FAILURE:
                elements0.append(address5)
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode1(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['example'][index0] = (address0, self._offset)
        return address0

    def _read_exampleBody(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['exampleBody'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 11]
        if chunk0 == '\\begin{exe}':
            address1 = TreeNode(self._input[self._offset:self._offset + 11], self._offset)
            self._offset = self._offset + 11
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\\\\begin{exe}"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 0, self._offset, [], True
            while address3 is not FAILURE:
                index3, elements2 = self._offset, []
                address4 = FAILURE
                index4 = self._offset
                chunk1 = None
                if self._offset < self._input_size:
                    chunk1 = self._input[self._offset:self._offset + 9]
                if chunk1 == '\\end{exe}':
                    address4 = TreeNode(self._input[self._offset:self._offset + 9], self._offset)
                    self._offset = self._offset + 9
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"\\\\end{exe}"')
                self._offset = index4
                if address4 is FAILURE:
                    address4 = TreeNode(self._input[self._offset:self._offset], self._offset)
                    self._offset = self._offset
                else:
                    address4 = FAILURE
                if address4 is not FAILURE:
                    elements2.append(address4)
                    address5 = FAILURE
                    if self._offset < self._input_size:
                        address5 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                        self._offset = self._offset + 1
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('<any char>')
                    if address5 is not FAILURE:
                        elements2.append(address5)
                    else:
                        elements2 = None
                        self._offset = index3
                else:
                    elements2 = None
                    self._offset = index3
                if elements2 is None:
                    address3 = FAILURE
                else:
                    address3 = TreeNode(self._input[index3:self._offset], index3, elements2)
                    self._offset = self._offset
                if address3 is not FAILURE:
                    elements1.append(address3)
                    remaining0 -= 1
            if remaining0 <= 0:
                address2 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements0.append(address2)
                address6 = FAILURE
                chunk2 = None
                if self._offset < self._input_size:
                    chunk2 = self._input[self._offset:self._offset + 9]
                if chunk2 == '\\end{exe}':
                    address6 = TreeNode(self._input[self._offset:self._offset + 9], self._offset)
                    self._offset = self._offset + 9
                else:
                    address6 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"\\\\end{exe}"')
                if address6 is not FAILURE:
                    elements0.append(address6)
                else:
                    elements0 = None
                    self._offset = index1
            else:
                elements0 = None
                self._offset = index1
        else:
            elements0 = None
            self._offset = index1
        if elements0 is None:
            address0 = FAILURE
        else:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['exampleBody'][index0] = (address0, self._offset)
        return address0


class Parser(Grammar):
    def __init__(self, input, actions, types):
        self._input = input
        self._input_size = len(input)
        self._actions = actions
        self._types = types
        self._offset = 0
        self._cache = defaultdict(dict)
        self._failure = 0
        self._expected = []

    def parse(self):
        tree = self._read_document()
        if tree is not FAILURE and self._offset == self._input_size:
            return tree
        if not self._expected:
            self._failure = self._offset
            self._expected.append('<EOF>')
        raise ParseError(format_error(self._input, self._failure, self._expected))


def format_error(input, offset, expected):
    lines, line_no, position = input.split('\n'), 0, 0
    while position <= offset:
        position += len(lines[line_no]) + 1
        line_no += 1
    message, line = 'Line ' + str(line_no) + ': expected ' + ', '.join(expected) + '\n', lines[line_no - 1]
    message += line + '\n'
    position -= len(line) + 1
    message += ' ' * (offset - position)
    return message + '^'

def parse(input, actions=None, types=None):
    parser = Parser(input, actions, types)
    return parser.parse()
