def safe_open_csv():
    """Prompt the user for a CSV file path and return an open file object.

    :returns: Open text-mode file object if successful, None if the user stops.
    """
    while True:
        file_name = input("Enter file location: (type 'Stop' to exit): ")
        if file_name == "Stop":
            print("This code has been stopped.")
            return None
        try:
            if file_name.lower().endswith(".csv"):
                file = open(file_name, "r")
                print("File opened successfully.")
                return file
            else:
                print("Not a correct file type. Only .csv files are supported.")
        except FileNotFoundError:
            print(f"File {file_name} cannot be found.\n")
        except Exception as e:
            print(f"Something went wrong: {e}.\n")


def store_data() -> list[list] | None:
    """Reads an CSV-like file object and return its contents, skipping the first line.
     Prompts the user to open a CSV file using `safe_open_csv()`.
     Each line is split by semi-commas into a list of strings.

    :returns: A list of lists of strings representing
    the CSV rows, or None if an error occurs.
    """
    contents = []
    file_csv = safe_open_csv()
    if file_csv is None:
        return None
    try:
        for i, line in enumerate(file_csv):
            if i == 0:
                continue
            row = line.strip().split(";")
            while len(row) < 7:
                row.append('')
            contents.append(row)
        return contents
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None
    finally:
        file_csv.close()


contents = store_data()

#case 1
def print_number_of_lines(data: list[list]) -> None:
    """Print the total number of lines in the dataset.

    :param data: List of lists containing the CSV data.
    """
    print("Number of lines: " + str(len(data)))


#case 2
def print_lines(data: list[list]) -> None:
    """Print each line of the dataset with descriptive labels.

    :param data: List of lists containing CSV rows.
    """
    for idx, line in enumerate(data, start = 1):
        # line is a list of 7 elements: ID, startdate, datestamp, Nummer, City, Color, word
        print(f"Line {idx}, Started at {line[1]}, Send at {line[2]}, "
              f"Number: {line[3]}, City: {line[4]}, Color: {line[5]}, Word: {line[6]}.")


#case 3
def unique_dates(data: list[list]) -> list:
    """Print and count all unique date values in the dataset.

    :param data: List of lists containing CSV rows.
    :returns: List of unique dates.
    """
    dates = set()
    for row in data:
        if row[2] != '':
            dates.add((row[2][:10]))
    print(f'We have {len(dates)} unique dates.')
    print("Unique dates: " + str(dates))


#case 4
def print_number_stats(data: list[list], index: int):
    """ Convert the values in the specified column to floats and print
    the minimum, maximum, and average of valid numbers.
    Non-numeric entries are ignored.

    :param data: list of lists containing data
    :param index: index of the column to analyze
    """
    numbers = []
    non_numbers = []
    for row in data:
        try:
            # Replacing comma with dot for scientific notation
            value = row[index].replace(',', '.')
            numbers.append(float(value))
        except Exception:
            #non_numbers.append(row[index].replace(',', '.'))
            continue  # ignore non-numeric values
    if numbers:
        minimum = min(numbers)
        maximum = max(numbers)
        average = sum(numbers) / len(numbers)
        print(f"Minimum: {minimum}")
        print(f"Maximum: {maximum}")
        print(f"Average: {average}")
        #print(f'These non-numeric items are ignored: {non_numbers}')
    else:
        print("No valid numbers found in the selected column.")


#case 5 and case 6
def item_count(data: list[list], index) -> dict:
    """Count occurrences of each unique value in the given column.

    :param data: List of lists containing CSV rows.
    :param index: Column index to analyze.
    :returns: Dictionary with items of column index as keys
    and occurrence counts as values.
    """
    item_dict = {}
    for row in data:
        item = row[index].lower()
        if item in item_dict:
            item_dict[item] = item_dict[item] + 1
        else:
            item_dict[item] = 1
    return item_dict


