#calculator.py

def sum(m,n):
    for x in range(n):
        m=m+1
    return m

def divide(m,n):
    try:
        if(n<=0):
            raise Exception("can't divide by zero")
    except:
        return "cannot divide by zero"
    result=0
    while m-n>=0:
        result=result+1
        m=m-n
    return result

