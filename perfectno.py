perfect_no = 6
output = 0
x = ''
for i in range(1, perfect_no):
    # print(f"{perfect_no}/{i} = {perfect_no/i}")
    if perfect_no % i == 0:
        output = output + i
        if output == perfect_no:
            x = 'yes'
        else:
            x = 'no. this is no perfect no.'
print(x)
# 6, 28, 496, 8128, and 33550336.


