#10. Bygg en enkel miniräknare med stöd för +, -, *, och /.

def calculate(expression):
    import re
    # Splitta uttrycket i siffror och operatorer
    tokens = re.findall(r'\d+|\+|\-|\*|\/', expression)
    if not tokens:
        return "Ogiltigt uttryck"

    # Första passet: Multiplikation och division
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '*':
            stack[-1] = stack[-1] * int(tokens[i + 1])
            i += 1
        elif token == '/':
            stack[-1] = stack[-1] / int(tokens[i + 1])
            i += 1
        else:
            stack.append(int(token) if token.isdigit() else token)
        i += 1

    # Andra passet: Addition och subtraktion
    result = stack[0]
    i = 1
    while i < len(stack):
        operator = stack[i]
        operand = stack[i + 1]
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        i += 2

    return result

# Testa funktionen
expression = input("Ange ett matematiskt uttryck (t.ex. 2 + 3 * 4 - 5): ")
try:
    print("Resultat:", calculate(expression))
except Exception as e:
    print("Fel vid beräkning:", e)
