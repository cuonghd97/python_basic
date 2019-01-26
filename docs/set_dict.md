# Set & Dict
## 1 Set
Set là một container, tuy nhiên không được sử dụng nhiều bằng LIST hay TUPLE.
Một Set gồm các yếu tố sau:
* Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
* Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
* Set không chứa nhiều hơn 1 phần tử trùng lặp
* Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.
### 1.1 Cách khởi tạo Set
```
#bình thường
set1 = {1,2.0,5,"sinionth"}

#sử dụng comprehension
set2 = {x for x in range(0,6)}

#sử dụng contrutor
set3 = set([1, 2, 3])
```
### 1.2 Một số toán tử với Set
```
set1 ={1, 2, 3}
set2 = {3, 4, 5}

#Toán tử - (Kết quả trả về những phần tử chỉ thuộc set1 )
set1 - set2
------------output---------------------------------------
{1, 2}

#Toán tử & (giao)
set1 & set2
------------output---------------------------------------
{3}


#Toán tử | (hợp)
set1 | set2
------------output---------------------------------------
{1, 2, 3, 4, 5}


#Toán tử ^ (Trả về các giá trị chỉ thuộc 1 trong 2 set)
set1 ^ set2
------------output---------------------------------------
{1, 2, 4, 5}

```
### 1.3 Indexing và Slicing Set
do set không quan tâm đến vị trí các phần tử nên sẽ không hỗ trợ indexing và slicing
### 1.4 Các phương thức
```
 |  add(...)
 |      Add an element to a set.
 |      
 |      This has no effect if the element is already present.
 |  
 |  clear(...)
 |      Remove all elements from this set.
 |  
 |  copy(...)
 |      Return a shallow copy of a set.
 |  
 |  difference(...)
 |      Return the difference of two or more sets as a new set.
 |      
 |      (i.e. all elements that are in this set but not the others.)
 |  
 |  difference_update(...)
 |      Remove all elements of another set from this set.
 |  
 |  discard(...)
 |      Remove an element from a set if it is a member.
 |      
 |      If the element is not a member, do nothing.
 |  
 |  intersection(...)
 |      Return the intersection of two sets as a new set.
 |      
 |      (i.e. all elements that are in both sets.)
 |  
 |  intersection_update(...)
 |      Update a set with the intersection of itself and another.
 |  
 |  isdisjoint(...)
 |      Return True if two sets have a null intersection.
 |  
 |  issubset(...)
 |      Report whether another set contains this set.
 |  
 |  issuperset(...)
 |      Report whether this set contains another set.
 |  
 |  pop(...)
 |      Remove and return an arbitrary set element.
 |      Raises KeyError if the set is empty.
 |  
 |  remove(...)
 |      Remove an element from a set; it must be a member.
 |      
 |      If the element is not a member, raise a KeyError.
 |  
 |  symmetric_difference(...)
 |      Return the symmetric difference of two sets as a new set.
 |      
 |      (i.e. all elements that are in exactly one of the sets.)
 |  
 |  symmetric_difference_update(...)
 |      Update a set with the symmetric difference of itself and another.
 |  
 |  union(...)
 |      Return the union of sets as a new set.
 |      
 |      (i.e. all elements that are in either set.)
 |  
 |  update(...)
 |      Update a set with the union of itself and others.
```

## 2 Dict
Dict(Dictionary) cũng là một container như LIST, TUPLE. Có điều khác biệt là những container như List, Tuple có các index để phân biệt các phần tử thì Dict dùng các key để phân biệt.

Một Dict gồm các yếu tố sau:
* Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
* Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
* Các phần tử của Dict phải là một cặp key-value, mỗi cặp key-value được xem như là một item. Key mà đã truyền cho item đó phải là duy nhất,
 trong khi đó value có thể là bất kỳ kiểu giá trị nào. Key phải là một kiểu dữ liệu không thay đổi 
 (immutable) như chuỗi, số hoặc tuple.
* Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
### 2.1 Cách khởi tạo Dict
```
#bình thường
dct1 = {'ten':'siniotnh','tuoi':18}

#sử dụng comprehension
dct2 = {key:value for key,value in [['ten','sinionth'],['tuoi',18]]}

#sử dụng contructor
dct1 = dict([['ten','sinionth'],['tuoi',18]])
dct1 = dict(ten='sinionth', tuoi=18)

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
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |  
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 |  
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Returns a new dict with keys from iterable and values equal to value.
 |  
 |  get(...)
 |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.
 |  
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |  
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |  
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |  
 |  setdefault(...)
 |      D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D
 |  
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |  
 |  values(...)
 |      D.values() -> an object providing a view on D's values
```
