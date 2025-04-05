#add import
from question_d import get_assessment_value, get_tax_assessed

if __name__ == "__main__":
    while True:
        try:
            user_input = input("Enter value of the property or 'q' to exit the program: ")
            if user_input.lower() == 'q':
                print("Exiting Program")
                break
            
            value_of_property = float(user_input)
            assessment_value = get_assessment_value(value_of_property)
            tax = get_tax_assessed(assessment_value)

            print(f"Assessment Value is  ${assessment_value:.2f}")
            print(f"Property Tax is ${tax:2f}")

        except ValueError:
            print("Invalid input, enter a number for the property value")

