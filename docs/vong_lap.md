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
## 8.3 break, continue & pass
 - `break`: thoát khỏi vòng lặp (gần nhất) nếu có khối else thì bỏ qua cả khối else
 - `continue`: tiếp tục vòng lặp tiếp theo
 - `pass`: không làm gì cả dùng để cho phù hợp cú pháp
 
## 8.4 Looping technique
- dictionary

```
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

------------output--------------------------------------
gallahad the pure
robin the brave
```

- get index
```
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

------------output--------------------------------------
0 tic
1 tac
2 toe
```

- loop >2 same time
```
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

------------output--------------------------------------
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
```

 
