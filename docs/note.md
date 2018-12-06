#### 1) `if __name__ == '__main__':`

Ta có một file `file1.py` như sau:
```
import file2

if __name__ == '__main__':
  print('Hello wolrd')
```

và `file2.py`:
```
print('123')
if __name__ == '__main__':
  print('Hoho')
```

- khi run `file1.py` thì thuộc tính `__name__` của module file1 sẽ được gán bằng `'__main__'` và các thuộc tính `__name__` của các module import vào sẽ gán bằng tên của module đó file2 sẽ gán bằng `'file2'`. 
- câu lệnh `import file2` trong `file1.py` sẽ thực thi tất cả các câu lệnh trong module file2 ngoại trừ khối `if __name__ == '__main__':` vì lúc này `__name__` của file2 là `'file2'` như vậy kết quả khi chạy `file1.py` sẽ ra là
```
Hello world
123
```

#### 2) Iterator và Generator
##### 2.1) Iterator 
là một khái niệm chỉ các lớp dạng danh sách cho phép chúng ta duyệt qua chúng mà không cần quan tâm đến kiểu dữ liệu đó là gì.

Để một lớp được gọi là Iterator thì lớp đó phải hỗ trợ 2 phương thức là `__iter__()` và `__next__()`. 
- ` __iter__()`: chỉ đơn giản là trả về đối tượng tham chiếu tới chính nó
- `__next__()` : trả về phần tử tiếp theo có trong danh sách cho đến phần tử cuối cùng thì giải phóng exception StopIteration.

```
str = "123"
it = iter(str)
while True:
    try:
        print (it.__next__())
    except StopIteration:
        break
        
--------OUTPUT---------
1
2
3
```
##### 2.2) Generator 
Generator chẳng qua cũng chỉ là Iterator, chúng cũng tạo ra một đối tượng kiểu danh sách, nhưng bạn chỉ có thể duyệt qua các phần tử của generator một lần duy nhất vì generator không lưu dữ liệu trong bộ nhớ mà cứ mỗi lần lặp thì chúng sẽ tạo phần tử tiếp theo trong dãy và trả về phần tử đó.

```
def gen():
    x, y = 1, 2
    yield x, y
    x += 1
    yield x, y
    
it = gen()

while True:
    try:
        print (it.__next__())
    except StopIteration:
        break
        
----------OUTPUT--------------
(1, 2)
(2, 2)
```

#### 3) Cách truyền tham số dạng *args và **kwargs trong python

Thực sự thì không nhất thiết phải là *args và **kwargs. điều quan trọng là tham số có 1 dấu sao * hay là 2 dấu sao **. Đặt tên tham số là *var hay **vars hay bất cứ thứ gì bạn muốn.
Nhưng để dễ hiểu thì nên dùng tên chuẩn là *args và **kwargs

##### 3.1) *args và **kwargs dùng để làm gì?

Khi khai báo 1 hàm, sử dụng *args và **kwargs cho phép bạn truyền vào bao nhiêu tham số cũng được mà không cần biết trước số lượng.
Ví dụ:
```
//với giả sử các tham số truyền vào đều là số
def sum(*args):
    total = 0
    for number in args:
        total += number
return total

// gọi hàm
sum(1, 2, 3,19)
sum( 1, 100)
```
##### 3.2) *args và **kwargs khác gì nhau?

Khi gọi hàm trong Python, có 2 kiểu truyền tham số:
- Truyền tham số theo tên.
- Truyền tham số bình thường theo thứ tự khai báo đối số.
```
def register(name, password):
	....
#Truyền tham số theo kiểu thông thường, phải theo đúng thứ tự
register( 'Coulson', 'hail_Hydra')
#Truyền tham số theo tên, Không cần phải theo thứ tự khai báo thao số
register( password='cookHim', name='Skye')
```
*args nhận các tham số truyền bình thường. Sử dụng args như một list.
**kwargs nhận tham số truyền theo tên. Sử dụng kwargs như một. dictionary
Ví dụ
```
def test_args(*args):
    for item in args:
        print (item)
----------------------------------------------
>>test_args('Hello', 'world!')
Hello
world!
----------------------------------------------
def test_kwargs(*kwargs):
    for key, value in kwargs.iteritems():
        print ('{0} = {1}'.format(key, value))
-----------------------------------------------    
>>test_kwargs(name='Dzung', age=10)
age = 10
name = Dzung
```
##### 3.3) Thứ tự sử dụng và truyền tham số *args, **kwargs và tham số bình thường
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
