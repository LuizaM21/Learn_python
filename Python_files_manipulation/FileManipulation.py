import os
from pathlib import Path


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
        self.input_file = input_file

    def read_file(self):
        """Automatically close file in the context manager"""
        # check if the file exists and is not empty
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                with open('{}'.format(self.input_file), 'r') as f:
                    f_content = f.read()
                    return f_content
            except Exception as e:
                print(e)
        else:
            print("No such file or directory! ", self.input_file)

    def write_file(self):
        """Create a file and write into it"""
        if os.path.isfile(self.input_file):
            try:
                with open('{}'.format(self.input_file), 'w') as f:
                    print('create and write into file {} '.format(f.name))
                    print('Apply mode: {}'.format(f.mode))
                    file_lines = ['name: Zimbabwe\n', 'alpha2_code: ZW\n', 'alpha3_code: ZWE\n']
                    f.writelines(file_lines)
                    return True
            except Exception as e:
                print(e)
                return
        else:
            print("No such file or directory! ", self.input_file)

    def copy_text_file(self, output_file):
        """Create a copy of an existent file"""
        if os.path.isfile(self.input_file):
            try:
                with open('{}'.format(self.input_file), 'r') as read_f:
                    if not os.path.exists(output_file):
                        Path(output_file).touch()
                        with open('{}'.format(output_file), 'w') as write_f:
                            for line in read_f:
                                write_f.write(line)
                        write_f.close()
                        print("FILE SUCCESSFULLY COPIED UNDER:\n\t{}".format(output_file))
                        return True
                    else:
                        print("FILE ALREADY EXIST UNDER:\n\t{}".format(output_file))
            except Exception as e:
                print(e)
        else:
            print("No such file or directory! ", self.input_file)
            return

    def copy_binary_file(self, output_file):
        """Copy file in binary mode"""
        if os.path.isfile(self.input_file) and os.stat(self.input_file).st_size != 0:
            try:
                with open('{}'.format(self.input_file), 'rb') as read_b:
                    with open('{}'.format(output_file), 'wb') as copy_b:
                        for line in read_b:
                            copy_b.write(line)
                        print("SUCCESSFULLY COPIED FILE INTO: {}".format(output_file))
                        return True
            except Exception as e:
                print(e)
                return
        else:
            print("No such file or directory! ", self.input_file)

    def add_to_existent_file(self):
        """Add content to existent csv file"""
        if os.path.isfile(self.input_file):
            try:
                with open('{}'.format(self.input_file), 'a+') as append_f:
                    new_lines = ['name: Afghanistan\n', 'alpha2_code: AF\n', 'alpha3_code: AFG\n']
                    append_f.writelines(new_lines)
                    append_f.read()
                print("SUCCESSFULLY ADDED CONTENT INTO FILE")
                return True
            except Exception as e:
                print(e)
                return
        else:
            print("NO SUCH FILE OR DIRECTORY!\n\t", self.input_file)

    def count_words(self):
        """Count the number of word in a file"""
        try:
            with open('{}'.format(self.input_file)) as f:
                content = f.read()
                return content
        except FileNotFoundError:
            print("No such file or directory! ", self.input_file)
        finally:
            words = content.split()
            number_words = len(words)
            return number_words


