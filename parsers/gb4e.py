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
        self.body = elements[2]


class TreeNode2(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode2, self).__init__(text, offset, elements)
        self.string = elements[3]


class TreeNode3(TreeNode):
    def __init__(self, text, offset, elements):
        super(TreeNode3, self).__init__(text, offset, elements)
        self.whitespace = elements[1]


class ParseError(SyntaxError):
    pass


FAILURE = object()


class Grammar(object):
    def _read_container(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['container'].get(index0)
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
                address3 = self._read_whitespace()
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
                address4 = FAILURE
                address4 = self._read_body()
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address5 = FAILURE
                    chunk1 = None
                    if self._offset < self._input_size:
                        chunk1 = self._input[self._offset:self._offset + 9]
                    if chunk1 == '\\end{exe}':
                        address5 = TreeNode(self._input[self._offset:self._offset + 9], self._offset)
                        self._offset = self._offset + 9
                    else:
                        address5 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('"\\\\end{exe}"')
                    if address5 is not FAILURE:
                        elements0.append(address5)
                    else:
                        elements0 = None
                        self._offset = index1
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
            address0 = TreeNode1(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['container'][index0] = (address0, self._offset)
        return address0

    def _read_body(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['body'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 1, self._offset, [], True
        while address1 is not FAILURE:
            address1 = self._read_example()
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['body'][index0] = (address0, self._offset)
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
            address2 = self._read_whitespace()
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
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 3]
            if chunk0 == '\\ex':
                address3 = TreeNode(self._input[self._offset:self._offset + 3], self._offset)
                self._offset = self._offset + 3
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"\\\\ex"')
            if address3 is not FAILURE:
                elements0.append(address3)
                address4 = FAILURE
                remaining1, index3, elements2, address5 = 1, self._offset, [], True
                while address5 is not FAILURE:
                    address5 = self._read_whitespace()
                    if address5 is not FAILURE:
                        elements2.append(address5)
                        remaining1 -= 1
                if remaining1 <= 0:
                    address4 = TreeNode(self._input[index3:self._offset], index3, elements2)
                    self._offset = self._offset
                else:
                    address4 = FAILURE
                if address4 is not FAILURE:
                    elements0.append(address4)
                    address6 = FAILURE
                    address6 = self._read_string()
                    if address6 is not FAILURE:
                        elements0.append(address6)
                        address7 = FAILURE
                        index4 = self._offset
                        address7 = self._read_xlist()
                        if address7 is FAILURE:
                            address7 = TreeNode(self._input[index4:index4], index4)
                            self._offset = index4
                        if address7 is not FAILURE:
                            elements0.append(address7)
                            address8 = FAILURE
                            remaining2, index5, elements3, address9 = 0, self._offset, [], True
                            while address9 is not FAILURE:
                                address9 = self._read_whitespace()
                                if address9 is not FAILURE:
                                    elements3.append(address9)
                                    remaining2 -= 1
                            if remaining2 <= 0:
                                address8 = TreeNode(self._input[index5:self._offset], index5, elements3)
                                self._offset = self._offset
                            else:
                                address8 = FAILURE
                            if address8 is not FAILURE:
                                elements0.append(address8)
                            else:
                                elements0 = None
                                self._offset = index1
                        else:
                            elements0 = None
                            self._offset = index1
                    else:
                        elements0 = None
                        self._offset = index1
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
            address0 = TreeNode2(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        self._cache['example'][index0] = (address0, self._offset)
        return address0

    def _read_xlist(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['xlist'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1, elements0 = self._offset, []
        address1 = FAILURE
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 13]
        if chunk0 == '\\begin{xlist}':
            address1 = TreeNode(self._input[self._offset:self._offset + 13], self._offset)
            self._offset = self._offset + 13
        else:
            address1 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\\\\begin{xlist}"')
        if address1 is not FAILURE:
            elements0.append(address1)
            address2 = FAILURE
            remaining0, index2, elements1, address3 = 1, self._offset, [], True
            while address3 is not FAILURE:
                address3 = self._read_example()
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
                address4 = FAILURE
                chunk1 = None
                if self._offset < self._input_size:
                    chunk1 = self._input[self._offset:self._offset + 11]
                if chunk1 == '\\end{xlist}':
                    address4 = TreeNode(self._input[self._offset:self._offset + 11], self._offset)
                    self._offset = self._offset + 11
                else:
                    address4 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"\\\\end{xlist}"')
                if address4 is not FAILURE:
                    elements0.append(address4)
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
        self._cache['xlist'][index0] = (address0, self._offset)
        return address0

    def _read_string(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['string'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        remaining0, index1, elements0, address1 = 0, self._offset, [], True
        while address1 is not FAILURE:
            index2, elements1 = self._offset, []
            address2 = FAILURE
            index3 = self._offset
            index4 = self._offset
            index5, elements2 = self._offset, []
            address3 = FAILURE
            chunk0 = None
            if self._offset < self._input_size:
                chunk0 = self._input[self._offset:self._offset + 3]
            if chunk0 == '\\ex':
                address3 = TreeNode(self._input[self._offset:self._offset + 3], self._offset)
                self._offset = self._offset + 3
            else:
                address3 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"\\\\ex"')
            if address3 is not FAILURE:
                elements2.append(address3)
                address4 = FAILURE
                address4 = self._read_whitespace()
                if address4 is not FAILURE:
                    elements2.append(address4)
                else:
                    elements2 = None
                    self._offset = index5
            else:
                elements2 = None
                self._offset = index5
            if elements2 is None:
                address2 = FAILURE
            else:
                address2 = TreeNode3(self._input[index5:self._offset], index5, elements2)
                self._offset = self._offset
            if address2 is FAILURE:
                self._offset = index4
                chunk1 = None
                if self._offset < self._input_size:
                    chunk1 = self._input[self._offset:self._offset + 11]
                if chunk1 == '\\end{xlist}':
                    address2 = TreeNode(self._input[self._offset:self._offset + 11], self._offset)
                    self._offset = self._offset + 11
                else:
                    address2 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('"\\\\end{xlist}"')
                if address2 is FAILURE:
                    self._offset = index4
                    chunk2 = None
                    if self._offset < self._input_size:
                        chunk2 = self._input[self._offset:self._offset + 13]
                    if chunk2 == '\\begin{xlist}':
                        address2 = TreeNode(self._input[self._offset:self._offset + 13], self._offset)
                        self._offset = self._offset + 13
                    else:
                        address2 = FAILURE
                        if self._offset > self._failure:
                            self._failure = self._offset
                            self._expected = []
                        if self._offset == self._failure:
                            self._expected.append('"\\\\begin{xlist}"')
                    if address2 is FAILURE:
                        self._offset = index4
                        chunk3 = None
                        if self._offset < self._input_size:
                            chunk3 = self._input[self._offset:self._offset + 9]
                        if chunk3 == '\\end{exe}':
                            address2 = TreeNode(self._input[self._offset:self._offset + 9], self._offset)
                            self._offset = self._offset + 9
                        else:
                            address2 = FAILURE
                            if self._offset > self._failure:
                                self._failure = self._offset
                                self._expected = []
                            if self._offset == self._failure:
                                self._expected.append('"\\\\end{exe}"')
                        if address2 is FAILURE:
                            self._offset = index4
            self._offset = index3
            if address2 is FAILURE:
                address2 = TreeNode(self._input[self._offset:self._offset], self._offset)
                self._offset = self._offset
            else:
                address2 = FAILURE
            if address2 is not FAILURE:
                elements1.append(address2)
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
                    elements1.append(address5)
                else:
                    elements1 = None
                    self._offset = index2
            else:
                elements1 = None
                self._offset = index2
            if elements1 is None:
                address1 = FAILURE
            else:
                address1 = TreeNode(self._input[index2:self._offset], index2, elements1)
                self._offset = self._offset
            if address1 is not FAILURE:
                elements0.append(address1)
                remaining0 -= 1
        if remaining0 <= 0:
            address0 = TreeNode(self._input[index1:self._offset], index1, elements0)
            self._offset = self._offset
        else:
            address0 = FAILURE
        self._cache['string'][index0] = (address0, self._offset)
        return address0

    def _read_whitespace(self):
        address0, index0 = FAILURE, self._offset
        cached = self._cache['whitespace'].get(index0)
        if cached:
            self._offset = cached[1]
            return cached[0]
        index1 = self._offset
        chunk0 = None
        if self._offset < self._input_size:
            chunk0 = self._input[self._offset:self._offset + 1]
        if chunk0 == '\n':
            address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
            self._offset = self._offset + 1
        else:
            address0 = FAILURE
            if self._offset > self._failure:
                self._failure = self._offset
                self._expected = []
            if self._offset == self._failure:
                self._expected.append('"\\n"')
        if address0 is FAILURE:
            self._offset = index1
            chunk1 = None
            if self._offset < self._input_size:
                chunk1 = self._input[self._offset:self._offset + 1]
            if chunk1 == '\t':
                address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                self._offset = self._offset + 1
            else:
                address0 = FAILURE
                if self._offset > self._failure:
                    self._failure = self._offset
                    self._expected = []
                if self._offset == self._failure:
                    self._expected.append('"\\t"')
            if address0 is FAILURE:
                self._offset = index1
                chunk2 = None
                if self._offset < self._input_size:
                    chunk2 = self._input[self._offset:self._offset + 1]
                if chunk2 == ' ':
                    address0 = TreeNode(self._input[self._offset:self._offset + 1], self._offset)
                    self._offset = self._offset + 1
                else:
                    address0 = FAILURE
                    if self._offset > self._failure:
                        self._failure = self._offset
                        self._expected = []
                    if self._offset == self._failure:
                        self._expected.append('" "')
                if address0 is FAILURE:
                    self._offset = index1
        self._cache['whitespace'][index0] = (address0, self._offset)
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
        tree = self._read_container()
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
