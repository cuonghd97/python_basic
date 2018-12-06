#### 4) Unserscore `_`
##### 4.1) When used in interpreter
python interpreter lưu trữ giá trị biểu thức cuối cùng vào biến `_`:
```
>>10
10
>> _ * 3
30
>> _ * 10
300
```

##### 4.2) For Ignoring the values
Sử dụng `_` để bỏ qua giá trị
```
# Ignore a value when unpacking
x, _, y = (1, 2, 3) # x = 1, y = 3 
# Ignore the multiple values. It is called "Extended Unpacking" which is available in only Python 3.x
x, *_, y = (1, 2, 3, 4, 5) # x = 1, y = 5  
# Ignore the index
for _ in range(10):     
    do_something()  
# Ignore a value of specific location
for _, val in list_of_tuple:
    do_something()
```
##### 4.3) Give special meanings to name of variables and functions
##### `_single_leading_underscore`
Dùng để khai báo biến, hàm private trong class hoặc module. Các biến hàm này chỉ sử dụng trong nội bộ class hoặc module. Ví dụ các biến, hàm private sẽ ko gọi được khi `import`. Tuy nhiên python ko hỗ trợ private thực sự ta vẫn có cách để gọi đến ở bên ngoài.

```
_internal_name = 'one_nodule' # private variable
_internal_version = '1.0' # private variable

class _Base: # private class
    _hidden_factor = 2 # private variable
    def __init__(self, price):
        self._price = price
    def _double_price(self): # private method
        return self._price * self._hidden_factor
    def get_double_price(self):
        return self._double_price() 
```

Cách để gọi private ở bên ngoài `_X_Y` trong đó:
- X là tên module hoặc class
- Y là tên biến hoặc hàm

##### `__double_leading_and_trailing_underscore__`
Sử dụng cho biến, hàm đặc biệt ( “magic method”)
[https://www.python-course.eu/python3_magic_methods.php](https://www.python-course.eu/python3_magic_methods.php)

