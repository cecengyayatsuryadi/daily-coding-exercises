def get_user_input():
    while True:
        answer = input("Do you love me? (y/n) ")
        if answer.lower() in ["y", "n"]:
            return answer.lower()
        else:
            print("Please answer with 'y' or 'n'.")


def process_user_input(answer):
    if answer == "y":
        print("I love you too.")
    else:
        print("No one loves me :).")


def main():
    answer = get_user_input()
    process_user_input(answer)


if __name__ == "__main__":
    main()
