

class FileManipulation:

    instance = None

    @staticmethod
    def get_instance():
        """
        Verifies if an instance is already created, otherwise create one and saves it,
        to avoid multiple reads of the same file
        :return: a ConfigData instance
        """
        if not FileManipulation():
            FileManipulation.instance = FileManipulation()
        return FileManipulation.instance

    def __init__(self, input_file):
        self.file = input_file

    # automatically close the file using context manager
    def read_file(self):
        with open('{}'.format(self.file), 'r') as f:
            f_content = f.read()
            return f_content

    # create a file and write into it
    def write_file(self):
        print('Call write_file function from FileManipulation class')
        with open('{}'.format(self.file), 'w') as f:
            print('create and write into file {} '.format(f.name))
            print('Apply mode: {}'.format(f.mode))
            file_lines = ['name: Zimbabwe\n', 'alpha2_code: ZW\n', 'alpha3_code: ZWE\n']
            f.writelines(file_lines)
        return True

    # create a copy of an existent file
    def copy_text_file(self, output_file):
        print('\nCall copy_text_file function from FileManipulation class')
        with open('{}'.format(self.file), 'r') as read_f:
            with open('{}'.format(output_file), 'w') as write_f:
                for line in read_f:
                    write_f.write(line)
        return True

    # copy file in binary mode
    def copy_binary_file(self, output_file):
        print('\nCall copy_binary_file function from FileManipulation class')
        with open('{}'.format(self.file), 'rb') as read_b:
            with open('{}'.format(output_file), 'wb') as copy_b:
                for line in read_b:
                    copy_b.write(line)
        return True

    def add_to_existent_file(self):
        print('\nCall add_to_existent_file function from FileManipulation class\n')
        with open('{}'.format(self.file), 'a+') as append_f:
            new_lines = ['name: Afghanistan\n', 'alpha2_code: AF\n', 'alpha3_code: AFG\n']
            append_f.writelines(new_lines)
            append_f.read()
        return True


