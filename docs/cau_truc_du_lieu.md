>Cấu trúc dữ liệu là cách lưu trữ, tổ chức dữ liệu có thứ tự, có hệ thống để dữ liệu có thể được 
sử dụng một cách hiệu quả.

## 1) Array
>Mảng (Array) là một trong các cấu trúc dữ liệu cũ và quan trọng nhất. Mảng có thể lưu giữ 
một số phần tử cố định và các phần tử này nền có cùng kiểu.
> - Phần tử (Element): Mỗi mục được lưu giữ trong một mảng được gọi là một phần tử.
> - Chỉ mục (Index): Mỗi vị trí của một phần tử trong một mảng có một chỉ mục số được sử dụng để 
nhận diện phần tử.
 
### Khởi tạo
```
from array import *

arrayName = array(typecode, [Initializers])
```
|Typecode|Value|
|--------|-----|
|b	|Represents signed integer of size 1 byte|
|B	|Represents unsigned integer of size 1 byte|
|c	|Represents character of size 1 byte|
|i	|Represents signed integer of size 2 bytes|
|I	|Represents unsigned integer of size 2 bytes|
|f	|Represents floating point of size 4 bytes|
|d	|Represents floating point of size 8 bytes|

Ví dụ:
```
from array import *

array1 = array('i', [10,20,30,40,50])

for x in array1:
   print(x)
   
---------------output----------------
10
20
30
40
50
```

## 2) List
<a href="https://github.com/dung1101/python_basic/blob/master/docs/list_tuple.md" target="_blank">Click here</a>
## 3) Tuple
<a href="https://github.com/dung1101/python_basic/blob/master/docs/list_tuple.md" target="_blank">Click here</a>
## 4) Dict
<a href="https://github.com/dung1101/python_basic/blob/master/docs/set_dict.md" target="_blank">Click here</a>
## 5) Set
<a href="https://github.com/dung1101/python_basic/blob/master/docs/set_dict.md" target="_blank">Click here</a>

## 6) Matrix
```
from numpy import *
```
## 7) Map
## 8) Linked Lists
## 9) Stack
```
class Stack:
    def __init__(self):
        self.arr = []
    
    def __str__(self):
        return str(self.arr)
        
    def push(self, value):
        self.arr.append(value)
        
    def pop(self):
        try:
            return self.arr.pop()
        except IndexError:
            return "No element in stack"
```

## 10) Queue
```
class Queue:
    def __init__(self):
        self.arr = []

    def __str__(self):
        return str(self.arr[::-1])

    def enqueue(self, value):
        self.arr.insert(0, value)

    def dequeue(self):
        return self.arr.pop()
-----------------------------------        

```

## 11) Hash Table
## 12) Binary Tree
## 13) Search Tree
## 14) Heap
## 15) Graph