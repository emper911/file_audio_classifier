import os
from subprocess import Popen
import argparse


class sample_library_reorganizer:
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
        self._create_sample_folders()
        self._categorize()

    def _create_sample_folders(self):
        """
        """
        
        pass

    def _categorize(self):
        pass

        
def parse_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', '--search_path', required=True, help="Provide path(s) to search from", nargs='')
    parse.add_argument('-d', '--destination_path', required=True, help="Provide a path to put new directories and ")
    return parse.parse_args()

def main():
    args = parse_args()
    sample_library_controller = sample_library_reorganizer(args.search_directory, args.destination_directory)
    sample_library_controller.start()


if __name__ == "__main__":
    main()