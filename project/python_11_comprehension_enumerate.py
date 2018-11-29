# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    #(1)Comprehension
    #cu phap [ output-expression for-statement optional-predicate ]
    tong=0
    [print(x) for x in range(10)]
    #(2) enumerate
    #cu phap enumerate(iterable[, start])
    student_list=["he","ha","hi","ho"]
    for a,b in enumerate(student_list,1):
        print(a,":",b)
        
