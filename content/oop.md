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


