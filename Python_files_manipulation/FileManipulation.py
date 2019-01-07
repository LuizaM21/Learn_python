

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

    def read_file(self):
        """Automatically close the file using context manager"""
        try:
            with open('{}'.format(self.file), 'r') as f:
                f_content = f.read()
        except FileNotFoundError:
            print("No such file or directory! ", self.file)
        else:
            return f_content

    def write_file(self):
        """Create a file and write into it"""
        try:
            with open('{}'.format(self.file), 'w') as f:
                print('create and write into file {} '.format(f.name))
                print('Apply mode: {}'.format(f.mode))
                file_lines = ['name: Zimbabwe\n', 'alpha2_code: ZW\n', 'alpha3_code: ZWE\n']
                f.writelines(file_lines)
        except FileNotFoundError:
            print("No such file or directory! ", self.file)
        else:
            return True

    def copy_text_file(self, output_file):
        """Create a copy of an existent file"""
        try:
            with open('{}'.format(self.file), 'r') as read_f:
                with open('{}'.format(output_file), 'w') as write_f:
                    for line in read_f:
                        write_f.write(line)
        except FileNotFoundError:
            print("No such file or directory! ", self.file)
        else:
            return True

    def copy_binary_file(self, output_file):
        """Copy file in binary mode"""
        try:
            with open('{}'.format(self.file), 'rb') as read_b:
                with open('{}'.format(output_file), 'wb') as copy_b:
                    for line in read_b:
                        copy_b.write(line)
        except FileNotFoundError:
            print("No such file or directory! ", self.file)
        else:
            return True

    def add_to_existent_file(self):
        """Add content to existent csv file"""
        try:
            with open('{}'.format(self.file), 'a+') as append_f:
                new_lines = ['name: Afghanistan\n', 'alpha2_code: AF\n', 'alpha3_code: AFG\n']
                append_f.writelines(new_lines)
                append_f.read()
        except FileNotFoundError:
            print("No such file or directory! ", self.file)
        else:
            return True

    def count_words(self):
        """Count the number of word in a file"""
        try:
            with open('{}'.format(self.file)) as f:
                content = f.read()
        except FileNotFoundError:
            print("No such file or directory! ", self.file)
        else:
            words = content.split()
            number_words = len(words)
            return number_words


