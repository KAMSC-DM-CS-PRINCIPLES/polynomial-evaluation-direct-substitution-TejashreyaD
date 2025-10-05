def evaluate_polynomial(degree, x, constant_term, *coefficients):
    if len(coefficients) != degree:
        raise ValueError(f"need {degree} coefficient(s), but got {len(coefficients)}.")

    total = constant_term
    print(f"S0 (value of the constant term) = {total}")

    for k in range(1, degree + 1):
        term = coefficients[k - 1] * (x ** k)
        print(f"S{k} (sum of the first {k + 1} terms) = {total} + {coefficients[k - 1]} * ({x}^{k}) = {total + term}")
        total += term

    print(f"P(x) = {total}")
    return total


def main():
    while True:
        try:
            degree = int(input("Degree of the polynomial: "))
            x = float(input("Value of x: "))
            constant_term = float(input("Value of constant term: "))

            coefficients = []
            for k in range(1, degree + 1):
                coeff = float(input(f"Coefficient of the x^{k} term: "))
                coefficients.append(coeff)

            print("\nDesired Outputs")
            print("-" * 20)
            evaluate_polynomial(degree, x, constant_term, *coefficients)

        except ValueError as e:
            print("Error:", e)
            continue

        again = input("Do you want to evaluate another polynomial? (yes/no): ")
        if again.strip().lower() != 'yes':
            break


if __name__ == "__main__":
    main()