#case 7
def stats_participations(data: list[list], index: int):
    """Count completed and non-completed participants in a given column.

    :param data: List of lists containing CSV rows.
    :param index: Column index to check for empty values.
    """
    participants = 0
    non_participants = 0
    for item in data:
        if item[index] != "":
            participants += 1
        else:
            non_participants += 1
    print(f"There are {participants + non_participants} submissions: "
          f"{participants} complete and {non_participants} incomplete.")


#case 8
def stats_id(data: list[list]):
    """Find missing identifier numbers by comparing expected and actual IDs.

    :param data: List of lists containing CSV rows.
    :returns: List of missing identifiers.
    """
    reference = list(range(1, len(data)+1))
    actuals = [int(row[0]) for row in data]
    result = list(set(reference) - set(actuals))
    print(f"We have {len(result)} inconsistent IDs.")
    print(f"Inconsistent (missing) IDs: {result}")
    return result


#case 9
def stats_qwords(data: list[list]):
    """Analyze and count words containing the letter 'q'.
    Prints separate counts for words starting with 'q',
    containing 'q', and without 'q'.

    :param data: List of lists containing CSV rows.
    """
    q_words = 0
    q_start_words = 0
    no_q_words = 0
    for row in data:
        if row[6] != "":
            word = row[6].lower()
            if word[0] == 'q':
                q_start_words += 1
            elif 'q' in word :
                q_words += 1
            else :
                no_q_words += 1
    print(f'{q_start_words} words start with q')
    print(f'{q_words} words contain q, but not as first letter')
    print(f'{no_q_words} words do not contain q')


#case 10
def save_q_words(filename, data: list[list]):
    """Save all words starting with 'q' to a new file.
    Only rows with valid numbers and dates are included.

    :param filename: Path of the file to save the data.
    :param data: List of lists containing CSV rows.
    """
    try:
        file = open(filename, 'w')
        for row in data:
            if row[6] != "" and row[3] != "":
                word = row[6].lower()
                if word[0] == 'q' and row[3] != '':
                    new_list = [row[0], row[3], row[5], row[6]]
                    file.write(";".join(new_list) + '\n')
    except Exception as e:
        print(e)
    print("File saved.")


def menu(contents: list[list]):
    """Offer the user 10 options to analyze and process the CSV data."""

    while True:
        print("\nChoose an option by typing a number or Stop:\n")
        print("1)\t Print the number of lines")
        print("2)\t Print the content")
        print("3)\t Print unique dates")
        print("4)\t Print number statistics")
        print("5)\t Print color statistics")
        print("6)\t Print city names")
        print("7)\t Print participation statistics")
        print("8)\t Print ID statistics")
        print("9)\t Print Q-word statistics")
        print("10)\t Save selected data")
        print("Stop)\t Program stops")

        keuze = input("\nYour choice: ").strip()

        match keuze:
            case "Stop":
                print("Program has stopped.")
                break
            case "1":  # Print het aantal lijnen
                print_number_of_lines(contents)
            case "2":  # Print inhoud van elke lijn
                print_lines(contents)
            case "3":
                # Print unieke datums
                unique_dates(contents)
            case "4":
                # Print getal statistieken
                print_number_stats(contents, 3)
            case "5":
                # Print kleur statistieken
                color_dict = item_count(contents, 5)
                for key, value in color_dict.items():
                    if key != '':
                        print(f'{key} is found {value} times')
            case "6":
                # Print unieke plaatsnamen
                city_dict = item_count(contents, 4)
                for key in city_dict:
                    if key != '':
                        print(key)
            case "7":
                # Print deelname statistieken
                stats_participations(contents, 2)
            case "8":
                # print ontbrekende id waarden
                stats_id(contents)
            case "9":
                # Print stats over q-woorden
                stats_qwords(contents)
            case "10":
                # Saves valid values in given file
                filename = input("Enter a file location to save the data: ").strip()
                save_q_words(filename, contents)
            case _:
                print("Invalid choice, try again.")

menu(contents)