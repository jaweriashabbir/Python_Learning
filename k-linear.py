haystack = 'jaweria shabbir'
needle = 'shabbir'
checker = ''
condition = True
index = -1
# y = len(haystack)-1
for i in range(0, len(haystack)):
    for j in range(len(needle)):
        try:
            checker = checker + haystack[i + j]
            if checker == needle:
                index = i
                condition = False
        except:
            pass
    if condition == False:
        break
    checker = ''
print(index)






