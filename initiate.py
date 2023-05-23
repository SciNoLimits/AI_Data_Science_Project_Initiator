"""
This script generates a project directory structure based on the `dir_struct` dictionary. 
It creates directories and files recursively according to the specified structure. 
After creating the project structure, it provides an option to open the project in Visual Studio Code.

The directory structure is defined using a nested dictionary `dir_struct`. 
Each key represents either a directory or a file, prefixed with "d-" or "f-" respectively. 
The script traverses the dictionary recursively and creates directories and files accordingly.

The script also uses the `colorama` library to display colored output in the console.

Functions:
- show_progress(path: str, file_name: str, level: int = 0, log_type: str = "INFO") -> None:
    Displays the progress of file creation with colored output.

- show_error(path: str, file_name: str, level: int = 0, log_type: str = "INFO") -> None:
    Displays an error message for file creation with colored output.

- create_dir(path: str, level: int = 1) -> None:
    Creates a directory at the specified path and displays the progress or error message.

- create_file(path: str, level: int = 1) -> None:
    Creates a file at the specified path and displays the progress or error message.

- create_project(dic: dict) -> None:
    Creates a project directory structure based on the provided dictionary.

- open_in_vscode() -> None:
    Opens the generated project in Visual Studio Code using the `code` command.

- main() -> None:
    The main function that orchestrates the project creation process. 
    It calls the `create_project` function and prompts the user to open the project in Visual Studio Code.

Note: This code assumes that the `colorama` library is installed in the Python environment.
"""


import os
import sys
from colorama import Fore, Style

DIR = str(input(f"{Fore.LIGHTCYAN_EX}Your Project Name >>> {Style.RESET_ALL}"))
dir_struct = {
    f"d-{DIR}": {
        "f-LICENSE": {},
        "f-Makefile": {},
        "f-README.md": {},
        "d-data": {"d-external": {}, "d-interm": {}, "d-processed": {}, "d-raw": {}},
        "d-docs": {},
        "d-models": {},
        "d-notebooks": {},
        "d-references": {},
        "d-reports": {"d-figures": {}},
        "f-requirements.txt": {},
        "f-setup.py": {},
        "d-src": {
            "f-__init__.py": {},
            "d-data": {"f-make_dataset.py": {}},
            "d-features": {"f-build_features.py": {}},
            "d-models": {"f-predict_model.py": {}, "f-train_model.py": {}},
            "d-visualization": {"f-visualize.py": {}},
        },
        "f-tox.ini": {},
    }
}


def show_progress(
    path: str, file_name: str, level: int = 0, log_type: str = "INFO"
) -> None:
    """
    Displays the progress of file creation with colored output.

    Args:
        path (str): The path of the file or directory.
        file_name (str): The name of the file or directory.
        level (int, optional): The level of nesting in the directory structure. Defaults to 0.
        log_type (str, optional): The type of log to display. Can be "INFO" or "DEBUG". Defaults to "INFO".
        
    Returns:
        None
    """
    pattern = (
        Fore.LIGHTYELLOW_EX
        + Style.BRIGHT
        + "│\t" * (level - 1)
        + "├"
        + "─" * 4
        + Style.RESET_ALL
    )
    if log_type.upper() == "INFO":
        print(pattern + Fore.GREEN + Style.BRIGHT + f"{file_name}" + Style.RESET_ALL)

    if log_type.upper() == "DEBUG":
        print(pattern + Fore.GREEN + f"{file_name} >>> {path}" + Style.RESET_ALL)
    return None


