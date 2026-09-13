# import modules and global variables
from pathlib import Path
import shutil

base_dir = Path("your path")
target_dir = base_dir / "sorted"


# declare categories and extensions
FILE_CATEGOIRES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "archives": [".zip", ".rar", ".tar", ".gz", ".7z"]
}


# create directories based on categories
def create_category_directories():
    for category,_ in FILE_CATEGOIRES.items():
        (target_dir / category).mkdir(parents=True,exist_ok=True)


# searching and categorizing files
def search_and_categorize_file():
    for file in base_dir.rglob("*"):
        for category,extensions in FILE_CATEGOIRES.items():
            if file.suffix in extensions:
                try:
                    shutil.copy(file,target_dir / category)
                except shutil.SameFileError:
                    pass

# run the application
create_category_directories()
search_and_categorize_file()