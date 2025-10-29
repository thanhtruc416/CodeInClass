class Product:
    def __init__(self,id=None,name=None,quantity=None,price=None):
        """
        sự khác biệt init với int
        hàm to string tự động thực hiện khi đối tượng được xuất trên giao diện màn hình
        alias là nhiều biến tham gia quản lý
        garbage collection sẽ thu hồi các ô nhớ không còn các biến quản lý
        """
        self.id=id
        self.name=name
        self.quantity=quantity
        self.price=price
    def __str__(self):
        return f'{self.id}\t{self.name}\t{self.price}'


