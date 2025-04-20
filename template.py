
"""
This script creates a predefined list of files and their parent directories if they do not already exist.
Modules:
    - os: Provides a way of using operating system-dependent functionality.
    - pathlib.Path: Offers an object-oriented approach to handling filesystem paths.
    - logging: Used for tracking events that happen during the execution of the program.
Global Variables:
    - list_of_files (list): A list of file paths (relative to the script's directory) to be created.
Functionality:
    - Iterates through the `list_of_files`.
    - Normalizes each file path to be OS-independent using `Path.resolve()`.
    - Checks if the parent directory of the file exists:
        - If not, creates the directory and logs the action.
    - Checks if the file exists:
        - If not, creates the file and logs the action.
        - If it exists, logs that the file already exists.
"""
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    # Normalize the file path to be OS-independent
    file_path = file_path.resolve()
    logging.info(f"Processing: {file_path}")
    
    # Create parent directories if they don't exist
    if not file_path.parent.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {file_path.parent}")
    
    # Create the file if it doesn't exist
    if not file_path.exists():
        file_path.touch()
        logging.info(f"Created file: {file_path}")
    else:
        logging.info(f"File already exists: {file_path}")