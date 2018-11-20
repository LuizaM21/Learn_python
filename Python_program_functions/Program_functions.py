"""Interrupt a program only when the specific key is being used"""


def main():
    prompt = "\nTo end this process press 'q'."
    prompt += "\nPlease enter your name: "

    message = ""

    while message != 'q':
        message = input(prompt)
        print(message)


if __name__ == '__main__':
    main()

