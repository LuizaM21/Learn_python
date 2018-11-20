import pprint


def update_a_dictionary():
    country_details = {}
    country = True

    while country:
        """Update an empty dictionary with user input """

        country_name = input("Insert country name: ")
        country_capital = input("Enter country capital: ")
        country_details.setdefault(country_name.title(), country_capital.title())
        pprint.pprint(country_details)
        # flag necessary to break the while loop if user hits q key
        repeat = input("Insert a country and a capital. To finish the process press 'q'")
        if repeat != 'q':
            continue
        else:
            country = False


if __name__ == '__main__':
    update_a_dictionary()

