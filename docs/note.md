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
