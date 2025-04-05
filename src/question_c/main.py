#add import
import question_c

def main():
    
    print(f"The initial value of global_num is {question_c.get_global_num()}")
    
    question_c.use_global()

    print(f"The modified value of global_num is {question_c.get_global_num()}")

main()