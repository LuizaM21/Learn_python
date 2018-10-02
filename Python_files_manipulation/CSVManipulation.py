import csv


class CSVManipulation(object):

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_csv_file(self):
        with open('{}'.format(self.input_file), 'r') as read_csv:
            csv_file = csv.reader(read_csv)
            for line in csv_file:
                print(line)

    # read specific column from csv file
    def read_csv_specific_column(self, column_index: object) -> object:
        with open('{}'.format(self.input_file), 'r') as csv_read:
            csv_reader = csv.reader(csv_read)
            # skip the first line
            # next(csv_reader)
            country_list = []
            for line in csv_reader:
                country_list.append(line[column_index])
            print(country_list)

    def copy_csv_column_into_new_file(self, column_index: object):
        with open('{}'.format(self.input_file), 'r') as csv_read:
            csv_reader = csv.reader(csv_read)

            with open('{}'.format(self.output_file), 'w', newline='') as csv_write:
                csv_writer = csv.writer(csv_write)
                output_list = []

                for line in csv_reader:
                    csv_writer.writerow(line[column_index-1:column_index])
                    output_list.append(line[column_index-1:column_index])
                print(output_list)

    def read_csv_as_dictionary(self, column_name):
        with open('{}'.format(self.input_file), 'r') as input_csv:
            csv_reader = csv.DictReader(input_csv)
            for line in csv_reader:
                print(line[column_name])

    def write_csv_as_dictionary(self):
        with open('{}'.format(self.input_file), 'r') as input_csv:
            dict_reader = csv.DictReader(input_csv)

            with open('{}'.format(self.output_file), 'w',  newline='') as output_csv:
                field_names = ['No', 'ISO3', 'CountryName', 'CurrencyCode']
                dict_writer = csv.DictWriter(output_csv, fieldnames=field_names)

                print('\n\n CountryConfig_columns_copy.csv results file\n\n')
                for line in dict_reader:
                    del line['CapitalCity']
                    del line['ISO2']
                    dict_writer.writerow(line)
                    print(line)

