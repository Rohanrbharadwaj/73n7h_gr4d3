# This program finds the zeroes of a quadratic polynomial, if they just so happen to be real
# Please use spacing between terms

def eval_quadratic(exp: str) -> None:
    if "^2" not in expression:
        print("Expression's not quadratic")

    terms = []
    op = ""
    coeff_b = const = 0

    for i in exp.split(" "):
        if i == "-" or i == "+":
            op = i
        elif op:
            terms.append(str(op) + str(i))
            op = ""
        else:
            terms.append(i)
    print()

    for i in terms:
        if not any(c.isalpha() for c in i):
            const = int(i)
        elif "^2" in i:
            if len(i) == 3:
                coeff_a = 1
            elif i[:-3] == "-":
                coeff_a = -1
            else:
                coeff_a = int(i.replace("+", "")[:-3])
        else:
            if i[:-1] == "+":
                coeff_b = 1
            elif i[:-1] == "-":
                coeff_b = -1
            else:
                coeff_b = int(i[:-1])

    # If a quadratic polynomial is give by ax^2 +  bx + c
    # sum of roots = -b/a
    # product of roots = c/a
    # zeroes = (-b +- sqrt(b^2 - 4*a*c)) / 2*coeffa

    discriminant = (coeff_b) ** 2 - (4 * coeff_a * const)
    print("Discriminant = {}".format(discriminant))

    if discriminant == 0:
        zero = -coeff_b / (2 * coeff_a)
        print("The zeroes are real and identitical")
        print("α = β = {}".format(zero))
    elif discriminant > 0:
        rooted = discriminant ** (0.5)
        alpha = (-coeff_b + rooted) / (2 * coeff_a)
        beta = (-coeff_b - rooted) / (2 * coeff_a)
        print("The zeroes are real and unique")
        print("α = {}".format(alpha))
        print("β = {}".format(beta))
    else:
        print("The zeroes are imaginary")


expression = input("Expression : ")
eval_quadratic(expression)
