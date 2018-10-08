

class FileManipulation(object):

    # automatically close the file using context manager
    def read_file(self):
        print('\nCall read_file method')
        with open('{}'.format(self), 'r') as f:
            f_content = f.read(50)
            print(f_content)

    # create a file and write into it
    def write_file(self):
        print('\nCall write_file function from FileHandling class')
        with open('{}'.format(self), 'w') as f:
            print(f.name)
            print(f.mode)
            file_lines = ['name: Zimbabwe\n', 'alpha2_code: ZW\n', 'alpha3_code: ZWE\n']
            f.writelines(file_lines)

    # create a copy of an existent file
    def copy_text_file(self, output_file):
        print('\nCall copy_text_file function from FileHandling class')
        with open('{}'.format(self), 'r') as read_f:
            with open('{}'.format(output_file), 'w') as write_f:
                for line in read_f:
                    write_f.write(line)

    # copy file in binary mode
    def copy_binary_file(self, output_file):
        print('\nCall copy_binary_file function from FileHandling class')
        with open('{}'.format(self), 'rb') as read_b:
            with open('{}'.format(output_file), 'wb') as copy_b:
                for line in read_b:
                    copy_b.write(line)

    def add_to_existent_file(self):
        print('\nCall add_to_existent_file function from FileHandling class\n')
        with open('{}'.format(self), 'a+') as append_f:
            new_lines = ['name: Afghanistan\n', 'alpha2_code: AF\n', 'alpha3_code: AFG\n']
            append_f.writelines(new_lines)
            append_f.read()

