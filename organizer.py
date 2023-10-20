import os
import shutil
import logging
from termcolor import colored

class FileOrganizer:
    def __init__(self, directory):
        self.directory = directory
        self.category_to_extensions = {
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
        self.log_file_path = os.path.expanduser("~/.cache/organizer/organizer_log.txt")
        logging.basicConfig(filename=self.log_file_path, level=logging.INFO)
        
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
