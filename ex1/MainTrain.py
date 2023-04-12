from parser import *
import random
import string

a = Num(random.randint(-100,100))
b = Num(random.randint(-100,100))
c = Num(random.randint(-100,100))
d = Num(random.randint(-100,100))

# print (a.num,b.num,c.num,d.num)

# a = Num(41)
# b = Num(41)
# c = Num(90)
# d = Num(-50)


# a = Num(15)
# b = Num(7)
# c = Num(-16)
# d = Num(27)


if Plus(a,b).calc() != a.calc()+b.calc():
    print("problem with Plus (-10)")

if Minus(a,b).calc() != a.calc()-b.calc():
    print("problem with Minus (-10)")

if Mul(a,b).calc() != a.calc()*b.calc():
    print("problem with Mul (-10)")

x = Div(a,b).calc()
if x > a.calc()/b.calc()+0.01 or x < a.calc()/b.calc()-0.01:
    print("problem with Div (-10)")

if Plus(a,Mul(b,Minus(c,d))).calc() != a.calc()+b.calc()*(c.calc()-d.calc()) :
    print("problem with expression (-10)")


def strf(x) -> string:
    s=str(x)
    if s.startswith('-'):
        s="("+s+")"
    return s

sa = strf(a.calc())
sb = strf(b.calc())
sc = strf(c.calc())
sd = strf(d.calc())

s = sa+'+'+sb+'*('+sc+'-'+sd+')'
# print (s)
# print (ShuntingYardAlgorithm(s))
# print (f"need to calculate:\n{eval(s)}")
# print (f"Actually calculates:\n{parser(s)}")
if parser(s) != eval(s) :
    print("problem with parser (-20)")
if parser(s) != eval(s) :
    print("problem with parser (-10)")


s = sa+'*'+sa+'+'+sb+'*('+sc+'-'+sd+'+'+sb+')'
# print (s)
# print (ShuntingYardAlgorithm(s))
# print (f"need to calculate:\n{eval(s)}")
# print (f"Actually calculates:\n{parser(s)}")
if parser(s) != eval(s) :
    print("problem with parser (-20)")

s = sa+'*('+sa+'+'+sb+'*('+sc+'-'+sd+'+'+sb+'))'
# print (s)
# print (ShuntingYardAlgorithm(s))
# print (f"need to calculate:\n{eval(s)}")
# print (f"Actually calculates:\n{parser(s)}")
if parser(s) != eval(s) :
    print("problem with parser (-20)")


print("done")