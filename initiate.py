"""
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
    """Shows progress of files creation"""
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
    """Shows progress of files creation"""
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
    """_summary_

    Args:
        path (str): _description_
        dirctorys (list[str]): _description_
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
    """_summary_

    Args:
        path (str): _description_
        dirctorys (list[str]): _description_
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
    """creates project according to dictionary passed.

    Args:
        dic : _description_
    """

    def one_directory(dic: dict, path: str) -> None:
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


def open_in_vscode():
    """_summary_"""
    command_string = f"code {DIR}"
    print(f"Running Command >>> {command_string}")
    os.system(command_string)
    # sys.exit()


def main() -> None:
    """_summary_"""
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


if __name__ == "__main__":
    main()
