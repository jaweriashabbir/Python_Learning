no1 = 20
no2 = 98
out = 0
def greater(x,y):
    if x > y:
        return x
    elif x < y:
        return y
def smaller(y,x):
    if y < x:
        return y
    elif y > x:
        return x
greaterno = greater(no1, no2)
smallerno = smaller(no2, no1)
while True:
    z = greaterno % smallerno
    greaterno = smallerno
    smallerno = z
    if z == 0:
        break
    out = z
print(out)
