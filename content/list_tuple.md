# 3.List và Tuple
## 3.1 List
LIST là một container được sử dụng rất nhiều trong các chương trình Python.Một List gồm các yếu tố sau:
* Được giới hạn bởi cặp ngoặc [ ], tất cả những gì nằm trong đó là những phần tử của List.
* Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
* List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó!
### Cách khởi tạo List
```
#bình thường
lst = [1,2.0,5,"sinionth"]
#sử dụng comprehension
lst2 = [x for x in range(0,6)]
#sử dụng contrutor
lst = list([1, 2, 3])
```
### Một số toán tử với List 
Giống hệt chuỗi
### Thay đổi nội dung list
```
lst = [1,2.0,5,"sinionth"]
lst[2]="con cua"
'''
[1, 2.0, 'con cua', 'sinionth']
'''
```
### Ma trận
```
mat = [[0,1,2],[3,4,5]]
mat[1]# hàng 1
mat[0][2] #hàng 0 cột 2
```
### Các phương thức 
```
#count(object,start,end) : đếm số lần object xuất hiện trong list
lst.count(2)
#index(i) : tương tự lst[i]
#copy() : copy
lst1 = lst.copy()
#clear() : xóa mọi phần tử
ls1.clear()
#append(object) và extend(iterable) : thêm phần tử vào cuối list
#truyền 1 list vào append thì sẽ coi cả list đấy là 1 phần tử còn extend thì sẽ thêm từng phần tử 
lst2.append(1,4)
lst2.extend(4,5)
#insert(x,i) thêm x vào vị trí i
lst2.insert(5,4)
#pop(i) lấy phần tử thứ i và xóa khỏi list
lst2.pop(3)
#remove(x) xóa x khỏi list
ls1.remove(3)
#sort(key,reverse=bool): sắp xếp list 
```
## 3.2 Tuple
tuple là một container được sử dụng rất nhiều trong các chương trình Python.Một Tuple gồm các yếu tố sau:
* Được giới hạn bởi cặp ngoặc ( ), tất cả những gì nằm trong đó là những phần tử của Tuple.
* Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
* List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó!
### Cách khởi tạo List
```
#bình thường
lst = (1,2.0,5,"sinionth")
#sử dụng contrutor
lst = list((1, 2, 3))
```
### Một số toán tử với Tuple
Giống list
### Thay đổi nội dung Tuple
Về mặt lý thuyết là không thể
### Ma trận
Giống list
### Các phương thức 
Có count và index (giống list)

