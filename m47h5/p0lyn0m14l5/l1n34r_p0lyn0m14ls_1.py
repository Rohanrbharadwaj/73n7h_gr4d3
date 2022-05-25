#this program finds the zero of a linear polynomial
#please use spacing between terms 

exp = input("expression : ")
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
        coeff = int(i[:-1])
    else :
        const = int(i.replace('+',''))

print((0-const)/coeff)