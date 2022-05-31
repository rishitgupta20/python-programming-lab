from datetime import datetime


def log_info(name, choice, str):
    ptr = open(f"{name}.log.{choice}.txt", "a")
    s1 = f"[{Given_time()}]  -->   {str}\n"
    ptr.write(s1)


def Read_logs(name, choice):
    ptr = open(f"{name}.log.{choice}.txt", "r")
    print()
    for line in ptr:
        print(line, end="")


def Given_time():
    return datetime.now()


def Main_input():
    name = input("Enter your user name: ")

    print('''
What do you want to Enter: Diet or Exercise log
Enter "diet" for Enter Diet log.
Enter "exercise" for Enter Exercise log.
Or type "read" to read log.
    ''')
    choice = input()

    if choice == "diet" or choice == "exercise":
        str = input("Enter the log: ")
        log_info(name, choice, str)

    elif choice == "read":
        choice1 = input("Which log do you want to read: ")
        Read_logs(name, choice1)


if __name__ == "__main__":
    Main_input()
