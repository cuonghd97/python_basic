# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
if __name__ == "__main__":
#    #(1) mo,dong , doc va ghi file
#    # mac dich se ma mo file de doc
#    # r va  mo ra de doc
#    # w va  mo ra de ghi de
#    # a va  mo ra de ghi tiep
#    f1=open('Text.txt','r')
#    f2=open('Text.txt')
#    f3=open('Text.txt')
#    print(f1.read(20))
##    sau khi doc 20 ky tu con tro se tro tai do
##    su dung read(5) se doc tiep 5ky tu tiep theo
#    print(f1.read())
#    print(f1.readline())
#    print(f1.readlines())
#    ls1=list(f2)
#    print(ls1)
#    tp1=tuple(f3)
#    print(tp1)
#    #(2)kiem soat con tro file voi seek()
#    #seek(4) dua con tro den vi tri thu 4
#    f1.close()
#    f2.close()
#    f3.close()
    #(3) mo file su dung cau lenh with
    with open('Text.txt') as fO:
        print(fO.read())
    #khi ket thuc khoi lenh with file se tu dong dong
    