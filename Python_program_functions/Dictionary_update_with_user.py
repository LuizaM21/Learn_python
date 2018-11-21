import pprint


def update_a_dictionary():
    countries_details = {}
    country = True

    while country:
        """Update an empty dictionary with user input """

        country_name = input("Insert country name: ")
        country_capital = input("Enter country capital: ")
        country_currency = input("Enter country currency: ")
        country_ISO2 = input("Enter ISO2 code for this country: ")

        country_details = countries_details.setdefault(country_name.title(), {})
        country_details.setdefault("Capital city", country_capital.title())
        country_details.setdefault("Currency", country_currency.upper())
        country_details.setdefault("ISO2_code", country_ISO2.upper())

        # flag necessary to break the while loop if user hits q key
        repeat = input("In order to insert another country details press enter. \nTo finish the process press 'q'\n")
        pprint.pprint(countries_details)
        if repeat != 'q':
            continue
        else:
            country = False


if __name__ == '__main__':
    update_a_dictionary()

