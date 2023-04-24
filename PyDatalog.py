from pyDatalog import pyDatalog

def Factorial(X):
    res = 1
    for i in range(X,1,-1):
        res *= i
    return res

pyDatalog.create_terms('X,Y,Factorial')

print ((X==4) & (Y == Factorial(X)))
