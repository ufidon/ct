# https://en.wikipedia.org/wiki/Shunting_yard_algorithm
# https://gregorycernera.medium.com/converting-regular-expressions-to-postfix-notation-with-the-shunting-yard-algorithm-63d22ea1cf88
def insert_concatenation_operators(regex):
    """Inserts explicit concatenation operators ('⋅') in the regex."""
    output = ""
    operators = {'+', '*', '⋅', '(', ')'}
    
    for i in range(len(regex)):
        output += regex[i]
        if i + 1 < len(regex):
            # Check if we need to insert '⋅'
            if ((regex[i] not in operators) or regex[i] == ')' or regex[i] == '*') and ((regex[i+1] not in operators) or regex[i+1] == '('):
                output += '⋅'  # Insert explicit concatenation operator
    return output

def infix_to_postfix(regex):
    """Converts infix regex to postfix notation using the Shunting-Yard algorithm."""
    operators = {'+', '*', '⋅', '(', ')'}
    precedence = {'*': 3, '⋅': 2, '+': 1, '(':0}  # Operator precedence
    output = []
    operator_stack = []

    for token in regex:
        if token not in operators:  # If it's a letter, append to output
            output.append(token)
        elif token == '(':  # Push '(' to stack
            operator_stack.append(token)
        elif token == ')':  # Pop until '(' is found
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            operator_stack.pop()  # Remove '(' from stack
        else:  # Operator handling (*, ⋅, +)
            while operator_stack and (precedence[operator_stack[-1]] != '(') and (precedence[operator_stack[-1]] > precedence[token] or (token != '*' and precedence[operator_stack[-1]] == precedence[token])):
                output.append(operator_stack.pop())
            operator_stack.append(token)

    # Pop any remaining operators
    while operator_stack:
        output.append(operator_stack.pop())

    return "".join(output)  # Convert list to string

# Given regular expression
# regex = "α(a+b)*b(虫🦆)*"
regex = "a(a+b)*b"

# Step 1: Insert concatenation operators
regex_with_concat = insert_concatenation_operators(regex)
print(f"Regex with concatenation operators: {regex_with_concat}")

# Step 2: Convert to postfix notation
postfix_regex = infix_to_postfix(regex_with_concat)
print(f"Postfix notation: {postfix_regex}")
