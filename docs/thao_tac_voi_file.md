# 5.Thao tác tới file
## Mở file
```
#open(file,mode) : đường dẫn và chế độ 
filex=open('test.txt','r')#mở ra để đọc
filey=open('test.txt','w') #mở ra để ghi con trỏ file sẽ trỏ vào đầu file
filez=open('test.txt','a') #mở ra để vào con trỏ file sẽ trỏ vào cuối file
```
## Đóng file
```
#close() : đóng file
filed.close()
```
## Đọc file
```
#read(size=-1) nếu size mắc định hoặc âm sẽ đọc tất cả nội dung,con trỏ sẽ trỏ tại vị trí size sau khi đọc 
filex.read()
filey.read(20) đọc 20 ký tự tại vị trí con trỏ file đang trỏ 
#readline(size=-1) giống read nhưng size ở đây sẽ là số dòng chứ ko phải số ký tự
#readlines()đọc toàn bộ file và chuyển vào vào một list
#đọc file bằng cách đưa vào constructor của list hoặc tuple
filex=open('test.txt')
set1=set(filex)
lst1=list(filex)
```
## Ghi file
```
#write(text) trả về số ký tự đã ghi vào file và còn trỏ sẽ trỏ tại vị trí kết thúc 
```
## Kiểm soát con trở file
```
#seek(offset): di chuyển con trỏ đến vị trí mong muốn
filey.seek(5)
filex.seek(0) 
```
## Câu lệnh with 
cú pháp
	with <câu lệnh> as <biến>:
			<câu lệnh>
```
with open('test.txt') as fileo:
	data=fileo.read()
print(data)
#file chỉ mở trong khối with, sau khi kết thúc khối with file sẽ đóng
```
