import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "multilingual"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/helper.py",
    ".env",
    "requirements.txt",
    "app.py",
    "research/trials.ipynb","setup.py"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")

