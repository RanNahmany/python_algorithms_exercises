#   Matala 1 / Python Algorithms Course
#   
#   Made by:
#   Ran Nahmany (רן נחמני) / ID: 209137421

from abc import ABC
from numpy import double
from abc import ABC,abstractmethod
import string

class Expression(ABC):
    @abstractmethod
    def calc(self)->double:
        pass

# implement the classes here
class Num(Expression):
    def __init__(self,num:int):
        self.num=num

    def calc(self)->int:
        return self.num

class BinExp(Expression):
    def __init__(self, left:Expression,right:Expression):
        self.left=left
        self.right=right
    
    @abstractmethod
    def calc(self)->double:
        pass

class Plus(BinExp):
    def calc(self):
        return self.left.calc()+self.right.calc()

class Minus(BinExp):
    def calc(self):
        return self.left.calc()-self.right.calc()

class Mul(BinExp):
    def calc(self):
        return self.left.calc()*self.right.calc()
    
class Div(BinExp):
    def calc(self):
        return self.left.calc()/self.right.calc()

# Part 1 - This function recived a string and return a queue of the expression by the Shunting Yard Algorithm
def ShuntingYardAlgorithm(expression:str)->list:
    queue:list = []
    stack:list = []

    add_minus = False

    # operators = {"+":operator.add, "-":operator.sub, "*":operator.mul, "/":operator.truediv}
    operators = {"+", "-", "*", "/"}

    i = 0
    while i < len(expression):
        if expression[i] in string.digits:  # if char is a digit
            #  parse the multi-digit number and update the index
            num = ""
            starting_index = i

            while i < len(expression) and expression[i] in string.digits:
                num += expression[i]
                i += 1
            i -= 1

            if (expression[starting_index-1] == "-" and expression[starting_index-2] == "(" and expression[i+1] == ")") and expression[starting_index-3] != "-":
                num = "-" + num
            
            elif add_minus and expression[starting_index-3] != "-":
                num = "-" + num

            add_minus = False
            queue.append(int(num))

        elif expression[i] in operators:    # if char is an operator
            if expression[i-1] != "(":   # if the char is not Minus
                if stack:
                    if stack[-1] in "*/":    
                        queue.append(stack.pop())
                if expression[i] == "-" and expression[i-1] != "(": # and expression[i-2] != "-":
                    add_minus = True
                    stack.append("+")
                else:
                    stack.append(expression[i])
        elif expression[i] == "(":        # if char is a left parenthesis
            stack.append(expression[i])
        elif expression[i] == ")":      # if char is a right parenthesis
            while stack[-1] != "(":     # while the top of the stack is not a left parenthesis
                queue.append(stack.pop())
            stack.pop()

        i += 1

    while stack:
        queue.append(stack.pop())
    
    # print (queue)

    return queue

# Part 2 - The Implementation of the parser function - This function recived the queue from the ShuntingYardAlgorithm function and calculate the expression
def calc(expression:list)->int:
    stack:list = []
    operators = {"+":Plus, "-":Minus, "*":Mul, "/":Div}

    for char in expression:
        if char in operators:
            right = Num(stack.pop())
            left = Num(stack.pop())
            calc_it = (operators[char](left, right)).calc()
            stack.append(calc_it)
        else:
            stack.append(char)
    
    return stack.pop()


# The parser function was implemented by using the ShuntingYardAlgorithm function and the calc function from above
def parser(expression)->double:
    fixed_expression = ShuntingYardAlgorithm(expression)
    calc_it = calc(fixed_expression)

    return calc_it
