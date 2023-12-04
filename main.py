class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()

    def top(self):
        if self.isEmpty():
            return None
        else:
            return self.items[-1]

    def size(self):
        return len(self.items)

def isNumber1(char):
    return char in "123456789."

def isNumber(char):
    try:
        float(char)
        return True
    except:
        return False


def isOperator(char):
    return char in "+-*/^"


def precedence(op):
    if op == "^":
        return 3
    elif op in "*/":
        return 2
    elif op in "+-":
        return 1
    else:
        return 0


def operate(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return None
        else:
            return a / b
    elif op == "^":
        return a ** b
    else:
        return None


def infix_to_postfix(expression):
    stack_input = Stack()
    stack_output = Stack()
    stack_postfix = Stack()
    postfix = ""
    num = ""

    for char in expression:
        if isNumber1(char):
            num += char

        elif isOperator(char):
            if num != "":
                stack_output.push(num)
                num = ""
            index = expression.index(char)
            if char == "-" and expression[index-1] == "(":
                stack_output.push("0")

            while not stack_input.isEmpty() and precedence(stack_input.top()) >= precedence(char):
                stack_output.push(stack_input.pop())

            stack_input.push(char)

        elif char == "(":
            if num != "":
                stack_output.push(num)
                num = ""
            stack_input.push(char)

        elif char == ")":
            if num != "":
                stack_output.push(num)
                num = ""

            while not stack_input.isEmpty() and stack_input.top() != "(":
                stack_output.push(stack_input.pop())

            if stack_input.isEmpty():
                return None

            stack_input.pop()

        elif char == " ":
            continue

        else:
            return None

    if num != "":
        stack_output.push(num)

    while not stack_input.isEmpty():

        if stack_input.top() in "()":
            return None
        stack_output.push(stack_input.pop())

    # while not stack_output.isEmpty():
    #     stack_postfix.push(stack_output.pop())

    result = []
    while not stack_output.isEmpty():
        result.append(stack_output.pop())

    return (list(result[::-1]))


def calculate(exp):
    stack_operand = Stack()

    for char in exp:
        if isNumber(char):
            stack_operand.push(float(char))

        elif isOperator(char):
            b = stack_operand.pop()
            a = stack_operand.pop()

            if a is None or b is None:
                return None

            result = operate(a, b, char)

            if result is None:
                return None

            stack_operand.push(result)

        else:
            return None

    result = stack_operand.pop()

    if not stack_operand.isEmpty():
        return None

    return result


def calculator(exp):
    postfix = infix_to_postfix(exp)

    if postfix is None:
        print("error")

    else:
        result = calculate(postfix)

        if result is None:
            print("error")

        else:
            print(f"the result is {result}")



n = input()

calculator(n)