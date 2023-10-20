# File Organizer

File Organizer is a Python script that helps you organize files in a directory into categorized folders based on their file extensions. It also allows you to rename files based on custom rules or patterns and logs all file movements.

## Features

1. **Automatic Categorization**: The script automatically categorizes files into folders based on their file extensions. You can customize the category mapping to suit your needs.
   
2. **Logging**: All file movements are logged into a text file, making it easy to track what changes were made to your files.

3. **Extension Customization**: You can interactively specify the category for file types not already in the list during the categorization process.

4. **Truncate Filenames**: File names longer than 15 characters are automatically truncated for better readability in the console output.

## Getting Started

1. Clone this repository to your local machine.

2. Ensure you have Python 3.x installed.

3. Install the required libraries using pip:

4. Open a terminal and navigate to the directory containing the `organizer.py` script.

5. Run the script:


6. Follow the on-screen prompts to categorize and organize your files.

## Usage

### Categorization

- The script scans the current directory for files and categorizes them into predefined folders based on their file extensions.

- For unmapped file extensions, you can interactively specify the category.

### Renaming

- You can define custom renaming rules using placeholders such as `{original}`, `{date}`, `{category}`, and `{custom}`.

- The script will apply these rules to rename files during the organization process.

### Logging

- All file movements are logged in a log file located at `~/.cache/organizer/organizer_log.txt`.

## Customization

- You can customize the category mappings by editing the `category_to_extensions` dictionary in the script.

## Examples

- Example renaming rule: `{date}_{original}` will rename a file to `20231021_example_file.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the [termcolor](https://pypi.org/project/termcolor/) library for colorful console output.
