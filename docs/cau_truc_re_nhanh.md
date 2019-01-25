# 7.Cấu trúc rẽ nhánh

## cú pháp
```
if <điều kiện>:
  <câu lệnh>
```
nếu điều kiện được thỏa mãn thì câu lệnh được thực hiện
```
if a > 10 :
  print('Số lớn hơn 10')
```
cú pháp
```
if điều kiện:
  <câu lệnh>
else :
  <câu lệnh>
```
* Nếu điều kiện được thỏa mãn thì câu lệnh trong khối if được thực hiện 
* Nếu không thỏa mãn điều kiện thì câu lệnh trong khối else được thực hiện 
```
if a > 10 :
    print('Số lớn hơn 10')
else :
    print('Số không lớn hơn 10')
```
cú pháp
```
if <điều kiện 1>:
  <câu lệnh>
elif <điều kiện 2>:
  <câu lệnh>
...
elif <điều kiện n>:
  <câu lệnh>
else :
  <câu lệnh>
``` 
* Nếu điều kiện thứ i nào đó được thỏa mãn thì câu lệnh trong khối tương ứng được thực hiện 
* Nếu không thỏa mãn bất kỳ điều kiện nào thì câu lệnh trong khối else được thực hiện 
