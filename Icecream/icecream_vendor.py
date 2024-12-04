import csv
import re

ice_cream_menu = {
    'Vanilla': {'Waffle': 200, 'Sugar': 150, 'Cup': 120},
    'Chocolate': {'Waffle': 250, 'Sugar': 200, 'Cup': 180},
    'Strawberry': {'Waffle': 230, 'Sugar': 200, 'Cup': 150}
}


def display_menu():
    print("Ice Cream Menu:")
    with open('icecream_menu.csv', newline='') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            print(' | '.join(row))

# To get Customer name
def getCustomer_name():
    while True:
        name = input("Enter name of Customer: ")
        if re.match(r'^[A-Za-z\s]+$', name):
            return name

        print ("Invalid Input. Please enter valid name")
    

# To get the number of ice creams
def getIcecream_no():
    while True:
        
        number = input("How many ice creams do you want? ")
        if re.match(r'^[1-9][0-9]*$', number):
            number = int (number)
            return number
            
        
        print("Invalid input! Please enter a valid number.")


# To get the type of cone
def getCone_type():

    valid_cones = list(ice_cream_menu['Vanilla'].keys())
    print(valid_cones)

    while True:
        cone = input("Enter type of cone you want (Waffle, Sugar, Cup): ").capitalize()
        if cone in valid_cones:
                return cone
            
        print("Invalid cone type! Please choose from Waffle, Sugar, or Cup.")
        

            

# To get the flavor type
def getFlavour_type():
    valid_flavours = list(ice_cream_menu.keys())
    while True:
        flavour = input("Enter type of flavour you want (Vanilla, Chocolate, Strawberry): ").capitalize()
        if flavour in valid_flavours:
                return flavour
        
        print("Invalid flavour! Please choose from Vanilla, Choclcolate, or Strawberry.")
        

# To get the number of scoops
def getScoop_no():
    while True:
        scoop = input("Enter number of scoops you want: ")
        if re.match(r'^[1-9][0-9]*$', scoop):
            scoop = int (scoop)
            return scoop
        
        print("Please enter a valid number of scoops")
         
# Calculate price
def calculatePrice(flavour, cone, scoop):
    price_per_scoop = ice_cream_menu[flavour][cone]
    total_price = price_per_scoop * scoop
    return total_price

# Print bill in tabular format
def print_bill(name, ice_creams):
    print("\nBill:")
    print(f"{'Customer Name:':<20} {name}")
    print("-" * 55)
    print(f"{'Ice Cream ':<12}{'Flavour':<15}{'Cone Type':<12}{'Scoops':<8}{'Price':<10}")
    print("-" * 55)

    total = 0
    for i, ice_cream in enumerate(ice_creams, 1):
        flavour, cone, scoop, price = ice_cream
        print(f"{i:<12}{flavour:<15}{cone:<12}{scoop:<8}{price:<10}")
        total += price
    
    print("-" * 55)
    print(f"{'Total':<45} Rs{total:}")
    print("-" * 55)

#Main function
def main():
    total_bill= 0
    costumer_name= None
    ice_creams= []


    while True:
        if costumer_name is None:
            costumer_name = getCustomer_name()

        display_menu()
        num_ice_creams = getIcecream_no()

        for i in range(num_ice_creams):
            print(f"\nIce Cream {i + 1}:")
            flavour = getFlavour_type()
            cone = getCone_type()
            scoop_count = getScoop_no()
            price = calculatePrice(flavour, cone, scoop_count)
            ice_creams.append((flavour, cone, scoop_count, price))
            total_bill += price
            print(f"Total price for Ice Cream {i + 1}: Rs{price:}")

        print_bill(costumer_name, ice_creams)  

        continue_choice = input("Would you like to continue (yes/no)? ").lower()
        if continue_choice not in ['yes', 'y']:  
            print("Thank you for your purchase!")
            break

if __name__ == "__main__":
    main()
