from pathlib import Path
import re


def main():
    while True:
        print(f"1. Add new entry\n2. Show all entries\n3. Clear all entries\n4. Exit")
        status = int(input(f"Enter choice (1-4): "))

        match status:
            case 1:
                print(f"1\n")
                add_new_entry()
                print(f"\n")
            case 2:
                print(f"2\n")
                show_all_entries()
                print(f"\n")
            case 3:
                print(f"3\n")
                clear_entries()
                print(f"\n")
            case 4:
                break
            case _:
                break


#block in which the user enter data for the diary
def add_new_entry():
    date = get_valid_input("Enter date (YYYY-MM-DD): ", r"\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$")
    grade = get_valid_input("Enter grade (0-9): ", r"\d{1}")
    entry = get_valid_input("Enter comment: ", r".*")
    file_path = Path("diary.txt")
    try:
        with file_path.open("a") as diary:
            diary.write(f"{date}|{grade}|{entry}\n")

    except FileNotFoundError:
        with file_path.open("r") as diary:
            diary.write(f"{date}|{grade}|{entry}")

    except PermissionError:
        print("Error: You do not have permission to access this file")

    except Exception as e:
        print(f"Error: {e}")


#block that validates data via regular expression
def get_valid_input(prompt, pattern):
    while True:
        try:
            value = input(prompt)
            if re.fullmatch(pattern, value):
                return value
        except ValueError:
            print("Error: Invalid input. Please enter value again")


#shows all data from a file
def show_all_entries():
    data = []
    file_path = Path("diary.txt")
    try:
        with file_path.open("r") as diary:
            for line in diary:
                date, grade, entry = [x.strip() for x in line.split("|")]

                data.append({
                    "date": date,
                    "grade": grade,
                    "entry": entry
                })
            print(f"========================================\n        All entries\n========================================")
            print(f"+------------+--------+--------------------------------+\n|    Дата    | Оценка |           Текст                |\n+------------+--------+--------------------------------+")
            for member in data:
                print(f" {member["date"]:^12}|{member["grade"]:^8}| {member["entry"]:<32}")
                print(f"+------------+--------+--------------------------------+")

    except FileNotFoundError:
        print("Error: File couldn't be found")

    except PermissionError:
        print("Error: You do not have permission to access this file")

    except Exception as e:
        print(f"Error: {e}")

    input("Press ENTER for continue...")


#clear
def clear_entries():
    match input("You sure? (y/n) "):
        case "y":
            Path("diary.txt").unlink(missing_ok=True)
        case _:
            pass

    input("Press ENTER for continue...")


if __name__ == "__main__":
    main()
    input("Press ENTER for exit...")