import  random


list_of_fruits = ["Strawberry", "Persimmon", "Banana","Tomato", "Pear", "Durian", "Blackberry" ]
max_number_of_tries = 0
def select_random_word():
    return random.choice(list_of_fruits).lower()

def main():
    random_word = select_random_word()
    print(random_word)
    max_number_of_tries = len(random_word) + 2
    random_word_after_user_input =( "*" * len(random_word))
    print(random_word_after_user_input)
    user_input_count = 0
    while True:
        if random_word == random_word_after_user_input :
            print("Congratulation! you won!!!!!!!!!!!!!!!!!!!!!!!")
            break
        user_input =  input("Please enter a letter : ").strip().lower()
        user_input_count += 1
        print(f"This is user_input = {user_input}")
        input_index =  int(random_word.find(user_input))
        if input_index >= 0:
            print(input_index)
            random_word_after_user_input = random_word_after_user_input[:input_index] +user_input + random_word_after_user_input[input_index +1:]
            print(f"Congratrulation! The Letter you Enter is Correct  \n The world looks like {random_word_after_user_input} ")
            continue
        else:
            print(f"Ops! Thats wrong. You have {max_number_of_tries - user_input_count} Tries left")
            if max_number_of_tries - user_input_count <= 0:
                print("Thanks for playing")
                break
                    

if __name__ == "__main__":
    main()