import os
import shutil

# Directory names
IMAGE_DIR = "/IMAGES/"
SVG_DIR = "/SVG/"
SCREENSHOTS_DIR = "/SCREENSHOTS/"
MUSIC_DIR = "/MUSIC/"
VIDEOS_DIR = "/VIDEOS/"
DOCS_DIR = "/DOCS/"
APPLICATIONS_DIR = "/APPLICATIONS/"
ARCHIVE_DIR = "/ARCHIVE/"

# Directory list
DIRECTORIES = [
    IMAGE_DIR, SVG_DIR, SCREENSHOTS_DIR, MUSIC_DIR,
    VIDEOS_DIR, DOCS_DIR, APPLICATIONS_DIR, ARCHIVE_DIR
]

# File extensions
IMAGE_EXT = ["png", "jpg", "jpeg", "gif", "jfif"]
SVG_EXT = ["svg"]
SCREENSHOT_EXT = ["greenshot"]
MUSIC_EXT = ["mp3"]
VIDEO_EXT = ["mp4"]
DOCS_EXT = ['doc', 'docx', 'odt', 'pdf', 'xls', 'xlsx', 'ods', 'ppt', 'pptx', 'txt']
APPLICATION_EXT = ["exe", "msi"]
ARCHIVE_EXT = ["zip", "rar"]

# Current directory
PATH = os.path.dirname(__file__)

# Shorthand functions
exists = lambda p: os.path.exists(p)
listdir = lambda p: os.listdir(p)
get_extension = lambda f: f.split(".")[-1].lower()
move_file = lambda file_, dir_: shutil.move(PATH + "/" + file_, PATH + dir_ + file_)

# List files in the directory (exclude subdirectories)
FILES = [file for file in listdir(PATH) if os.path.isfile(os.path.join(PATH, file))]


def make_directories():
    for DIR in DIRECTORIES:
        dir_path = PATH + DIR
        if not exists(dir_path):
            os.mkdir(dir_path)


# Make necessary directories before moving forward
make_directories()


def organize_files():
    for file in FILES:
        file_extension = get_extension(file)
        try:
            if file_extension in IMAGE_EXT:
                if "Greenshot" in file:
                    move_file(file, SCREENSHOTS_DIR)
                else:
                    move_file(file, IMAGE_DIR)

            elif file_extension in MUSIC_EXT:
                move_file(file, MUSIC_DIR)

            elif file_extension in VIDEO_EXT:
                move_file(file, VIDEOS_DIR)

            elif file_extension in DOCS_EXT:
                move_file(file, DOCS_DIR)

            elif file_extension in APPLICATION_EXT:
                move_file(file, APPLICATIONS_DIR)

            elif file_extension in ARCHIVE_EXT:
                move_file(file, ARCHIVE_DIR)

            elif file_extension in SVG_EXT:
                move_file(file, SVG_DIR)

        except Exception as e:
            print(f"Failed to move file {file}: {e}")


organize_files()

