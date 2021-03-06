import csv
import os
import pprint


class CSVManipulation:

    def __init__(self, input_file, output_file=""):
        self.input_file = input_file
        self.output_file = output_file

    def read_csv_lines(self):
        """return the content of csv into a list of strings"""
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                csv_data_list = []
                with open('{}'.format(self.input_file), 'r') as read_csv:
                    csv_file = csv.reader(read_csv)
                    for line in csv_file:
                        csv_data_list.append(line[0])
                    return csv_data_list
            except Exception as e:
                return str(e)
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)
            return ""

    def read_csv_specific_column(self, column_index: object) -> object:
        """Read specific column from csv file and return a list"""
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                with open('{}'.format(self.input_file), 'r') as csv_read:
                    csv_reader = csv_read.read().splitlines()
                    # remove the first line with headers
                    del csv_reader[0]
                    column_list = []
                    for line in csv_reader:
                        line = line.split(",")
                        column_list.append(line[column_index])
                return column_list
            except Exception as e:
                return str(e)
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)
            return ""

    def copy_csv_column_into_new_file(self, column_index: object):
        if os.path.isfile(self.input_file):
            try:
                with open('{}'.format(self.input_file), 'r') as csv_read:
                    csv_reader = csv.reader(csv_read)
                    with open('{}'.format(self.output_file), 'w', newline='') as csv_write:
                        csv_writer = csv.writer(csv_write)

                        output_list = []
                        for line in csv_reader:
                            csv_writer.writerow(line[column_index-1:column_index])
                            output_list.append(line[column_index-1:column_index])
                        csv_write.close()
                        print("CONTENT SUCCESSFULLY COPIED UNDER:\n\t{}".format(self.output_file))
                        return True
            except Exception as e:
                print(e)
                return ""
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)
            return ""

    def read_csv_as_dictionary(self, column_name):
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                with open('{}'.format(self.input_file), 'r') as input_csv:
                    csv_reader = csv.DictReader(input_csv)
                    for line in csv_reader:
                        print(line[column_name])
                    return csv_reader
            except Exception as e:
                print(e)
                return ""
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)
            return ""

    def write_csv_as_dictionary(self):
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                with open('{}'.format(self.input_file), 'r') as input_csv:
                    dict_reader = csv.DictReader(input_csv)

                    with open('{}'.format(self.output_file), 'w',  newline='') as output_csv:
                        field_names = ['No', 'ISO3', 'CountryName', 'CurrencyCode']
                        dict_writer = csv.DictWriter(output_csv, fieldnames=field_names)

                        for line in dict_reader:
                            del line['CapitalCity']
                            del line['ISO2']
                            dict_writer.writerow(line)
                            pprint.pprint(line)
                        return True
            except Exception as e:
                print(e)
                return ""
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)
            return ""

    def overwrite_csv_existent_column(self, column_values, column_index):
        """
            Read the existent csv file, modify and store in a new list.
            Write the new list in the same csv file path
        """

        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                with open('{}'.format(self.input_file), 'r') as csv_reader:
                    # obtain each csv line into a list
                    current_csv = csv_reader.read().splitlines()
                    # extract csv headers
                    updated_csv = []
                    for ind, line in enumerate(current_csv):
                        line = line.split(',')
                        # overwrite existent data with new data at a given index list
                        line[column_index] = column_values[ind]
                        updated_csv.append(line)
                    csv_reader.close()

                    with open('{}'.format(self.input_file), 'w', newline='') as csv_write:
                        csv_writer = csv.writer(csv_write)
                        for line in updated_csv:
                            csv_writer.writerow(line)
                            print(line)
                        print("CONTENT UPDATED UNDER:\n\t{}".format(self.input_file))
                        return True
            except Exception as e:
                print(e)
                return ""
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)
            return ""

