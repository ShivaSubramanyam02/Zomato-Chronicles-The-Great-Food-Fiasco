import pickle

class ZestyZomato:
    def __init__(self):
        self.menu = {}
        self.orders = {}
        self.order_id_counter = 1
        self.coupons = {"SAVE10": 10, "SAVE20": 20}
        self.load_data()

    def save_data(self):
        with open("zomato_data.pkl", "wb") as f:
            pickle.dump((self.menu, self.orders, self.order_id_counter), f)

    def load_data(self):
        try:
            with open("zomato_data.pkl", "rb") as f:
                self.menu, self.orders, self.order_id_counter = pickle.load(f)
        except FileNotFoundError:
            pass

    def add_dish(self, dish_id, name, price, available):
        self.menu[dish_id] = {"name": name, "price": price, "available": available}
        self.save_data()
        print(f"Dish '{name}' added successfully!")
    
    def remove_dish(self, dish_id):
        if dish_id in self.menu:
            del self.menu[dish_id]
            self.save_data()
            print("Dish removed successfully!")
        else:
            print("Dish not found!")
    
    def update_availability(self, dish_id, available):
        if dish_id in self.menu:
            self.menu[dish_id]["available"] = available
            self.save_data()
            print("Availability updated!")
        else:
            print("Dish not found!")
    
    def view_menu(self):
        print("\n--- Menu ---")
        for dish_id, dish in self.menu.items():
            status = "Available" if dish["available"] else "Not Available"
            print(f"{dish_id}: {dish['name']} - {dish['price']} - {status}")
    
    def take_order(self, customer_name, dish_ids, coupon_code=None):
        total_price = 0
        ordered_dishes = {}
        for dish_id in dish_ids:
            if dish_id in self.menu and self.menu[dish_id]["available"]:
                ordered_dishes[dish_id] = self.menu[dish_id]
                total_price += self.menu[dish_id]["price"]
            else:
                print(f"Dish {dish_id} is not available!")
                return
        
        discount = self.coupons.get(coupon_code, 0) if coupon_code else 0
        final_price = total_price - (total_price * discount / 100)
        
        order_id = str(self.order_id_counter)
        self.orders[order_id] = {"customer": customer_name, "dishes": ordered_dishes, "status": "received", "total_price": total_price, "discount": discount, "final_price": final_price}
        self.order_id_counter += 1
        self.save_data()
        print(f"Order {order_id} placed successfully! Final Price: {final_price}")
    
    def update_order_status(self, order_id, status):
        if order_id in self.orders:
            self.orders[order_id]["status"] = status
            self.save_data()
            print("Order status updated!")
        else:
            print("Order not found!")
    
    def view_orders(self, status_filter=None):
        print("\n--- Order List ---")
        for order_id, order in self.orders.items():
            if status_filter is None or order["status"] == status_filter:
                print(f"Order ID: {order_id} | Customer: {order['customer']} | Status: {order['status']} | Total: {order['total_price']} | Discount: {order['discount']}% | Final: {order['final_price']}")
    
    def generate_invoice(self, order_id):
        if order_id in self.orders:
            order = self.orders[order_id]
            print("\n--- Invoice ---")
            print(f"Order ID: {order_id}")
            print(f"Customer: {order['customer']}")
            print("Dishes:")
            for dish in order["dishes"].values():
                print(f"- {dish['name']} - {dish['price']}")
            print(f"Total Price: {order['total_price']}")
            print(f"Discount: {order['discount']}%")
            print(f"Final Price: {order['final_price']}")
        else:
            print("Order not found!")
    
    def exit_system(self):
        print("Exiting system. Have a great day!")
        exit()

zomato = ZestyZomato()
while True:
    print("\n🍽️ Welcome to Zesty Zomato! 🍽️")
    print("---------------------------------")
    print("1️⃣ Add Dish")
    print("2️⃣ Remove Dish")
    print("3️⃣ Update Availability")
    print("4️⃣ View Menu")
    print("5️⃣ Take Order")
    print("6️⃣ Update Order Status")
    print("7️⃣ View Orders")
    print("8️⃣ Generate Invoice")
    print("9️⃣ Exit")
    print("---------------------------------")
    
    choice = input("🚀 Enter your choice: ")
    if choice == "1":
        dish_id = input("🏷️ Enter Dish ID: ")
        name = input("🍛 Enter Dish Name: ")
        price = float(input("💰 Enter Price: "))
        available = input("✔️ Available (yes/no): ").lower() == "yes"
        zomato.add_dish(dish_id, name, price, available)
    elif choice == "2":
        dish_id = input("🏷️ Enter Dish ID: ")
        zomato.remove_dish(dish_id)
    elif choice == "3":
        dish_id = input("🏷️ Enter Dish ID: ")
        available = input("✔️ Available (yes/no): ").lower() == "yes"
        zomato.update_availability(dish_id, available)
    elif choice == "4":
        zomato.view_menu()
    elif choice == "5":
        customer_name = input("👤 Enter Customer Name: ")
        dish_ids = input("🍛 Enter Dish IDs (comma separated): ").split(",")
        coupon_code = input("🎟️ Enter Coupon Code (if any): ")
        zomato.take_order(customer_name, dish_ids, coupon_code)
    elif choice == "6":
        order_id = input("🆔 Enter Order ID: ")
        status = input("🔄 Enter New Status: ")
        zomato.update_order_status(order_id, status)
    elif choice == "7":
        status_filter = input("🔍 Enter Status to Filter (leave empty for all): ")
        status_filter = status_filter if status_filter else None
        zomato.view_orders(status_filter)
    elif choice == "8":
        order_id = input("🆔 Enter Order ID: ")
        zomato.generate_invoice(order_id)
    elif choice == "9":
        zomato.exit_system()
    else:
        print("⚠️ Invalid choice! Try again.")
