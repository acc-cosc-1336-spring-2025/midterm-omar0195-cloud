from question_a import reverse_string

def main():

    while True:

        user_input = input("Enter reverse string ")

        result_reversed = reverse_string(user_input)
        print(f"Reverse String is: {result_reversed}")

    
            
main()