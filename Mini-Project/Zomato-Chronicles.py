class FoodOrder:
    def __init__(self):
        self.menu = {
            "1": "Chicken Biryani", "2": "Vegetable Fried Rice", "3": "Butter Naan", "4": "Lassi", 
            "5": "Fruit Salad", "6": "Butter Chicken", "7": "Paneer Masala", "8": "Mixed Vegetable", "9": "Gulab Jamun"
        }
        self.prices = {
            "1": 350, "2": 200, "3": 25, "4": 80, "5": 100, "6": 280, "7": 220, "8": 240, "9": 120
        }
        self.cart = []
            
        
        
    def display_menu(self):
        print("~~~~~~~~~~ ZESTY ZOMATO ~~~~~~~~~~")
        print("------------ MENU ------------")
        for key, value in self.menu.items():
            print(f"{key}. {value:<25}: ₹{self.prices[key]:.2f}")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
                
    def take_order(self):
        while True:
            food_id = input("Please select an item by number (q to quit): ").strip()
            if food_id.lower() == "q":
                break
            elif food_id in self.menu:
                self.cart.append(food_id)
            else:
                print("Invalid selection. Please try again.")

    def display_order(self):
        self.total = 0
        print("------------ YOUR ORDER ------------")
        print(f"{'Item':<25}{'Price':>10}")
        print("-" * 36)
        for food_id in self.cart:
            item_name = self.menu[food_id]
            item_price = self.prices[food_id]
            self.total += item_price
            print(f"{item_name:<25}₹{item_price:>10.2f}")
        print("-" * 36)
        print(f"{'Total':<25}₹{self.total:>10.2f}")
        
    def process_order(self):
        self.display_menu()
        self.take_order()
        self.display_order()
        
if __name__ == "__main__":
    order = FoodOrder()
    order.process_order()



        
        
            
        

        
        