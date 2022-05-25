# This program finds the zero of a linear polynomial
# Please use spacing between terms


def eval_linear(expression: str) -> int:
    terms = []
    op = ""
    const = 0

    for i in exp.split(" "):
        if i == "-" or i == "+":
            op = i
        elif op:
            terms.append(str(op) + str(i))
            op = ""
        else:
            terms.append(i)

    for i in terms:
        if any(c.isalpha() for c in i):
            if len(i) == 1:
                coeff = 1
            elif len(i) == 2 and i[0] == "-":
                coeff = -1
            else:
                coeff = int(i[:-1])
        else:
            const = int(i.replace("+", ""))

    return (0 - const) / coeff


exp = input("Expression : ")
print(eval_linear(exp))
