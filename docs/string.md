# 2.String
String là một trong các kiểu phổ biến nhất trong Python. String trong Python là immutable. 
Python không hỗ trợ một kiểu chữ cái; chúng được coi như các chuỗi có độ dài là 1.
Trong Python, String được lưu giữ dưới dạng các ký tự đơn trong vị trí ô nhớ liên tiếp nhau. 
## Khai báo
Sử dụng ' ' or " " or ''' ''' or """ """ để khai báo chuỗi
```
#' ' và " " để khai báo chuỗi bình thường
'Sinionth'
"Hello wolrd !"
#''' ''' và """ """ để khai báo chuỗi nhiều dòng
'''File
Edit
Search
View
Encoding
Language
'''
```
*chú ý: Trong python 2.x string chứa ký tự ANCII còn python 3.x là unicode, muốn khai báo unicode ở python 2.x thì thêm `u` ở đầu ví dụ `u'hello'`

## Escape sequence 

|Tên|Kí hiệu|Giải thích|
|---|-------|----------|
|Alert|\a|Phát ra một tiếng bip|
|Backspace|\b|In ra một khoảng trắng|
|Newline|\n|Đưa con trỏ xuống dòng tiếp theo|
|Horizontal tab|\t|In một horizontal tab|
|Single quote|\’|In ra kí tự ‘|
|Double quote|\”|In ra kí tự “|
|Blackslash| \\ |In ra kí tự \ |

## Chuỗi trần: 
giúp sửa nhưng escape sequence không mong muốn, thực chất chuỗi trần sẽ thêm \ vào trước escape sequence. 
```
r'si\nionth'
```
Một số toán tử với chuỗi
```
#toán tử +
s = "si"
s +="nionth"
---------------------------------
>> "sinionth"

#toán tử *
s ="abc"
s *=2
---------------------------------
>> "abcabc"

#toán tử in trả về True or False
"a" in "abc"
---------------------------------
>>True

```

## indexing và cắt chuỗi
```
s = "sinionth"
s[2] #vị trí thứ 2 từ trái qua phải đếm từ 0
s[-4] #vị trí thứ 4 từ phải qua trái đếm từ 1
s[4:8] #Cắt từ vị trí thứ 4 đến vị trí thứ 7 trái qua phải
s[3:] #Cắt từ 3 đến hết trái qua phải
s[3:None] #Cắt từ 3 đến hết trái qua phải
s[:5] #Cắt từ đầu đến 4 trái qua phải
s[None:5] #Cắt từ đầu đến 4 trái qua phải
```
