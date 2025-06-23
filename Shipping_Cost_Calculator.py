# Shipping Cost Calculator

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_shipping_cost(weight, rate):
    return weight * rate

def main():
    print("=== Shipping Cost Calculator ===")
    ## Input package weight and shipping rate
    weight = get_positive_float("Enter the package weight in kilograms: ")
    rate = get_positive_float("Enter the shipping rate per kilogram: ")
    ## Calculate shipping cost
    shipping_cost = calculate_shipping_cost(weight, rate)
    ## Display the result
    print(f"Shipping Cost: ${shipping_cost:,.2f} USD")

if __name__ == "__main__":
    main()