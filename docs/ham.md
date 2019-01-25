# 9 Hàm
## 9.1 Định nghĩa 
Hàm, là một khối code được tổ chức và có thể tái sử dụng, để thực hiện một hành động nào đó. Trong các chương trước, bạn đã làm quen với một số hàm 
đã được xây dựng sẵn trong Python, điển hình như hàm print(). Tuy nhiên bạn cũng có thể tạo riêng cho mình một hàm với cách định nghĩa và kiểu giá trị 
cho riêng bạn. Các hàm này được gọi là user-defined function.
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
### 9.3.1 Tham số bắt buộc
```
def tong (a,b):
  print(a+b)
```
Khi khai báo tham số như trên thì khi gọi hàm phải truyền đủ cả 2 tham số nếu không sẽ báo lỗi
### 9.3.2 Tham số mặc định
```
def tong (a=0,b=0):
  print(a+b)
```
Khi truyền vào thiếu tham số thì hàm sẽ lấy giá trị mặc định của tham số
### 9.3.3 Tham số từ khóa
```
def phanSo (tuSo,mauSo):
  print(tuSo,"/",mauSo)
```
KHi ta gọi hàm phanSo(3,5) thì tuSo=3 và mauSo=5 kết quả 3/5

Khi ta gọi hàm phanSo(mauSo=3,tuSo=5) thì kết quả là 5/3 

### 9.3.4 Cách truyền tham số dạng *args và **kwargs trong python

Thực sự thì không nhất thiết phải là *args và **kwargs. điều quan trọng là tham số có 1 dấu sao * hay là 2 dấu sao **. Đặt tên tham số là *var hay **vars hay bất cứ thứ gì bạn muốn.
Nhưng để dễ hiểu thì nên dùng tên chuẩn là *args và **kwargs

#### 9.3.4.1 *args và **kwargs dùng để làm gì?

Khi khai báo 1 hàm, sử dụng *args và **kwargs cho phép bạn truyền vào bao nhiêu tham số cũng được mà không cần biết trước số lượng.
Ví dụ:
```
//với giả sử các tham số truyền vào đều là số
def summ(*args):
    total = 0
    for number in args:
        total += number
return total

// gọi hàm
summ(1, 2, 3, 19)
summ( 1, 100)
```
##### 9.3.4.2 *args và **kwargs khác gì nhau?
*args nhận các tham số truyền bình thường. Sử dụng args như một list.

**kwargs nhận tham số truyền theo tên. Sử dụng kwargs như một. dictionary
Ví dụ
```
def test_args(*args):
    for item in args:
        print (item)

test_args('Hello', 'world!')
----------------output------------------------
Hello
world!

i = [1,2,3]
test_args(*i)
----------------output------------------------
1
2
3


def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print ('{0} = {1}'.format(key, value))
    
test_kwargs(name='Dzung', age=10)
----------------output------------------------
age = 10
name = Dzung

a = {'a':1, 'b':2, 'c':3}
test_kwargs(**a)
----------------output------------------------
a = 1
b = 2
c = 3
```
##### 9.3.4.3 Thứ tự sử dụng và truyền tham số *args, **kwargs và tham số bình thường
Khi sử dụng phải khai báo đối số theo thứ tự:
`đối số xác đinh --> *args --> **kwargs` .
Đây là thứ tự bắt buộc. Và khi truyền tham số bạn cũng phải truyền theo đúng thứ tự này. Không thể truyền lẫn lộn giữa 2 loại.
Khi sử dụng đồng thời *args **kwargs thì không thể truyền tham số bình thường theo tên
Ví dụ
```
def show_detail(name, *args, **kwargs):
  ...
-----------------------------------------------------------
>>show_detail(name='Coulson', 'agent', age='40', level='A')
#Error
-----------------------------------------------------------
def show_detail_2(name, **kwargs):
    ...
-----------------------------------------------------------
>>show_detail_2(name='Coulson', age='40', level='A')
#Chạy Ok
```

### 9.3.5 Tất cả parameter (argument) trong Python được truyền bởi tham chiếu. 
Nghĩa là nếu bạn thay đổi những gì mà một parameter tham chiếu tới bên trong một hàm, thì thay đổi này cũng phản ánh trong hàm đang gọi.
```
a = 10

def abc(x):
	x +=1
-----------
def(a)
>> a = 11
```
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

## 9.5 Doc string
```
def my_function():
     '''
     Do nothing, but document it.
     No, really, it doesn't do anything.
     '''
     pass

print(my_function.__doc__)
----------------output------------------------
Do nothing, but document it.
No, really, it doesn't do anything.
```