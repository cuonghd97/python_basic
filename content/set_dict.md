# 4.Set & Dict
## 4.1 Set
Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.
Một Set gồm các yếu tố sau:
* Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
* Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
* Set không chứa nhiều hơn 1 phần tử trùng lặp
* Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.
### Cách khởi tạo Set
```
#bình thường
set1 = {1,2.0,5,"sinionth"}
#sử dụng comprehension
lst2 = {x for x in range(0,6)}
#sử dụng contrutor
set1 = set({1, 2, 3})
```
### Một số toán tử với List 
```
set1 ={1,2,3}
set2 = {3,4,5}
#Toán tử in (kiểm tra phần tử có thuộc set hay không)
1 in set1
#Toán tử - (Kết quả trả về những phần tử chỉ thuộc set1 )
set1 - set2
#Toán tử & (giao)
set1 & set2
#Toán tử | (hợp)
set1 | set2
#Toán tử ^ (Trả về các giá trị chỉ thuộc 1 trong 2 set)
set1 ^ set2
```
### Indexing và cắt Set
do set không quan tâm đến vị trí các phần tử nên sẽ không hỗ trợ indexing và cắt
### Các phương thức
```
#clear() : xóa mọi phần tử
#remove(x) xóa x khỏi set
#pop() lấy phần tử và xóa khỏi set 
#discard(i)
#copy() : copy
#add(i): thêm giá trị i vào set nếu đã có thì bỏ qua
```
## 4.2 Dict
Dict(Dictionary) cũng là một container như LIST, TUPLE. Có điều khác biệt là những container như List, Tuple có các index để phân biệt các phần tử thì Dict dùng các key để phân biệt.
Chắc bạn cũng dùng từ điển tiếng Anh để tra từ vựng rồi nhỉ? Có rất nhiều từ vựng trong đó nhưng mà không từ vựng nào giống nhau. Có chăng chúng chỉ giống nhau về nghĩa? Và đó cũng như Dict(Dictionary) hoạt động trong Python
Một Dict gồm các yếu tố sau:
* Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
* Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
* Các phần tử của Dict phải là một cặp key-value
* Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
* Các key buộc phải là một hash object
### Cách khởi tạo Dict
```
#bình thường
dct1 = {'ten':'siniotnh','tuoi':18}
#sử dụng comprehension
dct2 = {key:value for key,value in [['ten','sinionth'],['tuoi',18]]}
#sử dụng contructor khởi tạo dict rỗng
dct1 = dict([['ten','sinionth'],['tuoi',18]])
dct1 = dict(ten='sinionth', tuoi=18)
#Sử dụng Phương thức fromkeys
key=['ten','tuoi']
dct1 = dict.fromkeys(key)

```
### Lấy value trong Dict bằng key
```
dct1['ten']
dct1['tuoi']
```
### Thay đổi nội dung Dict 
```
#sửa
dct1['ten']='sini'
#thêm
dct1['gioi_tinh']='nam'
```
### các phương thức
```
#clear() : xóa mọi phần tử
#copy() : copy
#get('key') : trả về giá trị tương ứng với key
#items(): trả về một giá trị thuộc lớp dict_items là một container chứa các tuple 
#keys() :trả về một giá trị thuộc lớp dict_keys là một container chứa các key
#values() :trả về một giá trị thuộc lớp dict_values là một container chứa các values
#pop(key) : trả về gí trị tương ứng với key và xóa khỏi dict
#popitem() : trả về 1 tuple chứa 2 giá trị key-value bất kỳ và xóa khỏi dict
#setdefault(key) : trả về vá trị tương ứng với key ,nếu key không tồn tại thì thêm key vào list với giá trị là None 
#update(...) thêm phần tử vào list
dct1.update(ho='John')
dct1.update({'dem':'Nguyen'})
dct1.update(['code',6913])
```
