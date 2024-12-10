import csv
import os


class CSV_Saver:
    #headers = ["Id", "Name", "Age"]
    #test
    # Initializing with filename and headers
    def __init__(self, file_name=None):
        if file_name is None:
            file_name = f"{__class__.__name__}.csv"
        self.file_name = file_name
        self.headers = self.get_headers_from_file()

        if not self.headers:
            while True:
                user_input = input("Enter column headers like this (Name, Age, Address): ").strip()
                headers = [header.strip() for header in user_input.split(",") if header.strip()]
                if headers:
                    self.headers = headers
                    break
                else:
                    print("Invalid headers! Please enter a non-empty list of column names.")
            self.write_header()

    # Write header if new csv file
    def write_header(self):
        if not os.path.exists(self.file_name) or os.path.getsize(self.file_name) == 0:
            with open(self.file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
            print(f"Header written to {self.file_name}")
    
    #get header from existing file
    def get_headers_from_file(self):
        
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0:
            with open(self.file_name, mode='r') as file:
                reader = csv.reader(file)
                headers = next(reader, None)
                return headers
        return None

    # Making CSV file
    def make_csv_file(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)
            print(f"{self.file_name} created with headers: {self.headers}")
        else:
            print(f"{self.file_name} already exists.")

    # Writing rows
    def write_rows(self, data):
        file_exists = os.path.exists(self.file_name)
        write_header = not file_exists or os.path.getsize(self.file_name) == 0
        with open(self.file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            if write_header:
                writer.writerow(self.headers)
            writer.writerows(data)
        print(f"{data} written to {self.file_name}")

    # Writing all rows (after modification)
    def write_data(self, rows):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Data written to {self.file_name}")

    # Reading data
    def read_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, mode='r') as file:
                reader = csv.reader(file)
                return list(reader)
        else:
            print(f"{self.file_name} not found")
            return []

    # Data input from user
    def collect_data_from_user(self):
        rows = []
        while True:
            row_input = input("Enter a row of data (e.g., 1, Ram, 24) or type 'done' to finish: ")

            if row_input.lower() == 'done':
                break

            row_data = row_input.split(",")
            row_data = [item.strip() for item in row_data]

            if len(row_data) != len(self.headers):
                print(f"Please provide exactly {len(self.headers)} values.")
                continue

            rows.append(row_data)
        return rows

    # Updating specific attribute in row
    def update_attribute_in_row(self, row_index, column_index, new_value):
        rows = self.read_data()
        if 1 <= row_index < len(rows):  # Header row at index 0
            if 0 <= column_index < len(self.headers):
                old_value = rows[row_index][column_index]
                rows[row_index][column_index] = new_value
                print(f"Updated value in row {row_index}, column {column_index} from {old_value} to {new_value}")
                self.write_data(rows)
            else:
                print(f"Column index {column_index} is out of range")
        else:
            print(f"Row index {row_index} is out of range")

    # Updating entire row using classmethod
    @classmethod
    def update_entire_row(cls, row_index, new_row_data, file_name):
        instance = cls(file_name=file_name)
        rows = instance.read_data()
        if 1 <= row_index < len(rows):
            if len(new_row_data) == len(instance.headers):
                old_row = rows[row_index]
                rows[row_index] = new_row_data
                print(f"Updated row {row_index} from {old_row} to {new_row_data}")
                instance.write_data(rows)
            else:
                print("New row data doesn't match the number of columns")
        else:
            print(f"Row index {row_index} is out of range")

    # Deleting file
    def delete_file(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
            print(f"{self.file_name} deleted")
        else:
            print(f"{self.file_name} does not exist")

    # Validate row data
    @staticmethod
    def validate_row_data(headers, row_data):
        if len(headers) != len(row_data):
            raise ValueError(f"Expected {len(headers)} values, got {len(row_data)}.")
        return [item.strip() for item in row_data]


class Child_Class(CSV_Saver):
    # Deleting specific row
    def delete_row(self, row_index):
        rows = self.read_data()
        if 1 <= row_index < len(rows):  # Header row at index 0
            deleted_row = rows.pop(row_index)
            print(f"Row deleted: {deleted_row}")
            self.write_data(rows)
        else:
            print(f"Row index {row_index} is out of range.")

    # Add new row
    def add_new_row(self, new_row_data):
        new_row_data = self.validate_row_data(self.headers, new_row_data)
        self.write_rows([new_row_data])
        print(f"New row added: {new_row_data}")


def main():
    file_name = f"{CSV_Saver.__name__}.csv"
    my_data = Child_Class()
    my_data.make_csv_file()
    my_data.write_header()

    # Collect and write rows
    rows = my_data.collect_data_from_user()
    my_data.write_rows(rows)

    while True:
        print("Select an operation:")
        print("1.Update specific attribute")
        print("2.Update entire row")
        print("3.Add new row")
        print("4.Delete specific row")
        print("5.Delete entire file")
        print("6.Exit program")

        choice = input("Enter your choice 1-6: ").strip()

        if choice == "1":
            # Update specific attribute
            row_index = int(input("Enter the row index to update: "))
            column_index = int(input("Enter the column index to update: "))
            new_value = input("Enter the new value: ")
            my_data.update_attribute_in_row(row_index, column_index, new_value)

        elif choice == "2":
            # Update entire row
            row_index = int(input("Enter the row index to update (entire row): "))
            new_row_data = input("Enter the new row data (comma-separated): ").split(",")
            new_row_data = [item.strip() for item in new_row_data]
            Child_Class.update_entire_row(row_index, new_row_data, my_data.file_name)

        elif choice == "3":
            # Add new row
            new_row = input("Enter new row data (comma-separated): ").split(",")
            new_row = [item.strip() for item in new_row]
            my_data.add_new_row(new_row)

        elif choice == "4":
            # Delete specific row
            delete_index = int(input("Enter the row index to delete: "))
            my_data.delete_row(delete_index)

        elif choice == "5":
            # Delete entire file
            my_data.delete_file()

        elif choice == "6":
            print("Exiting the program")
            break

        else:
            print("Invalid choice. Please try again.")

        # Print data after each operation
        data_after_operation = my_data.read_data()
        print("Updated CSV data:", data_after_operation)


if __name__ == "__main__":
    main()
