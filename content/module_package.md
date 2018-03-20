# 10. Module & Package
## 10.1 Module
### Định nghĩa
Module được sử dụng để phân loại code thành các phần nhỏ hơn liên quan với nhau. Hay nói cách khác, Module giúp bạn tổ chức Python code một cách logic để giúp bạn dễ dàng hiểu và sử dụng code đó hơn. Về cơ bản, một Module là một file, trong đó các lớp, hàm và biến được định nghĩa. Tất nhiên, một Module cũng có thể bao gồm code có thể chạy.
### import module
Cú pháp
import <tên module>
Ví dụ
Tạo một file lưu là mod1.py ,bên trong code
```
def method1():
  pass
def method2():
```
Tạo một file và import module vào
```
#Cách 1:import module
import mod1
mod1.method1()
mod1.method2()

#Cách 2:import cụ thể method1, method 2
import mod1.method1 ,mod1.method2
method1()
method2()

#Cách 3:import cụ thể method1, method 2
from mod1 import method1,method2
method1()
method2()

#Cách 4:import tất cả thành phần của mod1
from mod1 import *
method1()
method2()
```
## 10.2 Package
### Định nghĩa
Về cơ bản, một Package là một tập hợp các Module, sub-package, … tương tự nhau. Đó là một cấu trúc có thứ bậc của thư mục và file.
### Các bước tạo package
Tạo thư mục có tên là Pack1
Trong thư mục tạo các module mod1.py
```
def method1():
  pass
```
mod2.py
```
def method2():
  pass
```
Tạo file __init__.py trong đó sẽ import các mod1,mod2
```
from mod1 import*
from mod2 import*
```
Bây giờ ta có thể import pack1 và sử dụng như là cách t import module
```
import pack1
pack1.method1()
pack1.method2()
```
