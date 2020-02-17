import os
from subprocess import Popen
import argparse


class sample_library_reorganizer:
<<<<<<< HEAD

    def __init__(self, search_directory, destination_directory):
        self.flat_folder_keywords = {
            "kick": ["kick", "kicks"],
            "snare": ["snare", "snares", "rim", "rims"],
            "hihat": ["hats", "hat", "hihat", "hi-hat", "open-hat", "pedal-hat", "hh"],
            "tops": ["ride", "crash", "cymbol", ""],
            "percussion": ["toms", ""],
            "loops": [""],
            "sfx": [""],
            "keys_piano": ["piano", "keys", ""],
            "guitars": [""]
            "guitar": [],
            "other": []
        }
        self.search_directory = search_directory
        self.destination_directory = destination_directory

    def start(self):
        """
        """
=======
    def __init__(self, search_directory, destination_directory):
        self.flat_folder = {
            "Drums": [
                "kick",
                "snare",
                "rim",
                "hihat",
                "percussion",
            ],
            "Loops": None,
            "sfx": None,
        }

    
    def start(self):
>>>>>>> f0938dc28a1eb6177f607e3e04a582277dddba2b
        self._create_sample_folders()
        self._categorize()

    def _create_sample_folders(self):
        """
<<<<<<< HEAD

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
=======
        """
        
        pass

    def _categorize(self):
>>>>>>> f0938dc28a1eb6177f607e3e04a582277dddba2b
        pass

        
def parse_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', '--search_path', required=True, help="Provide path(s) to search from", nargs='')
    parse.add_argument('-d', '--destination_path', required=True, help="Provide a path to put new directories and ")
    return parse.parse_args()

<<<<<<< HEAD

def main():
    args = parse_args()

    sample_library_controller = sample_library_reorganizer(
        args.search_directory,
        args.destination_directory
    )
=======
def main():
    args = parse_args()
    sample_library_controller = sample_library_reorganizer(args.search_directory, args.destination_directory)
>>>>>>> f0938dc28a1eb6177f607e3e04a582277dddba2b
    sample_library_controller.start()


if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
>>>>>>> f0938dc28a1eb6177f607e3e04a582277dddba2b
