# File Organizer

## Description

The File Organizer script helps you manage your cluttered directories by categorizing and moving files into appropriate folders. It's a Python script that scans a directory, identifies the type of each file based on its extension, and then moves it into a corresponding folder.

## Features

- Categorizes files based on their extensions.
- Creates folders dynamically based on file categories.
- Handles uncategorized files by prompting the user for input.
- Logs all file moves for later review.

## Dependencies

- Python 3.x
- termcolor (`pip install termcolor`)

## Setup

1. Clone the repository or download the `file_organizer.py` script.
2. Navigate to the directory containing the script in the terminal.
3. Install the required package by running `pip install termcolor`.

## Usage

1. Place the `file_organizer.py` script in the directory you want to organize.
2. Open a terminal and navigate to the directory containing the script.
3. Run `python file_organizer.py`.

After running the script, you'll find that all the files have been moved into folders that categorize them based on their types.

### Adding Custom Categories

The script will prompt you to categorize any unrecognized file extensions. Simply enter the desired category when prompted.

## Support

For any questions or issues, please open an issue on GitHub or contact the maintainer directly.

## License

This project is licensed under the MIT License.
