#### `if __name__ == '__main__':`

Ta có một file `file1.py` như sau:
```
import file2

if __name__ == '__main__':
  print('Hello wolrd')
```

và `file2.py`:
```
print('123')
if __name__ == '__main__':
  print('Hoho')
```

- khi run `file1.py` thì thuộc tính `__name__` của module file1 sẽ được gán bằng `'__main__'` và các thuộc tính `__name__` của các module import vào sẽ gán bằng tên của module đó file2 sẽ gán bằng `'file2'`. 
- câu lệnh `import file2` trong `file1.py` sẽ thực thi tất cả các câu lệnh trong module file2 ngoại trừ khối `if __name__ == '__main__':` vì lúc này `__name__` của file2 là `'file2'` như vậy kết quả khi chạy `file1.py` sẽ ra là
```
Hello world
123
```

