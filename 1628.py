# Ref: https://leetcode.com/problems/design-an-expression-tree-with-evaluate-function/discuss/910018/C%2B%2BPython-The-Intended-Solution-During-The-Interview-Polymorphism

import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass

class BinaryNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def evaluate(self) -> int:
        pass

class Plus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()

class Minus(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()

class Mul(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()

class Div(BinaryNode):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()

class Num(Node):
    def __init__(self, val):
        self.val = val
    def evaluate(self) -> int:
        return self.val

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        operator = {'+': Plus, '-': Minus, '*': Mul, '/': Div}
        stack = []
        for token in postfix:
            if token in operator:
                R = stack.pop()
                L = stack.pop()
                stack.append(operator[token](L, R))
            else:
                stack.append(Num(int(token)))
        return stack[0]
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""
