# 8 Vòng lặp
## 8.1 While
### Cú pháp
```
while <điều kiện>:
    <câu lệnh>
```
Nếu điều kiện thỏa mãn sẽ thực hiện vòng lặp
```
while a > 10 :
    a-=1
```
### Cú pháp
```
while <điều kiện>:
    <câu lệnh>
else :
    <câu lệnh>
```
Nếu điều kiện thỏa mãn sẽ thực hiện vòng lặp, sau khi kết thúc vòn lặp sẽ thực hiện câu lệnh trong khối else
```
while a > 10 :
    a-=1
else :
    print(a)
```
## 8.2 For
### Cú pháp
```
for <biến 1> , <biến 2>, ...<biến n> in <tập hợp>:
   <câu lệnh>
```
Duyệt hết các giá trị trong tập hợp, mỗi 1 lân sẽ thực hiện câu lệnh
```
for x in [1,2,3]:
   print(x)
```
### Cú pháp
```
for <biến 1> , <biến 2>, ...<biến n> in <tập hợp>:
   <câu lệnh>
else:
   <câu lệnh>
```
Sau khi kết thúc vòng for sẽ thực hiện câu lệnh trong khối else
```
for x in [1,2,3]:
   print(x)
else:
   print("Het")
```
## 8.3 break & continue
### break : thoát khỏi vòng lặp nếu có khối else thì bỏ qua cả khối else
### continue: tiếp tục vòng lặp tiếp theo
