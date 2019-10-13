#! /usr/bin/python3



# properse:
# to deme named paramenter as func call 


def mult(a, b, c):
    __ = a * b * c
    print(__)
    return __


def show(*args, **kwargs):
    print(locals())
    

if __name__ == '__main__':

    # pass dict
    __ = {'a': 3,
          'b': 5,
          'c': 7,}

    assert(mult(**__) == (3 * 5 * 7))

    show(**__)
    show(a = 3, b = 5, c = 7)
    show(3, 5, 7)

    

    
    