def show_error(
    path: str, file_name: str, level: int = 0, log_type: str = "INFO"
) -> None:
    """
    Displays an error message indicating that a file or directory already exists.

    Args:
        path (str): The path of the file or directory that already exists.
        file_name (str): The name of the file or directory.
        level (int, optional): The level of indentation in the directory structure. Defaults to 0.
        log_type (str, optional): The type of log message. Can be "INFO" or "DEBUG". Defaults to "INFO".

    Returns:
        None
    """
    pattern = (
        Fore.LIGHTYELLOW_EX
        + Style.BRIGHT
        + "│\t" * (level - 1)
        + "├"
        + "─" * 4
        + Style.RESET_ALL
    )
    if log_type.upper() == "INFO":
        print(pattern + Fore.RED + Style.BRIGHT + f"{file_name}" + Style.RESET_ALL)

    if log_type.upper() == "DEBUG":
        print(
            f"{pattern}Already Exists{Fore.RED}"
            + f"{file_name} >>> {path}"
            + Style.RESET_ALL
        )
    return None


def create_dir(path: str, level: int = 1) -> None:
    """
    Creates a directory at the specified path and displays the progress of the directory creation.

    Args:
        path (str): The path of the directory to create.
        level (int, optional): The level of indentation in the directory structure. Defaults to 1.

    Returns:
        None
    """
    file_name = path.split("/")
    file_name = file_name[path.count("/")]
    try:
        os.mkdir(path)
        show_progress(path, file_name, level, "INFO")

    except FileExistsError:
        show_error(path, file_name, level, "INFO")

    return None


def create_file(path: str, level: int = 1) -> None:
    """
    Creates a file at the specified path and displays the progress.

    Args:
        path (str): The path of the file to be created.
        level (int, optional): The level of indentation in the directory structure. Defaults to 1.

    Returns:
        None
    """
    file_name = path.split("/")
    file_name = file_name[path.count("/")]
    try:
        with open(path, "x", encoding="utf-8"):
            pass
        show_progress(path, file_name, level, "INFO")

    except FileExistsError:
        show_error(path, file_name, level, "INFO")
    return None


def create_project(dic: dict) -> None:
    """
    Creates a project directory structure based on a dictionary representation.

    Args:
        dic (dict): The dictionary representing the directory structure. Each key in the dictionary corresponds to a directory or file.
                    Directories are prefixed with "d-" and files are prefixed with "f-". The nested structure is represented using nested dictionaries.

    Returns:
        None
    """
    def one_directory(dic: dict, path: str) -> None:
        """
        Recursively creates directories and files based on the dictionary structure.

        Args:
            dic (dict): The dictionary representing the directory structure.
            path (str): The current path in the directory structure.

        Returns:
            None
        """
        for dict_name, info in dic.items():
            file_name = dict_name

            if file_name[:2] == "d-":
                file_name = file_name[2:]

            if file_name[:2] == "f-":
                file_name = file_name[2:]

            next_path = f"{path}/{file_name}"
            level = next_path.count("/")

            if isinstance(info, dict):
                if dict_name[:2] == "d-":
                    create_dir(next_path, level)

                if dict_name[:2] == "f-":
                    create_file(next_path, level)

                one_directory(info, next_path)

    one_directory(dic, ".")
    return None


def open_in_vscode()-> None:
    """
    Opens the project directory in Visual Studio Code.

    This function executes the 'code' command to open the project directory in Visual Studio Code. 
    It uses the value of the 'DIR' variable to determine the directory path.

    Args:
        None

    Returns:
        None
    """
    command_string = f"code {DIR}"
    print(f"Running Command >>> {command_string}")
    os.system(command_string)
    return None


def main() -> None:
    """
    Entry point of the script.
    Prompts the user to create a project directory structure and offers an option to open the project in VS Code.

    Returns:
        None
    """
    create_project(dir_struct)
    invscode = str(
        input(
            Fore.LIGHTCYAN_EX
            + "Would you like to open your project in VS code "
            + Style.RESET_ALL
            + Fore.LIGHTGREEN_EX
            + "YES"
            + Style.RESET_ALL
            + "/"
            + Fore.LIGHTRED_EX
            + "NO"
            + Style.RESET_ALL
            + " >>> "
        )
    )

    if invscode.upper() in {"YES", "Y"}:
        open_in_vscode()

    if invscode.upper() in {"NO", "N"}:
        sys.exit()
        
    return None


if __name__ == "__main__":
    main()
