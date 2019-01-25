# 3.List và Tuple
## 3.1 List
LIST là một container được sử dụng rất nhiều trong các chương trình Python.Một List gồm các yếu tố sau:
* List trong Python là thay đổi (mutable), nghĩa là Python sẽ không tạo một List mới nếu bạn sửa đổi một phần tử trong List.
* Được giới hạn bởi cặp ngoặc [ ], tất cả những gì nằm trong đó là những phần tử của List.
* Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
* List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó!

chú ý :List không lưu trữ các phần tử một cách trực tiếp tại chỉ mục. Sự thực là một tham chiếu được lưu trữ tại mỗi chỉ mục 
mà tham chiếu tới đối tượng được lưu trữ ở đâu đó trong bộ nhớ. Điều này là do một số đối tượng có thể lớn hơn một số đối tượng 
khác và vì thế chúng được lưu trữ tại một vị trí bộ nhớ khác.
### Cách khởi tạo List
```
#bình thường
lst = [1,2.0,5,"sinionth"]
#sử dụng comprehension
lst2 = [x for x in range(0,6)]
#sử dụng contrutor list(iterable)
lst = list((1, 2, 3))
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
### Một số phương thức 

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
*sử dụng `help(List)` để biết chi tiết
## 3.2 Tuple
tuple là một container được sử dụng rất nhiều trong các chương trình Python.Một Tuple gồm các yếu tố sau:
* Một tuple là một dãy các đối tượng không thay đổi (immutable) trong Python, vì thế tuple không thể bị thay đổi. 
* Được giới hạn bởi cặp ngoặc ( ), tất cả những gì nằm trong đó là những phần tử của Tuple.
* Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
* Tuple có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó!

Chú ý : Bất kỳ tập hợp nào gồm nhiều đối tượng, được phân biệt bởi dấu phảy, được viết mà không có các biểu tượng 
nhận diện (chẳng hạn như dấu ngoặc vuông cho List, dấu ngoặc đơn cho Tuple, …) thì Python mặc định chúng là Tuple.
### Cách khởi tạo List
```
#bình thường
lst = (1,2.0,5,"sinionth")
#sử dụng constructor
lst = tuple((1, 2, 3))
```
### Một số toán tử với Tuple
Giống list
### Thay đổi nội dung Tuple
Về mặt lý thuyết là không thể
### Ma trận
Giống list
### Các phương thức 
Có count và index (giống list)

** THAM KHẢO
[https://viblo.asia/p/high-performance-python-lists-and-tuples-part-ii-3P0lPMP45ox](https://viblo.asia/p/high-performance-python-lists-and-tuples-part-ii-3P0lPMP45ox)
