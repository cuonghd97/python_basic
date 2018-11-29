## 1.Number
Kiểu dữ liệu Number lưu trữ các giá trị số. Chúng là các kiểu dữ liệu immutable, hay là kiểu dữ liệu không thay đổi, nghĩa là các thay đổi về giá trị của kiểu dữ liệu số này sẽ tạo ra một đối tượng được cấp phát mới.
```
var1 = 1
var2 = 10
```
Python có 3 kiểu dữ liệu số cơ bản đó là:
- Kiểu int: kiểu số nguyên không có dấu thập phân.
- Kiểu long: là các số nguyên không giới hạn kích cỡ, được theo sau bởi một chữ l hoặc chữ L.
- Kiểu float: số thực với dấu thập phân. Kiểu này cũng có thể được viết ở dạng số mũ của 10 với E hoặc e như (2.5e2 = 2.5 x 102 = 250).

Một số hàm toán học cơ bản trong module Math:
|Hàm| Chức năng|
|---|----------|
|abs(x)|Trị tuyệt đối của x|
|ceil(x)|Số nguyên nhỏ nhất mà không nhỏ hơn x|
|fabs(x)|Giá trị tuyệt đối của x|
|floor(x)|làm tròn trả về số nguyên lớn nhất mà không lớn hơn x|
|max(x1, x2,...)|Trả về số lớn nhất|
|min(x1, x2,...)|Trả về số nhỏ nhất|
|modf(x)|Trả về phần nguyên và phần thập phân của x. Cả hai phần có cùng dấu với x và phần nguyên được trả về dưới dạng một số thực|
|pow(x, y)|Trả về giá trị của x**y.|
|round(x [,n])|Làm tròn x về n chữ số sau dấu thập phân. Python làm tròn theo cách sau: round(0.5) là 1.0 và round(-0.5) là -1.0|
|sqrt(x)|Trả về căn bậc hai của x, với x > 0|

Một số hàm xử lý random
|Hàm| Chức năng|
|---|----------|
|choice(seq)|Một item ngẫu nhiên trong một list, tuple, hoặc một string|
|randrange ([start,] stop [,step])|Một phần tử được lựa chọn một cách ngẫu nhiên từ dãy (start, stop, step)|
|random()|Một số thực ngẫu nhiên r trong dãy 0>= r >1|
|seed([x])|Thiết lập giá trị nguyên bắt đầu mà được sử đụng trong bộ sinh số ngẫu nhiên. Bạn nên gọi hàm này trước khi gọi bất cứ hàm ngẫu nhiên nào khác. Hàm này trả về None|
|shuffle(lst)|Sắp xếp các item trong list một cách ngẫu nhiên|
|uniform(x, y)|Một số thực ngẫu nhiên r trong dãy x>= r >y|


