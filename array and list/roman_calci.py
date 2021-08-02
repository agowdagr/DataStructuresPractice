from collections import deque
def romanToInt(s: str) -> int:
	res, prev = 0, 0
	dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
	for i in s[::-1]:
		if dict[i] >= prev:
			res += dict[i]
		else:
			res -= dict[i]
		prev = dict[i]
	return res

def infix_to_postfix(infix_input: list) -> list:

    precedence_order = {'+': 0, '-': 0, '*': 1, '/': 1, '^': 2}
    associativity = {'+': "LR", '-': "LR", '*': "LR", '/': "LR", '^': "RL"}

    i = 0
    postfix = []
    operators = "+-/*^"
    stack = deque()
    while i < len(infix_input):

        char = infix_input[i]
        if char in operators:
            if len(stack) == 0 or stack[0] == '(':
                stack.appendleft(char)
                i += 1
            else:
                top_element = stack[0]
                if precedence_order[char] == precedence_order[top_element]:
                    if associativity[char] == "LR":
                        popped_element = stack.popleft()
                        postfix.append(popped_element)
                    # if associativity of char is Right to left
                    elif associativity[char] == "RL":
                        stack.appendleft(char)
                        i += 1
                elif precedence_order[char] > precedence_order[top_element]:
                    stack.appendleft(char)
                    i += 1
                elif precedence_order[char] < precedence_order[top_element]:
                    popped_element = stack.popleft()
                    postfix.append(popped_element)
        elif char == '(':
            stack.appendleft(char)
            i += 1
        elif char == ')':
            top_element = stack[0]
            while top_element != '(':
                print(stack)
                popped_element = stack.popleft()
                postfix.append(popped_element)
                top_element = stack[0]
            stack.popleft()
            i += 1
        # char is operand
        else:
            postfix.append(char)
            i += 1

    if len(stack) > 0:
        for i in range(len(stack)):
            postfix.append(stack.popleft())
    # while len(stack) > 0:
    #     postfix.append(stack.popleft())

    return postfix

txt = "( II + III ) * IV"
x = txt.split(" ")
print(x)
postfix = (infix_to_postfix(x))
print(postfix)
stack = []
for i in postfix:
    if (i == "+"):
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 + op2)
    elif (i == "*"):
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 * op2)
    elif (i == "/"):
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 / op2)
    elif (i == "-"):
        op2 = stack.pop()
        op1 = stack.pop()
        stack.append(op1 - op2)
    else:
        stack.append(romanToInt(i))
print(round(stack.pop()))