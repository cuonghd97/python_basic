# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    #(1)Iterable object laf 1 object co kha nang lay ra rung phan tu
    #tuong tu nhu List va Dict
    #iter su dung phong thuc next() de la ra cac phan tu
    it=iter([1,2,3])
    print(next(it),next(it),next(it))
    #(2)ham ho tro iterable object
    # sum, min, max, sorted
    it1=iter([1,5,8,2,7,3,4])
    print(sorted(it1,reverse=True))