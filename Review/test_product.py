from Review.product import Product

p1=Product(100,'Thuốc Lào',4,20)
#xuất p1 ra màn hình
print(p1)
p2=Product(200,"Thuốc trị hôi nách",5,30)
p1=p2
print("Yhoong tin p1",p1)
p1.name="Thuốc tăng tự trọng"
print (p2)