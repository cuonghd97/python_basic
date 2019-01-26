# List và Tuple
## 1. List
LIST là một container được sử dụng rất nhiều trong các chương trình Python.Một List gồm các yếu tố sau:
* List trong Python là thay đổi (mutable), nghĩa là Python sẽ không tạo một List mới nếu bạn sửa đổi một phần tử trong List.
* Được giới hạn bởi cặp ngoặc [ ], tất cả những gì nằm trong đó là những phần tử của List.
* Các phần tử của List được phân cách nhau ra bởi dấu phẩy (,).
* List có khả năng chứa mọi giá trị, đối tượng trong Python. Và bao gồm chứa chính nó!

chú ý :List không lưu trữ các phần tử một cách trực tiếp tại chỉ mục. Sự thực là một tham chiếu được lưu trữ tại mỗi chỉ mục 
mà tham chiếu tới đối tượng được lưu trữ ở đâu đó trong bộ nhớ. Điều này là do một số đối tượng có thể lớn hơn một số đối tượng 
khác và vì thế chúng được lưu trữ tại một vị trí bộ nhớ khác.
### 1.1 Cách khởi tạo List
```
#bình thường
lst = [1,2.0,5,"sinionth"]

#sử dụng comprehension
lst2 = [x for x in range(0,6)]

#sử dụng contrutor list(iterable)
lst = list((1, 2, 3))
```

### 1.2 Thay đổi nội dung list
```
lst = [1,2.0,5,"sinionth"]
lst[2]="con cua"
'''
[1, 2.0, 'con cua', 'sinionth']
'''
```

### 1.3 Một số toán tử với List 
Giống hệt chuỗi
```
# toán tử +
a = [1,2,3,4]
b = [5,6,7,8]
a + b 
------------output---------------
[1, 2, 3, 4, 5, 6, 7, 8]

# toán tử *
a = [1,2,3,4]
a*2 
------------output---------------
[1, 2, 3, 4, 1, 2, 3, 4]

```

### 1.3 Ma trận
```
mat = [[0,1,2],[3,4,5]]
mat[1]# hàng 1
mat[0][2] #hàng 0 cột 2
```

### 1.4 Các phương thức 

```
 |  append(...)
 |      L.append(object) -> None -- append object to end
 |  
 |  clear(...)
 |      L.clear() -> None -- remove all items from L
 |  
 |  copy(...)
 |      L.copy() -> list -- a shallow copy of L
 |  
 |  count(...)
 |      L.count(value) -> integer -- return number of occurrences of value
 |  
 |  extend(...)
 |      L.extend(iterable) -> None -- extend list by appending elements from the iterable
 |  
 |  index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
 |  
 |  insert(...)
 |      L.insert(index, object) -- insert object before index
 |  
 |  pop(...)
 |      L.pop([index]) -> item -- remove and return item at index (default last).
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(...)
 |      L.remove(value) -> None -- remove first occurrence of value.
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(...)
 |      L.reverse() -- reverse *IN PLACE*
 |  
 |  sort(...)
 |      L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
```
*sử dụng `help(List)` để biết chi tiết

### 1.5 Sử dụng như stacks
```
stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

### 1.6 Sử dụng như queues
```
>>> from collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

## 2 Tuple
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
tup = (1,2.0,5,"sinionth")
tup_2 = 1, 2, 3

#sử dụng constructor tuple(iterable)
tup_4 = tuple([1, 2, 3])


```
### Một số toán tử với Tuple
Giống hệt chuỗi
```
# toán tử +
a = (1,2,3,4)
b = (5,6,7,8)
a + b 
------------output---------------
(1, 2, 3, 4, 5, 6, 7, 8)

# toán tử *
a = (1,2,3,4)
a*2 
------------output---------------
(1, 2, 3, 4, 1, 2, 3, 4)

```
### Thay đổi nội dung Tuple
Về mặt lý thuyết là không thể
```
a = (1,2,3,4)
a[0] = 10
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
### Ma trận
```
mat = ((0,1,2),(3,4,5))
mat[1]# hàng 1
mat[0][2] #hàng 0 cột 2
```
### Các phương thức 
chỉ có 2 phương thức
```
 |  count(...)
 |      T.count(value) -> integer -- return number of occurrences of value
 |  
 |  index(...)
 |      T.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
```

** THAM KHẢO
[https://viblo.asia/p/high-performance-python-lists-and-tuples-part-ii-3P0lPMP45ox](https://viblo.asia/p/high-performance-python-lists-and-tuples-part-ii-3P0lPMP45ox)
