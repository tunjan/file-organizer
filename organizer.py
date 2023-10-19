import os
import shutil
from termcolor import colored
from datetime import datetime

# Categories Mapping
category_to_extensions = {
    'Pictures': ['jpeg', 'png', 'jpg', 'gif', 'bmp', 'tiff', 'ico', 'jfif', 'webp', 'heif', 'indd', 'ai', 'eps'],
    'Audio': ['mp3', 'wav', 'aiff', 'flac', 'aac', 'ogg', 'wma', 'm4a', 'amr'],
    'Video': ['mp4', 'mkv', 'flv', 'avi', 'mov', 'wmv', 'm4v', 'mpg', 'mpeg', '3gp'],
    'Documents': ['doc', 'docx', 'pdf', 'odt', 'txt', 'rtf', 'tex', 'wpd', 'ods'],
    'Spreadsheets': ['xls', 'xlsx', 'csv', 'ods'],
    'Presentations': ['ppt', 'pptx', 'odp'],
    'Database': ['db', 'accdb', 'mdb', 'sql'],
    'Code': ['html', 'htm', 'css', 'scss', 'js', 'jsx', 'ts', 'tsx', 'php', 'py', 'java', 'c', 'cpp', 'go', 'rb', 'cs', 'sh', 'bat', 'pl', 'r'],
    'Archives': ['zip', 'rar', 'tar', 'gz', '7z', 'arj', 'deb', 'pkg', 'rpm', 'z', 'lz'],
    'DiskImages': ['iso', 'toast', 'vcd'],
    'Fonts': ['fnt', 'fon', 'otf', 'ttf'],
    'System': ['bak', 'cab', 'cfg', 'cpl', 'cur', 'dll', 'dmp', 'drv', 'icns', 'ini', 'lnk', 'msi', 'sys', 'tmp'],
    'GameFiles': ['b', 'dem', 'gam', 'nes', 'rom', 'sav'],
    'CAD': ['dwg', 'dxf'],
    'GIS': ['gpx', 'kml', 'kmz'],
    'Web': ['asp', 'aspx', 'cer', 'cfm', 'csr', 'dcr', 'htm', 'jsp', 'rss', 'xhtml'],
    'Plugin': ['crx', 'plugin'],
    'Scripts': ['js', 'php', 'pl', 'py', 'cgi', 'asp'],
    'Settings': ['cfg', 'ini', 'prf'],
    'Encoded': ['hqx', 'mim', 'uue'],
    'Compressed': ['z', 'gzip'],
    'Logs': ['log', 'dat'],
    '3DFiles': ['3dm', '3ds', 'max', 'obj'],
    'RasterImages': ['raster', 'pxr', 'raw'],
    'VectorFiles': ['svg', 'ai', 'eps'],
    'EBooks': ['epub', 'mobi', 'azw', 'lit', 'pdb'],
    'Email': ['eml', 'msg', 'oft', 'ost', 'pst', 'vcf'],
    'Executables': ['apk', 'bat', 'bin', 'cgi', 'com', 'exe', 'jar', 'msi', 'pl', 'sh', 'wsf'],
    'Crypto': ['cer', 'crt', 'der', 'pfx', 'pem', 'p12', 'p7b', 'p7r'],
    'Virtual': ['vmdk', 'ova', 'ovf'],
    'Configuration': ['cfg', 'conf', 'ini', 'reg'],
    'Scientific': ['cdf', 'dcm', 'fcs', 'fits', 'hdf', 'nc'],
    'Text': ['txt', 'log', 'md', 'nfo', 'conf'],
    'Subtitles': ['srt', 'sub', 'sbv'],
    'Torrents': ['torrent'],
    'Calendar': ['ics']
}

log_file_path = os.path.expanduser("~/.cache/organizer/organizer_log.txt")

def categorize_files(directory):
    # List all Files, excluding hidden files (those starting with a dot)
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and not f.startswith('.')]

    # Initialize an empty dictionary to store categorized files
    categorized_files = {}

    # Populate the categorized_files dictionary
    for file in files:
        for category, extensions in category_to_extensions.items():
            if file.split('.')[-1] in extensions:
                if category not in categorized_files:
                    categorized_files[category] = []
                categorized_files[category].append(file)
                break  # stop looking for other categories for this file

    # Identify unmapped file types
    uncategorized_files = [f for f in files if f not in [item for sublist in categorized_files.values() for item in sublist]]
    uncategorized_extensions = list(set([file.split('.')[-1] for file in uncategorized_files]))
    
    # Ask user to categorize unmapped extensions
    for ext in uncategorized_extensions:
        user_category = input(f"The extension '.{ext}' is not categorized. Please enter a category: ").strip()
        
        # Update category mappings
        if user_category not in category_to_extensions:
            category_to_extensions[user_category] = []
        category_to_extensions[user_category].append(ext)
        
        # Update categorized_files dictionary
        if user_category not in categorized_files:
            categorized_files[user_category] = []
        categorized_files[user_category].extend([f for f in uncategorized_files if f.split('.')[-1] == ext])

    # Move Files to the Categorized Folders
    for category, files in categorized_files.items():
        for file in files:
            src = os.path.join(directory, file)
            dest = os.path.join(directory, category, file)

            # Check if the destination directory exists, if not, create it
            if not os.path.exists(os.path.join(directory, category)):
                os.makedirs(os.path.join(directory, category))
            
            try:
                shutil.move(src, dest)
                filename, file_extension = os.path.splitext(file)
                truncated_filename = (filename[:15] + '..') if len(filename) > 15 else filename
                display_file = f"{truncated_filename}{file_extension}"
                print(f"{display_file} --> {colored(category, 'red') if category == 'Code' else colored(category, 'blue')}")
                log_entry = f"{src} --> {dest}\n"
                log_file = open(log_file_path, "a")
                log_file.write(log_entry)
                log_file.close()
            except Exception as e:
                print(f"Error occurred: {e}")

if __name__ == "__main__":
    directory = os.getcwd()  # Current Working Directory
    categorize_files(directory)
