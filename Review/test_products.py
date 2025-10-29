from Review.product import Product
from Review.products import ListProduct

lp=ListProduct()
lp.add_product(Product(100,'Product 1',200,10))
lp.add_product(Product(200,'Product 2',10,15))
lp.add_product(Product(300,'Product 3',80,8))
lp.add_product(Product(400,'Product 4',50,20))
lp.add_product(Product(500,'Product 5',150,17))
print("List of Products: ")
lp.print_products()
lp.desc_sort_product()
print("List of Product after descending sort")
lp.print_products()
lp.desc_sort_product_2()
print("List of Product after descending sort 2")
lp.print_products()

