
# Vending Machine Program

# Display the welcome message
print("""
█░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀   █▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀
▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█   █░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄
      """)

class VendingMachine:
    def __init__(self):
        # Defining the menu items with codes, prices, and categories
        self.menu = {
            'A1': {'name': 'Cola', 'price': 1.50, 'category': 'Drinks'},
            'A2': {'name': 'Doritos', 'price': 1.00, 'category': 'Snacks'},
            'B1': {'name': 'Coffee', 'price': 2.00, 'category': 'Hot Drinks'},
            'B2': {'name': 'Biscuit', 'price': 1.50, 'category': 'Snacks'},
            'C1': {'name': 'Water', 'price': 1.00, 'category': 'Drinks'},
            'C2': {'name': 'Orange Juice', 'price': 2.00, 'category': 'Drinks'},
            'D1': {'name': 'Wafers', 'price': 4.00, 'category': 'Snacks'},
            'D2': {'name': 'Tea', 'price': 2.00, 'category': 'Hot Drinks'},
            'E1': {'name': 'Apple Juice', 'price': 2.00, 'category': 'Drinks'},
            'E2': {'name': 'Haribo Gummy Bears', 'price': 4.00, 'category': 'Snacks'},
            'F1': {'name': 'Gatorade', 'price': 4.00, 'category': 'Drinks'},
            'F2': {'name': 'Green Tea', 'price': 2.00, 'category': 'Hot Drinks'},
        }

        # Initializing stock levels
        self.stock = {'A1': 5, 'A2': 10, 'B1': 3, 'B2': 15, 'C1': 0, 'C2': 10, 'D1': 5, 'D2': 10, 'E1': 5, 'E2': 10, 'F1': 5, 'F2': 10}

        # Initializing money in the machine
        self.money_in_machine = 0.0
        
    def display_menu(self):
        print("\n===== Vending Machine Menu =====")
        categories = set(item['category'] for item in self.menu.values())

        for category_index, category in enumerate(categories, start=1):
            print(f"{category_index}. {category}")

    def input_category(self):
        while True:
            try:
                selected_category_index = int(input("Enter the number of the category you want to explore, or '0' to stop: "))
                if selected_category_index == 0:
                    return None
                categories = set(item['category'] for item in self.menu.values())
                if 1 <= selected_category_index <= len(categories):
                    return list(categories)[selected_category_index - 1]
                else:
                    print("Invalid category number. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def display_submenu(self, category):
        # Displaying the submenu for the selected category
        print(f"\n===== {category} Menu =====")
        for code, item in self.menu.items():
            if item['category'] == category:
                stock_status = " (Out of Stock)" if self.stock[code] == 0 else ""
                print(f"{code}: {item['name']} – AED{item['price']}{stock_status}")

    def input_code(self):
        # Getting user input for the selected item code
        return input("Enter the code of the item you want to purchase, or '0' to go back to categories: ")

    def accept_money(self):
        # Accepting money from the user
        money_inserted = float(input("Insert money: AED"))
        self.money_in_machine += money_inserted
        return money_inserted

    def calculate_change(self, item_price, money_inserted):
        # Calculating the change to return to the user
        return money_inserted - item_price

    def dispense_item(self, code):
        # Dispensing the selected item and update stock
        if code in self.menu and self.stock[code] > 0:
            item = self.menu[code]
            self.stock[code] -= 1
            print(f"Dispensing {item['name']}...")
            return item
        else:
            print("Sorry, we are currently out of stock or the selected item is invalid.")
            return None

    def display_change(self, change):
        # Displaying the change to the user
        print(f"Change: AED{change:.2f}")

    def suggest_purchase(self, category):
        # Suggesting additional items based on the selected category
        suggestions = [item['name'] for code, item in self.menu.items() if item['category'] == category and self.stock[code] > 0]
        if suggestions:
            print(f"Consider adding {', '.join(suggestions)} to your purchase!")

    def thank_you_message(self):
        print("\nThank you for shopping with us. Have a great day!")

    def run(self):
        # Main execution loop
        while True:
            self.display_menu()
            selected_category = self.input_category()

            if selected_category is None:
                self.thank_you_message()
                break

            if selected_category in set(item['category'] for item in self.menu.values()):
                while True:
                    self.display_submenu(selected_category)
                    code = self.input_code()

                    if code.lower() == '0':
                        break

                    if code in self.menu:
                        item = self.menu[code]
                        item_price = item['price']

                        money_inserted = self.accept_money()

                        if money_inserted >= item_price:
                            change = self.calculate_change(item_price, money_inserted)
                            purchased_item = self.dispense_item(code)
                            if purchased_item:
                                self.display_change(change)

                                # Optional: Implementing a suggestion system based on purchased item category
                                self.suggest_purchase(item['category'])
                        else:
                            print("Insufficient funds. Please insert more money.")
                    else:
                        print("Invalid code. Please enter a valid code from the menu.")
            else:
                print("Invalid category. Please enter a valid category from the menu.")

# Running the vending machine program
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()