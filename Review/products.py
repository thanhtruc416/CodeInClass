class ListProduct:
    def __init__(self):
        self.products =[]
    def add_product(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)
    def desc_sort_product(self):
        for i in range (0,(len(self.products))):
            for j in range (i+1,(len(self.products))):
                pi=self.products[i]
                pj = self.products[j]
                if pi.price < pj.price:
                    self.products[j]=pi
                    self.products[i]=pj

# Merge Sort (giảm dần theo price)
    def desc_sort_product_2(self, arr=None):
            if arr is None:  # lần đầu gọi thì sort self.products
                arr = self.products

            if len(arr) > 1:
                mid = len(arr) // 2
                left = arr[:mid]
                right = arr[mid:]

                # Đệ quy sắp xếp 2 nửa
                self.desc_sort_product_2(left)
                self.desc_sort_product_2(right)

                i = j = k = 0

                # Trộn 2 nửa lại
                while i < len(left) and j < len(right):
                    if left[i].price >= right[j].price:  # so sánh giảm dần
                        arr[k] = left[i]
                        i += 1
                    else:
                        arr[k] = right[j]
                        j += 1
                    k += 1

                # Copy phần còn lại
                while i < len(left):
                    arr[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    arr[k] = right[j]
                    j += 1
                    k += 1

            # Nếu đang sort list chính thì cập nhật lại
            if arr is self.products:
                self.products = arr

