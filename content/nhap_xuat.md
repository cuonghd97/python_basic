# 6.Nhập xuất
# 6.1 Xuất
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
* file:  đầu ra mặc định là cửa sổ console 
* sep:   kí tự xem giữa các giá trị , mặc định là a space.
* end:   giá trị khi kết thúc, mặc định là a newline.
* flush: whether to forcibly flush the stream.
```
print("Hello","World", sep='---')
Hello---World
...
print("Hello",end='***')
Hello***
```
# 6.2 Nhập
input()
Kiểu giá trị nhập vào luôn luôn là string
```
i=input()
print("Hello",i)
```	
