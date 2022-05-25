from cmath import sqrt


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
print(coeffs)

for i in coeffs:
    if not any(c.isalpha() for c in i):
        const = int(i)
    elif any(c.isalpha() for c in i):
        if '^2' in i :
            if i.replace('+','')[:-3] == '' :
                coeffa = 1
            else :
                coeffa = int(i.replace('+','')[:-3])
        else :
            if i.replace('+','')[:-3] == '' :
                coeffb = 1
            else :
                coeffb = int(i[:-1])

alph = 0
beta = 0

#alpha + beta = -b/a
#alpha * beta = c/a
#zero = (-b +- abs(sqrt(coeffb^2 - 4*coeffa*const)))/2*coeffa

reality = coeffb^2 - 4 * coeffa * const

if reality == 0 :
    zero = - coeffb / 2 * coeffa