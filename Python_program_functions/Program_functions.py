

def decrease_list_of_users():
    """ iterate over a list using while loop
        If we modify a list using a for loop,
        python will loose track of the items in the list.
        For all types of modifications we can use while loop"""

    unconfirmed_users = ['tony', 'frances', 'mike', 'katie', 'jack']
    confirmed_users = []

    while unconfirmed_users:
        print("\nLength of unconfirmed_users: ", len(unconfirmed_users))

        current_user = unconfirmed_users.pop()
        print("current user: ", current_user.title())

        confirmed_users.append(current_user)
        print("length of confirmed_users: ", len(confirmed_users))


def main():
    """Interrupt a program only when the specific key is being used"""

    prompt = "\nTo end this process press 'q'."
    prompt += "\nPlease enter your name: "

    active = True
    while active:
        message = input(prompt)
        if message == 'q':
            active = False
        else:
            print(message)

    decrease_list_of_users()


if __name__ == '__main__':
    main()

