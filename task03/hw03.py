import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(directory: Path, indent: str = ""):
    try:
        entries = sorted(directory.iterdir(), key=lambda x: (not x.is_dir(), x.name.lower()))
    except PermissionError:
        print(f"{indent}{Fore.RED}[Доступ заборонено]")
        return
    
    for entry in entries:
        if entry.is_dir():
            print(f"{indent}{Fore.BLUE}{entry.name}/")
            print_directory_structure(entry, indent + "   ")
        else:
            print(f"{indent}{Fore.GREEN}{entry.name}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: Вкажіть шлях о директорії як аргумент.")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Помилка: Шлях '{path} не існує.")
        sys.exit(1) 

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: Шлях '{path}' не є директорією")
        sys.exit(1)

    print(f"{Fore.BLUE}{path.resolve().name}/")
    print_directory_structure(path, indent="    ")

if __name__=="__main__":
    main()