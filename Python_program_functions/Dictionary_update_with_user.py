import pprint


def update_a_dictionary():
    countries_details = {}
    country = True

    while country:
        """Update an empty dictionary with user input """

        country_name = input("Insert country name:\n")
        country_capital = input("Enter country capital:\n")
        country_currency = input("Enter country currency:\n")
        country_ISO2 = input("Enter ISO2 code for this country:\n")
        country_cities = input("Enter a list of cities for this country:\n")

        # create a subdivision dictionary to group the details for each inserted country
        country_details = countries_details.setdefault(country_name.title(), {})
        country_details.setdefault("Capital city", country_capital.title())
        country_details.setdefault("Currency", country_currency.upper())
        country_details.setdefault("ISO2_code", country_ISO2.upper())
        country_details.setdefault("country cities", [country_cities])

        # flag necessary to break the while loop if user hits q key
        repeat = input("In order to insert another country details press enter. \nTo finish the process press 'q'\n")
        pprint.pprint(countries_details)
        if repeat != 'q':
            continue
        else:
            country = False
    return countries_details


# TODO:  create method to write created JSON into a file
def write_json_into_file(json_content):
    pass


if __name__ == '__main__':
    update_a_dictionary()

