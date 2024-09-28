import qrcode
from PIL import Image

class CafeManagementSystem:
    def __init__(self):
        self.menu = {
            "Coffee": 3.00,
            "Tea": 2.50,
            "Sandwich": 5.00,
            "Salad": 4.00,
            "Cake": 3.50
        }
        self.orders = {}
        self.table_qr_codes = {i: f"QR_{i}" for i in range(1, 11)}  # Simulating 10 tables with unique QR codes
        self.generate_qr_codes()

    def generate_qr_codes(self):
        for table, qr_code in self.table_qr_codes.items():
            img = qrcode.make(qr_code)
            img.save(f"table_{table}.png")
            print(f"Generated QR code for Table {table}: {qr_code} (saved as table_{table}.png)")

    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ₹{price:.2f}")

    def take_order(self, table_number):
        print(f"\nTable {table_number} Order")
        while True:
            self.display_menu()
            order_item = input("Enter the item you want to order (or type 'done' to finish): ")
            if order_item.lower() == 'done':
                break
            elif order_item in self.menu:
                quantity = int(input(f"Enter the quantity for {order_item}: "))
                if table_number not in self.orders:
                    self.orders[table_number] = []
                self.orders[table_number].append((order_item, quantity))
            else:
                print("Item not found in the menu. Please try again.")

    def generate_bill(self, table_number):
        if table_number not in self.orders:
            print(f"No orders found for Table {table_number}")
            return
        print(f"\nBill for Table {table_number}:")
        total_cost = 0
        for item, quantity in self.orders[table_number]:
            item_cost = self.menu[item] * quantity
            total_cost += item_cost
            print(f"{item} (x{quantity}): ₹{item_cost:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    def start(self):
        print("Available QR Codes for Tables (images saved as table_<number>.png):")
        for table, qr in self.table_qr_codes.items():
            print(f"Table {table}: {qr}")

        while True:
            qr_code = input("\nEnter your table's QR code (or type 'exit' to quit): ")
            if qr_code.lower() == 'exit':
                break

            # Find the table number based on the entered QR code
            table_number = None
            for table, qr in self.table_qr_codes.items():
                if qr == qr_code:
                    table_number = table
                    break

            if table_number is not None:
                self.take_order(table_number)
                self.generate_bill(table_number)
            else:
                print("Invalid QR code. Please try again.")

# Start the cafe management system
cafe = CafeManagementSystem()
cafe.start()
