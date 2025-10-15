def evaluate_polynomial_horner(degree, x, constant_term, *coefficients):
    if len(coefficients) != degree:
        raise ValueError(f"need {degree} coefficient(s), but got {len(coefficients)}.")

    # Coefficients are for x^1 to x^n, constant_term is C0
    # For Horner's method, we need all coefficients from highest degree down to constant_term
    # So build the full list: [C_n, C_{n-1}, ..., C_1, C_0]
    all_coeffs = list(coefficients[::-1])  # Reverse coefficients: C_n to C_1
    all_coeffs.append(constant_term)  # Add C0 at the end (lowest power)

    # Horner's method initialization:
    total = all_coeffs[0]
    print(f"S0 (start with highest degree coefficient) = {total}")

    for k in range(1, degree + 1):
        total = total * x + all_coeffs[k]
        print(f"S{k} = S{k - 1} * {x} + {all_coeffs[k]} = {total}")

    print(f"P(x) = {total}")
    return total


def main():
    while True:
        try:
            degree = int(input("Degree of the polynomial: "))
            x = float(input("Value of x: "))
            constant_term = float(input("Value of constant term (C0): "))

            coefficients = []
            for k in range(1, degree + 1):
                coeff = float(input(f"Coefficient of the x^{k} term (C{k}): "))
                coefficients.append(coeff)

            print("\nDesired Outputs (Horner's method)")
            print("-" * 30)
            evaluate_polynomial_horner(degree, x, constant_term, *coefficients)

        except ValueError as e:
            print("Error:", e)
            continue

        again = input("Do you want to evaluate another polynomial with Horner's method? (yes/no): ")
        if again.strip().lower() != 'yes':
            break


if __name__ == "__main__":
    main()
