

def smart_sub(fn):

    def inner_fun(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)

    return inner_fun

@smart_sub
def add(n1,n2):

    return n1+n2

@smart_sub
def sub(n1,n2):
    return n1-n2

print(add(10,20))