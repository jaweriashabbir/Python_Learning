e_mail = 'jaweria.malik+shabbir@gmail.com'
out = ''
COM = '@gmail.com'
for i in range(0, len(e_mail)):
    iteration = e_mail[i]
    if iteration == '+':
        break
    elif iteration == '@':
        break
    elif iteration != '.':
        out = out + iteration
print(out + COM)
