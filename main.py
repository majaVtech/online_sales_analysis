from product import Product
from product_manager import ProductManager

pm = ProductManager()
pm.add_product(Product("Laptop", 80000, 5))
pm.add_product(Product("Telefon", 50000, 10))
pm.add_product(Product("Slusalice", 3000, 20))

pm.show_products()
print("Ukupna vrednost inventara:", pm.total_value(), "RSD")