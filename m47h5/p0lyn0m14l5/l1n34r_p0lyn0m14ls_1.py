# This program finds the zero of a linear polynomial
# Please use spacing between terms 

def eval_linear(expression: str) -> int:
    coeffs = []
    op = ''

    for i in exp.split(' '):
        if i == '-' or i == '+' or i == '/' or i == '*':
            op = i
        elif not op=='' :
            coeffs.append(str(op)+str(i))
            op = ''
        else :
            coeffs.append(i)

    for i in coeffs:
        if any(c.isalpha() for c in i):
            if len(i) == 1:
                coeff = 1
            else:
               coeff = int(i[:-1])           
        else :
            const = int(i.replace('+',''))

    return (0-const)/coeff

exp = input("Expression : ")
print(eval_linear(exp))
