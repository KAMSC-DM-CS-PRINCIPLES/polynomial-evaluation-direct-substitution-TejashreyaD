def evaluate_polynomial(degree, x, constant_term, *coefficients):
    if len(coefficients) != degree:
        raise ValueError(f"Need {degree} coefficient(s)")

    total = constant_term
    print (f"SO(value of the constant term)= {total}")

    for k in range(1, degree +1):
        value = coefficients[k-1] * x ** k
        total_old= total
        total = total + value
        print(f"S{k} (sum of the {k+1} lowest terms) = {total_old} + ({coefficients[k - 1]} × {x}^{k}) = {total}")

def main():
    while True:
        degree = int(input("Degree of polynomial: "))
        x = float(input("Value of x: "))
        constant_term = float(input("Constant term: "))

        coefficients = []
        for k in range(1, degree + 1):
            coefficients.append(float(input("Coefficient {k}: ")))

            print("\n Evaliauting polynomical...\n")
            final=evaluate_polynomial(degree, x, constant_term, *coefficients)
            print(final)

            except ValueError as e:
            print(e)
            continue

            do_again = input("Do you want to continue?: ")
            if again != "y":
                break
if __name__ == "__main__":
    main()