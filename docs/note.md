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

#### 4) Get size off screen window
```
from win32api import GetSystemMetrics
print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
```

#### 5)Command Line Arguments
[https://www.tutorialspoint.com/python/python_command_line_arguments.htm](https://www.tutorialspoint.com/python/python_command_line_arguments.htm)

#### 6)Comprehensive
```
x = 2
y = 4
z = 3
n = 1
# in ra toa do [X,Y,Z] tuong ung voi 0<= X,Y,Z <= x,y,z va X+Y+Z != n
print([[X,Y,Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if((X+Y+Z)!=n)])
```

#### 7)Print exactly digit after ','
```
print("%.2f" %avergare)
```

#### 8) Format
```
def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(1,number+1):
        print ("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
```

#### 9) Alphabet char
```
import string
string.ascii_lowercase

`abcdefjhijklmnnopqrstuvxyzw`
```

#### 10) Shuffe
```
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)

['Flying', 'Keep', 'Blue', 'High', 'The', 'Flag']
```

#### 11) multi thread
Đối với máy 1 core thì thread không thực sự chạy sông các thread mà chuyển đổi qua lại giữa các thread sử dụng 1 core CPU duy nhất => không làm tăng hiệu năng.

#### 12) String rpartition()
cú pháp: `string.rpartition(separator)`
chia string ra làm 3 phần tại `separator` xuất hiện cuối
```
>>>string = "ha ha 123"
>>>string.rpartition(" ")

('ha ha', ' ', '123')
```

#### 13) built-in function
[https://docs.python.org/3/library/functions.html#getattr](https://docs.python.org/3/library/functions.html#getattr)
