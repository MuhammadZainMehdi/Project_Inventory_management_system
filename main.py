class Inventory:
    inventory = {
        "hp001": {
            "name": "Hp Elitebook",
            "category": "laptop",
            "price": 1000,
            "quantity": 50
        },
        "dell101": {
            "name": "Dell XPS 13",
            "category": "laptop",
            "price": 1300,
            "quantity": 6
        },
        "apple201": {
            "name": "iPhone 15",
            "category": "smartphone",
            "price": 999,
            "quantity": 50
    },
        "sony301": {
            "name": "Sony WH-1000XM5",
            "category": "headphones",
            "price": 350,
            "quantity": 30
        },
        "sony302": {
            "name": "Sony PlayStation 5",
            "category": "gaming console",
            "price": 500,
            "quantity": 80
        }
    }
    @staticmethod
    def track_stocklevels():
        for product in Inventory.inventory:
            if Inventory.inventory[product]["quantity"] < 10:
                print(f"\033[1mInventory Alert: Low Stock Level for {product}\033[0m")

#----------Product Class----------
class Product:
    #----------Product Class Constructor----------
    def __init__(self, id, name, category, price, stock):
        self.product_id = id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock

#----------Admin Class----------
class Admin:
    #----------Class Variables----------
    __credentials = ["admin1", 1234]
    authentication = False

    #----------Admin Class Constructor----------
    def __init__(self, uname, password):
        self.username = uname
        self.password = password

        if self.username == Admin.__credentials[0] and self.password == Admin.__credentials[1]:
            Admin.authentication = True
            print("Login Successfull✅")
            Inventory.track_stocklevels()
        else:
            Admin.authentication = False
            print("Invalid Credentials!❌")
            return

    #----------Class Method to add products----------
    def add_products(self, Id, Name, Category, Price, Quantity):
        if Admin.authentication:
            product = Product(Id, Name, Category, Price, Quantity)
            Inventory.inventory[product.product_id] = {
                "name": product.name,
                "category": product.category,
                "price": product.price,
                "quantity": product.stock_quantity
            }
            print(f"Product {product.name}, Id {id} added to Inventory.")
        else:
            print("Access denied!")

    #----------Class Method to edit products----------
    def edit_products(self, Id):
        if Admin.authentication:
            if Id in Inventory.inventory:
                edit_choice = input("What you want to edit: ").lower()
                if edit_choice in Inventory.inventory[Id]:
                    if edit_choice == "price" or edit_choice == "quantity":
                        try:
                            old_value = Inventory.inventory[Id][edit_choice]
                            new_value = int(input("Input new value: "))
                            Inventory.inventory[Id][edit_choice] = new_value
                            print(f"Product Id {Id} {edit_choice}'s changed from {old_value} to {new_value}.")
                            Inventory.track_stocklevels()
                        except ValueError:
                            print("Invalid input. Price and quantity should be numeric values.")
                    else:
                        old_value = Inventory.inventory[Id][edit_choice]
                        new_value = int(input("Input new value: "))
                        Inventory.inventory[Id][edit_choice] = new_value
                        print(f"Product Id {Id} {edit_choice}'s changed from {old_value} to {new_value}.")
                else:
                    print("Invalid Choice!")
            else:
                print(f"No product found for Id {Id}")
        else:
            print("Access denied!")
                

    #----------Class Method to delete products----------
    def delete_products(self, Id):
        if Admin.authentication:
            if Id in Inventory.inventory:
                del_product = Inventory.inventory[Id]["name"]
                del Inventory.inventory[Id]
                print(f"Product {del_product}, Id {Id} deleted from Inventory.")
            else:
                print(f"No product found for Id {Id}")
        else:
            print("Access denied")

#----------User Class----------
class User:
    #----------Class Variables----------
    __credentials = ["user1", 1230]
    authentication = False

    #----------User Class Constructor----------
    def __init__(self, uname, password):
        self.username = uname
        self.password = password

        if self.username == User.__credentials[0] and self.password == User.__credentials[1]:
            User.authentication = True
            print("Login Successfull✅")
        else:
            User.authentication = False
            print("Invalid Credentials!❌")
            return

    #----------Class Method to view products----------
    def view_products(self):
        if User.authentication:
            if not Inventory.inventory:
                print("Inventory is Empty.")
            else:
                print("----------Products List----------")
                for item in Inventory.inventory:
                    print(f"Product: {Inventory.inventory[item]["name"]}, Price: ${Inventory.inventory[item]["price"]}, Stock available: {Inventory.inventory[item]["quantity"]}")
                print("-" * 30)
        else:
            print("Access denied")

    #----------Class Method to search products----------
    def search_product(self):
        search = input("Search by category: ")
        product_found = False

        for item in Inventory.inventory:
            if search == Inventory.inventory[item]["category"]:
                if not product_found:
                    print("These are the products that match your search:")
                print(f"Product: {Inventory.inventory[item]["name"]}, Price: ${Inventory.inventory[item]["price"]} Stock available: {Inventory.inventory[item]["quantity"]}")
                product_found = True
                
        if not product_found: 
            print("No products were found matching your search.")
            print("Browse through our available products: ")
            self.view_products()

    #----------Class Method to buy products----------
    def buy_products(self):
        if User.authentication:
            self.search_product()
            product_name = input("Which Product you want to buy: ")
            product_quantity = int(input("Enter quantity to buy: "))

            found = False
            required = False
            for item in Inventory.inventory:
                if product_name == Inventory.inventory[item]["name"]:
                    if product_quantity < Inventory.inventory[item]["quantity"]:
                        Inventory.inventory[item]["quantity"] -= product_quantity
                        found = True
                    else:
                        print("Required quantity is not available.")
                        required = True
                        return
                    print(f"Product {product_name}, quantity {product_quantity} added to Cart.")
                    print(f"Bill = ${Inventory.inventory[item]["price"] * product_quantity}")
                    break
            if found == False and required == False:
                print(f"{product_name} is out of stock.")
        else:
            print("Access denied")

#----------Main----------
while True:
    role = (input("Login as (Admin/User): ")).lower()
    if role != "":
        if role == "admin":
            username = input("Username: ")
            try:
                password = int(input("Password: "))
                admin = Admin(username, password)

                if Admin.authentication:
                    while True:
                        choice = input("1. Add\n2. Edit\n3. Delete\n4. Exit\nSelect an option: ")
                        if choice == "1":
                            id = input("Enter Product id: ")
                            name = input("Enter Product name: ")
                            category = input("Enter Product category: ")    
                            price = int(input("Enter Product price: "))
                            quantity = int(input("Enter Product stock quantity: "))
                            admin.add_products(id, name, category, price, quantity)
                        elif choice == "2":
                            edit_item = input("Enter Product Id to edit: ")
                            admin.edit_products(edit_item)
                        elif choice ==  "3":
                            del_item = input("Enter Product Id to delete: ")
                            admin.delete_products(del_item)
                        elif choice == "4":
                            break
                        else:
                            print("Invalid Choice")
                            break
            except ValueError:
                print("Invalid input in password.")

        elif role == "user":
            username = input("Username: ")
            try:
                password = int(input("Password: "))
                user = User(username, password)

                if User.authentication:
                    user.buy_products()
            except ValueError:
                print("Invalid input in password.")

        else:
            print("Role not defined!")
    else:
        break