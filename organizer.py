import os
import shutil
import logging
from termcolor import colored

import os
import shutil
import json
import logging
from termcolor import colored

# Load Extension-Category Mapping from JSON
def load_extension_mapping(json_path):
    with open(json_path, 'r') as f:
        return json.load(f)

# Configure Logging
def configure_logging(log_file_path):
    logging.basicConfig(filename=log_file_path, level=logging.INFO)

class FileOrganizer:
    def __init__(self, directory, disable_prompt=False):
        self.directory = directory
        self.category_to_extensions = load_extension_mapping('extension_mapping.json')
        self.disable_prompt = disable_prompt
        self.log_file_path = os.path.expanduser("~/.cache/organizer/organizer_log.txt")
        configure_logging(self.log_file_path)
        
    def _categorize_files(self):
        files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f)) and not f.startswith('.')]
        categorized_files = {}
        for file in files:
            for category, extensions in self.category_to_extensions.items():
                if file.split('.')[-1] in extensions:
                    if category not in categorized_files:
                        categorized_files[category] = []
                    categorized_files[category].append(file)
                    break
        return categorized_files

    def _handle_uncategorized_files(self, uncategorized_files):
        uncategorized_extensions = list(set([file.split('.')[-1] for file in uncategorized_files]))
        for ext in uncategorized_extensions:
            user_category = input(f"The extension '.{ext}' is not categorized. Please enter a category: ").strip()
            if user_category not in self.category_to_extensions:
                self.category_to_extensions[user_category] = []
            self.category_to_extensions[user_category].append(ext)

    def _move_files(self, categorized_files):
        for category, files in categorized_files.items():
            dest_dir = os.path.join(self.directory, category)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            for file in files:
                src = os.path.join(self.directory, file)
                dest = os.path.join(dest_dir, file)
                try:
                    shutil.move(src, dest)
                    logging.info(f"{src} --> {dest}")
                    filename, file_extension = os.path.splitext(file)
                    truncated_filename = (filename[:15] + '..') if len(filename) > 15 else filename
                    display_file = f"{truncated_filename}{file_extension}"
                    print(f"{display_file} --> {colored(category, 'red') if category == 'Code' else colored(category, 'blue')}")
                except Exception as e:
                    logging.error(f"Error occurred: {e}")

    def organize(self):
        categorized_files = self._categorize_files()
        all_files = [f for f in os.listdir(self.directory) if os.path.isfile(os.path.join(self.directory, f)) and not f.startswith('.')]
        uncategorized_files = [f for f in all_files if f not in [item for sublist in categorized_files.values() for item in sublist]]
        self._handle_uncategorized_files(uncategorized_files)
        self._move_files(categorized_files)

if __name__ == "__main__":
    directory = os.getcwd()
    organizer = FileOrganizer(directory)
    organizer.organize()
