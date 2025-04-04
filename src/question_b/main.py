#add import

import question_b

def main():
    quit_program = False
    while not quit_program:

        day_of_week = input('Enter a number inside range of 1 through 7 or "quit" to quit program:')
        
        if day_of_week.lower() == "quit":
            print ("Ending program")
            quit_program = True

        elif day_of_week.isdigit():
            number = int(day_of_week)
            result = question_b.get_day_of_the_week (number)

            print (result)

main()

