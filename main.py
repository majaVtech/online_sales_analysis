from product import Product
from product_manager import ProductManager
from cart import Cart

pm = ProductManager()
pm.add_product(Product("Laptop", 80000, 5))
pm.add_product(Product("Telefon", 50000, 10))
pm.add_product(Product("Slusalice", 3000, 20))

cart = Cart()
cart.add_to_cart(pm.products[0])
cart.add_to_cart(pm.products[1])
cart.add_to_cart(pm.products[2])

cart.show_cart()
print("Ukupna vrijednost korpe:", cart.total_cart_value(), "RSD")