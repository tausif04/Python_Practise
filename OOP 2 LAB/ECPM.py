class Product:
    total_products = 0  # Class variable to count the total number of products

    def __init__(self, name, category="General", price=0.0):
        self.name = name
        self.category = category
        self.price = price
        Product.total_products += 1

    @classmethod
    def default_product(cls, name):
        """Constructor with a default category and price."""
        return cls(name, "Uncategorized", 0.0)

    def display(self):
        return f"Product: {self.name}, Category: {self.category}, Price: ${self.price:.2f}"

class InventoryProduct(Product):
    def __init__(self, name, category="General", price=0.0, stock=0):
        super().__init__(name, category, price)
        self.stock = stock

    def restock(self, quantity):
        """Increase stock quantity."""
        self.stock += quantity
        print(f"Restocked {quantity} units of {self.name}. Current stock: {self.stock}")

    def check_low_stock(self, threshold=10):
        """Check if stock is below a certain threshold."""
        return self.stock < threshold

    def adjust_stock(self, quantity):
        """Reduce stock quantity after an order."""
        if quantity > self.stock:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.stock}")
        self.stock -= quantity

    def display(self):
        stock_status = "Low Stock" if self.check_low_stock() else "In Stock"
        return f"{super().display()}, Stock: {self.stock} ({stock_status})"

class CustomerOrder:
    def __init__(self):
        self.cart = []  # List of tuples (product_name, quantity, price_per_unit)

    def add_to_cart(self, product, quantity):
        """Add a product and quantity to the cart."""
        self.cart.append((product.name, quantity, product.price))
        print(f"Added {quantity} units of {product.name} to the cart.")

    def calculate_total(self):
        """Calculate the total bill for the order."""
        return sum(quantity * price for _, quantity, price in self.cart)

    def generate_invoice(self, inventory):
        """Generate a detailed invoice and adjust stock in inventory."""
        print("Generating invoice...")
        for name, quantity, _ in self.cart:
            for product in inventory:
                if product.name == name:
                    product.adjust_stock(quantity)
                    break
        print("Invoice generated and stock updated.")

    def display(self):
        """Display detailed invoice."""
        details = "\n".join([f"{name} - Qty: {quantity}, Unit Price: ${price:.2f}, Total: ${quantity * price:.2f}"
                             for name, quantity, price in self.cart])
        total = self.calculate_total()
        return f"Order Summary:\n{details}\nTotal Bill: ${total:.2f}"

# Example Usage
if __name__ == "__main__":
    # Create inventory products
    product1 = InventoryProduct("Laptop", "Electronics", 999.99, stock=20)
    product2 = InventoryProduct("Headphones", "Electronics", 49.99, stock=50)
    product3 = InventoryProduct.default_product("Notebook")
    product3.price = 2.99
    product3.stock = 200

    inventory = [product1, product2, product3]

    # Display inventory
    print("-- Inventory --")
    for product in inventory:
        print(product.display())

    # Create a customer order
    order = CustomerOrder()
    order.add_to_cart(product1, 2)
    order.add_to_cart(product3, 10)

    # Display order summary
    print("\n-- Order Summary --")
    print(order.display())

    # Generate invoice and update inventory
    order.generate_invoice(inventory)

    # Display updated inventory
    print("\n-- Updated Inventory --")
    for product in inventory:
        print(product.display())
