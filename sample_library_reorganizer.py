import os
from subprocess import Popen
import argparse


class sample_library_reorganizer:

    def __init__(self, search_directory, destination_directory):
        self.flat_folder_keywords = {
            "kick": ["kick", "kicks"],
            "snare": ["snare", "snares", "rim", "rims"],
            "hihat": [],
            "tops": [],
            "percussion": [],
            "loops": [],
            "sfx": [],
            "keys_piano": [],
            "guitar": [],
            "other": []
        }
        self.search_directory = search_directory
        self.destination_directory = destination_directory

    def start(self):
        """
        """
        self._create_sample_folders()
        self._categorize()

    def _create_sample_folders(self):
        """

        """
        for folder in self.flat_folder_keywords.keys():
            directory_path = self.destination_directory + '/' + folder
            if os.path.isdir(directory_path):
                continue
            else:
                os.mkdir(directory_path)

    def _categorize(self):
        # traverse root directory, and list directories as dirs and files as files
        for root, dirs, files in os.walk(self.search_directory):
            path = root.split(os.sep)
            print((len(path) - 1) * '---', os.path.basename(root))
            for file in files:
                print(len(path) * '---', file)
                pass
        pass

        
def parse_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', '--search_path', required=True, help="Provide path(s) to search from", nargs='')
    parse.add_argument('-d', '--destination_path', required=True, help="Provide a path to put new directories and ")
    return parse.parse_args()


def main():
    args = parse_args()

    sample_library_controller = sample_library_reorganizer(
        args.search_directory,
        args.destination_directory
    )
    sample_library_controller.start()


if __name__ == "__main__":
    main()
