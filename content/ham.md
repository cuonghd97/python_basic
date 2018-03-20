# 9 Hàm
## 9.1 Định nghĩa 
Hàm, là một khối code được tổ chức và có thể tái sử dụng, để thực hiện một hành động nào đó. Trong các chương trước, bạn đã làm quen với một số hàm đã được xây dựng sẵn trong Python, điển hình như hàm print(). Tuy nhiên bạn cũng có thể tạo riêng cho mình một hàm với cách định nghĩa và kiểu giá trị cho riêng bạn. Các hàm này được gọi là user-defined function.
Cú pháp
```
def <tên hàm> (<các tham số truyền vào>):
  <các câu lệnh thực thi>
```
## 9.2 Gọi hàm
Cú pháp
```
<tên hàm>(<các tham số truyền vào>)
```
## 9.3 Tham số 
### Tham số bắt buộc
```
def tong (a,b):
  print(a+b)
```
Khi khai báo tham số như trên thì khi gọi hàm phải truyền đủ cả 2 tham số nếu không sẽ báo lỗi
### Tham số mặc định
```
def tong (a=0,b=0):
  print(a+b)
```
Khi truyền vào thiếu tham số thì hàm sẽ lấy giá trị mặc định của tham số
### Tham số từ khóa
```
def phanSo (tuSo,mauSo):
  print(tuSo,"/",mauSo)
```
KHi ta gọi hàm phanSo(3,5) thì tuSo=3 và mauSo=5 kết quả 3/5
Khi ta gọi hàm phanSo(mauSo=3,tuSo=5) thì kết quả là 5/3 
### Tham số có số tham số thay đổi
```
def tong (*thamSo)
  t=0
  for i in thamSo
    t+=i
  print(t)
```
Ta có thể gọi hàm với số tham số tùy ý
## 9.4 Hàm nặc danh
Hàm nặc danh được tạo bởi sử dụng từ khóa lambda, không phải bởi từ khóa def. Hàm này chỉ trả về một giá trị dưới dạng một biểu thức đã được ước lượng.
Cú pháp
```
<tên hàm> = lambda <danh sách tham số>:<biểu thức>
```
Gọi hàm
```
<tên hàm>(<danh sách tham số>)
```
Ví dụ
```
#định nghĩa hàm
square=lambda x1: x1*x1
#gọi hàm
print(square(10))
```
