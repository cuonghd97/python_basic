 ## Decorator là gì ?

```
  Decorator là một mẫu thiết kế (Design pattern) thường được dùng để thay đổi hành vi, chức năng của 
hàm(function) hoặc lớp (class) mà không cần phải thay đổi code của hàm hoặc lớp.
  Về cơ bản Decorator giống như một lớp vỏ bọc (wrapper), nó thay đổi hành vi(behavior) của code trước
và sau khi gọi hàm chính (hàm được decorate).
```

### Ví dụ 1
  CHÚ Ý QUAN TRỌNG: hàm wrapper và hàm f phải có tham số phù hợp với nhau. Ví dụ như hàm f nhận vào chỉ 2 tham số thì hàm decorator không thể nhận vào 3 tham số hoặc 1 tham số.

```
def ten_decorator(f):
      def wrapper(ten):
          chuoi_moi = "Ten tui la " + ten
          return f(chuoi_moi)
      return wrapper

@ten_decorator
def xuat_ten( ten ):
    print (ten)
--------------------------------------------
xuat_ten('sinionth')                     
>> Ten tui la sinionth                   
```

### Ví dụ 2
  Decorator nào càng ở trên, xa function thì sẽ bọc lớp ngoài.Code của decorator được thực thi ngay lúc file nguồn Python được load lên. Ngoại trừ code trong hàm wrapper của decorator trong cùng sẽ được thực thi lúc gọi hàm. Decorator được gọi thực thi theo thứ tự từ trong (gần hàm nhất) ra ngoài. 
```
@ten_decorator1
@ten_decorator2
@ten_decorator3
def xuat_ten(ten):
    print (ten)
```

### Ví dụ 3
  decorator cũng có thể là một hàm nhận vào tham số bất kỳ và trả về một hàm và hàm trả về này nhận vào tham số là một hàm khác.
```
def chuc_danh_decorator(ten_chuc_danh):
    def ten_decorator(f):
        def wrapper(ten):
            chuoi_moi = "Xin gioi thieu {} {}".format(ten_chuc_danh, ten)
            return f(chuoi_moi)
        return wrapper
    return ten_decorator
  
@chuc_danh_decorator("Giao su")
def gioi_thieu(ten):
  print(ten)
---------------------------------------------------------------------
gioi_thieu('sinionth')
>> Xin gioi thieu Giao su sinionth
```
