import csv
import os
import pandas as pd


class CSV_Saver:
    #headers = ["Id", "Name", "Age"]
    #test
    # Initializing with filename and headers
    def __init__(self, file_name=None):
        if file_name is None:
            file_name = f"{self.__class__.__name__}.csv"
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
            pd.DataFrame(columns=self.headers).to_csv(self.file_name, index=False)
            print(f"Header written to {self.file_name}")
    
    #get header from existing file
    def get_headers_from_file(self):
        
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0:
            df = pd.read_csv (self.file_name)
            return df.columns.tolist()
        return None

    # Making CSV file
    def make_csv_file(self):
        if not os.path.exists(self.file_name):
            pd.DataFrame(columns=self.headers).to_csv(self.file_name, index=False)
            print(f"{self.file_name} created with headers: {self.headers}")
        else:
            print(f"{self.file_name} already exists.")

    # Writing rows
    def write_rows(self, data):
        file_exists = os.path.exists(self.file_name)
        df = pd.DataFrame (data, columns=self.headers)
        df.to_csv(self.file_name, mode = 'a', header = not file_exists, index = False)
        print(f"{data} written to {self.file_name}")

    # Writing all rows (after modification)
    def write_data(self, rows):
        df = pd.DataFrame (rows, columns=self.headers)
        df.to_csv (self.file_name, index=False)
        print(f"Data written to {self.file_name}")

    # Reading data
    def read_data(self):
        if os.path.exists(self.file_name):
            df = pd.read_csv (self.file_name)
            return df
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
        df = self.read_data()
      
        if row_index < len(df):
            column_name = self.headers[column_index]
            old_value = df.at[row_index, column_name]
            df.at[row_index, column_name] = new_value
            self.write_data(df)
            print(f"Updated value in row {row_index}, column {column_name} from {old_value} to {new_value}")
        else:
            print(f"Row index {row_index} is out of range")

    # Updating entire row using classmethod
    @classmethod
    def update_entire_row(cls, row_index, new_row_data, file_name):
        instance = cls(file_name=file_name)
        df = instance.read_data()
        if row_index < len(df):
            if len(new_row_data) == len(instance.headers):
                old_row = df.iloc [row_index].tolist()
                df.iloc[row_index] = new_row_data
                print(f"Updated row {row_index} from {old_row} to {new_row_data}")
                instance.write_data(df)
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

    @staticmethod
    def validate_row_data(headers, row_data):
        if len(headers) != len(row_data):
            raise ValueError(f"Expected {len(headers)} values, got {len(row_data)}.")
        return [item.strip() for item in row_data]
    
    def add_new_header(self, new_header):
        if new_header in self.headers:
            print("The header already exists")
            return

        df = self.read_data()
        df[new_header] = ""
        self.headers.append(new_header) 
        self.write_data(df)
        print("Added new header")

    def update_new_header_values(self, header_name):
        if header_name not in self.headers:
            print("The header does not exist")
            return

        df = self.read_data()
        df[header_name] = df[header_name].astype(str)
        for row_index in range(len(df)):
            new_value = input(f"Enter new value for row {row_index}, column '{header_name}': ").strip()
            df.at[row_index, header_name] = new_value

        self.write_data(df)
        print(f"Updated values for the header '{header_name}'.")


class Child_Class(CSV_Saver):
    # Deleting specific row
    def delete_row(self, row_index):
        df = self.read_data()
        if 0 <= row_index < len(df):
            deleted_row = df.iloc [row_index]
            df = df.drop (row_index)
            df = df.reset_index(drop=True)
            self.write_data(df)
            print(f"Row deleted: {deleted_row}")
        else:
            print(f"Row index {row_index} is out of range.")

    # Add new row
    def add_new_row(self, new_row_data):
        new_row_data = self.validate_row_data(self.headers, new_row_data)
        df = self.read_data()
        df.loc[len(df)] = new_row_data
        self.write_data(df)
        print(f"New row added: {new_row_data}")


class MyFile(Child_Class):
    """test"""


def main():
    my_data = MyFile()
    my_data.make_csv_file()
    rows = my_data.collect_data_from_user()
    if rows:
        my_data.write_rows(rows)

    def update_attribute():
        row_index = int(input("Enter the row index to update: "))
        column_index = int(input("Enter the column index to update: "))
        new_value = input("Enter the new value: ")
        my_data.update_attribute_in_row(row_index, column_index, new_value)

    def update_entire_row():
        row_index = int(input("Enter the row index to update (entire row): "))
        new_row_data = input("Enter the new row data (comma-separated): ").split(",")
        new_row_data = [item.strip() for item in new_row_data]
        Child_Class.update_entire_row(row_index, new_row_data, my_data.file_name)

    def add_new_row():
        new_row = input("Enter new row data (comma-separated): ").split(",")
        new_row = [item.strip() for item in new_row]
        my_data.add_new_row(new_row)

    def delete_row():
        delete_index = int(input("Enter the row index to delete: "))
        my_data.delete_row(delete_index)

    def delete_file():
        my_data.delete_file()

    def add_new_header():
        new_header = input("Enter the name of the new header to add: ").strip()
        my_data.add_new_header(new_header)

    def update_new_header_values():
        header_name = input("Enter the name of the header to update its values: ").strip()
        my_data.update_new_header_values(header_name)

    def exit_program():
        print("Exiting the program")
        exit()

    

    operations = {
        "1": update_attribute,
        "2": update_entire_row,
        "3": add_new_row,
        "4": delete_row,
        "5": delete_file,
        "6": exit_program,
        "7": add_new_header,
        "8": update_new_header_values
    }

    while True:
        print("Select an operation:")
        print("1.Update specific attribute")
        print("2.Update entire row")
        print("3.Add new row")
        print("4.Delete specific row")
        print("5.Delete entire file")
        print("6.Exit program")
        print("7.Add new header")
        print("8.Update values for a new header")

        choice = input("Enter your choice (1-8): ").strip()
        operations.get(choice, lambda: print("Invalid choice. Please try again."))()

        # Print data after each operation
        data_after_operation = my_data.read_data()
        print("Updated CSV data:")
        print(data_after_operation)




if __name__ == "__main__":
    main()
