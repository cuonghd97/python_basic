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
s[2:6:2] #Cắt từ 2 đến 5 step 2
s[6:2:-1] #Cắt ngược từ 6 về 3
```

## các method cơ bản
**capitalize()**: viết hoa chữ cái đầu chuỗi 
```
>>> "hi hi".capitalize()
'Hi hi'
```

**swapcase()**: đổi hoa <-> thường
```
"aBc".swapcase()
'AbC'
```

**split(sep, maxsplit)**: cắt chuỗi
```
>>>"a B c".split(sep=" ")
['a', 'B', 'c]
>>>"a B c".split(sep=" ", maxsplit=1)
['a', 'B c']
```

**join(iterable:str)**: ghép chuỗi
```
>>>"".join(["1","2","3"])
'123'
"-".join(["1","2","3"])
'1-2-3'
```

**find(sub)**: tìm kiếm vị trí đầu tiên xuất hiện `sub` trong chuỗi
```
>>>"ABCDCDC".find("CD")
2
```

**count(sub)**: đếm số `sub` trong chuỗi
```
>>>"ABCDCDCD".count("D")
3
```

**isalnum()**: kiểm tra chuỗi chỉ chứa ký tự alphabet và số (a-z, A-Z, 0-9)
```
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False
```

**isalpha()**: kiểm tra chuỗi chỉ chứa ký tự alphabet
```
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
```

**isdigit()**: kiểm tra chuỗi chỉ chứa ký tự số
```
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```

**islower()**: kiểm tra chuỗi mà các ký tự alphabet đều là kỹ tự thường (a-z)
```
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
```

**issuper()**: kiểm tra chuỗi mà các ký tự alphabet đều là kỹ tự hoa (A-Z)
```
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
```

**center(width,symbol)**: căn lề giữa
```
>>>"a".center(7)
'   a   '
>>>"a".center(7, "*")
'***a***'
```

**ljust(width,symbol)**: căn lề trái
```
>>>"a".ljust(7)
'a   '
>>>"a".ljust(7, "*")
'a******'
```

**rjust(width,symbol)**: căn lề giữa
```
>>>"a".rjust(7)
'      a'
>>>"a".rjust(7, "*")
'******a'
```

<b>format(*args, **kwargs)<b>: định dạng chuỗi
```
>>>"{} + {} = {}".format(1,2,3)
'1 + 2 = 3'
>>>"{0} + {2} = {1}".format(1,3,2)
'1 + 2 = 3'
>>>"{a} + {b} = {c}".format(a=1,c=3,b=2)
'1 + 2 = 3'
>>>'{:-^11}'.format('Sinonth') #căn lề giữa
'--Sinonth--'
>>>'{:-<11}'.format('Sinonth') #căn lề trái
'Sinonth----'
>>>'{:->11}'.format('Sinonth') #căn lề phải
'----Sinonth'

>>>"{:.2f}".format(13.006)
'13.01'
```