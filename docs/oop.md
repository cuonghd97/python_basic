# 12.OOP
## 12.1 Tạo class
cú pháp
```
class <tên class>(<danh sách các class cha>):
  <thân class>
```
ví dụ
```
class Cha:
  ttc1='Chung'
  ttc2=[]
  # constructor
  def __init__(self,tt1,tt2):
    self.tt1=tt1
    self.tt2=tt2
  def ptCha():
    print('phuong thuc cha')
```
* ttc1,ttc2 là các thuộc tính của class,và tất cả các đối tượng thuộc class sẽ có chung thuộc tính này ,khi ta thay đổi thuộc tính chung của một đối tượng thì thuộc tính chung của tất cả các đối tượng khác cũng thay đổi theo.
* tt1,tt2 cũng là các thuộc tính của class, mỗi một đối tượng sẽ có các thuộc tính tt1,tt2 là khác nhau.
* ptCha là phương thức của class
```
cha1 = Cha(11,111)
cha2 = Cha(22,222)
------------------
cha1.ttc
>> Chung
cha2.ttc
>> Chung

cha1.tt1
>> 11
cha2.tt1
>> 22
```
## 12.2 Kế thừa
```
class Con1(Cha):
  def ptCon1():
    print('phuong thuc con')
```
python hỗ trợ đa kế thừa 
```
class ConNgua:
    chan = 'Dai'
    bay = True

    def __init__(self, gioi_tinh='Duc'):
        self.gioi_tinh = gioi_tinh
       
    def chay(self):
        print('Nhanh')


class ConLua:
    chan = 'Ngan'
    boi = True

    def __init__(self, gioi_tinh='Cai'):
        self.gioi_tinh = gioi_tinh
    
    def chay(self):
        print('Cham')

class ConLa(ConNgua, ConLua):
    pass
----------------------------------------
la1 = ConLa()
la1.chan
>> Dai
la1.gioi_tinh
>> Duc
la1.bay
>> True
la1.boi
>> True
la1.chay()
>> Nhanh
```
* Lớp con sẽ kế thừa tất cả các thuộc tính và phương thức của các lớp cha. Mặc định nếu các phương thức và thuộc tính của các lớp cha trùng nhau thì lớp con sẽ kế thừa của lớp cha nào khai báo trước trong trường hợp trên là ConNgua

## 12.3 Ghi đè
```
class Con2(Cha):
  def ptCha():
    print('phuong thuc cha bi ghi de boi con 2')
```
* lớp Con2 kế thừa lớp Cha cả thuộc tính và phương thức ptCha, tuy nhiên phương thức ptCha ở lớp Con2 được định nghĩa khác
## 12.4 Ẩn dữ liệu
Các thuộc tính bình thường có thể gọi ra ở bên ngoài lớp thông qua cú pháp
<tên lơp>.<thuộc tính> hoặc <tên đối tượng thuộc lơp>.<thuộc tính>
Khi ta không muốn bên nguoài nhìn thấy thuộc tính nào thì tên thuộc tính ta thêm __ trước tương tụ cho phương thức
```
class Vidu:
  __thuocTinhAn=100
```
Tuy nhiên ta vẫn có thể gọi được bằng cú pháp
<đối tượng>._<tên lớp>__<tên thuộc tính>

## 12.5 Các thuộc tính mặc định
`__dict__`: Là Dictionary chứa namespace của lớp.
`__doc__`: Được sử dụng để truy cập Documentation String của lớp nếu có.
`__name__`: Là tên lớp.
`__module__`: Là tên Module trong đó lớp được định nghĩa. Thuộc tính là `__main__` trong chế độ tương tác.
`__bases__`: Là một Tuple chứa các lớp cơ sở.
```
class Sinhvien:
   'Class co so chung cho tat ca sinh vien'
   svCount = 0

   def __init__(self, ten, hocphi):
      self.ten = ten
      self.hocphi = hocphi
      Sinhvien.svCount += 1
   
   def displayCount(self):
     print "Tong so Sinh vien %d" % Sinhvien.svCount

   def displaySinhvien(self):
      print "Ten : ", self.ten,  ", Hoc phi: ", self.hocphi
-----------------------------------------------------------
Sinhvien.__doc__: Class co so chung cho tat ca sinh vien
Sinhvien.__name__: Sinhvien
Sinhvien.__module__: __main__
Sinhvien.__bases__: ()
Sinhvien.__dict__: {'__module__': '__main__', 'displayCount':
<function displayCount at 0xb7c84994>, 'svCount': 2, 
'displaySinhvien': <function displaySinhvien at 0xb7c8441c>, 
'__doc__': 'Class co so chung cho tat ca sinh vien', 
'__init__': <function __init__ at 0xb7c846bc>}
```

## 12.6 Một số phương thức mặc định
|Phương thức|chức năng|Lời gọi mẫu|
|-----------|---------|-----------|
|`__init__`( self [,args...]|Là constructor (với bất kỳ tham số tùy ý nào)|obj = tenLop(args)|
|`__del__`( self )|Là destructor, xóa một đối tượng| del obj|
|`__repr__`( self )| Biểu diễn chuỗi hiển thị khi gọi đối tượng(<Sinhvien: chuoigido>)|repr(obj)|
|`__str__`( self )| Biểu diễn chuỗi sau khi convert đối tượng sang string|str(obj)|
|`__cmp__`( self, x )|So sánh đối tượng|cmp(obj, x)|

## 12.7 Một số toán tử
|Phương thức|chức năng|Toán tử|
|-----------|---------|-------|
|`__add__`( self, other) |Cộng hai đối tượng| + |
|`__sub__`( self, other)|Trừ hai đối tượng| - |
|`__mul__`( self, other )| Nhân hai đối tượng|x|
|`__div__`( self )| Chia đối tượng sang string|:|
