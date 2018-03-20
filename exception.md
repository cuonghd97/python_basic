# 11.Exception
## Exception là gì?
Ngoại lệ có thể là bất kỳ điều kiện bất thường nào trong chương trình mà phá vỡ luồng thực thi chương trình đó. Bất cứ khi nào một ngoại lệ xuất hiện, mà không được xử lý, thì chương trình ngừng thực thi và vì thế code không được thực thi.
## Xử lý ngoại lệ
Cú pháp try-except-else
```
try:
   <câu lệnh có thể gây ra exception>
except Exception1:
   <xử lý nếu có exception 1>
except Exception2:
   <xử lý nếu có exception 2>
else:
   <xử lý nếu không có exception>
```
Nếu không biết rõ exception loại nào có thể để except:
ví dụ
```
try:
   fh = open("testfile", "w")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print "Error: Khong tim thay file"
else:
   print "Thanh cong ghi noi dung vao file"
   fh.close()
```
Cú pháp try-finally
```
try:
   <câu lệnh có thể gây ra exception>
finally:
   <thực thi dù có exception hay không>
```
ví dụ
```
fh = open("testfile", "w")
   try:
      fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
   finally:
      print "Chuan bi dong file"
      fh.close()
```
