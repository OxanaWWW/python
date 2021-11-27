"+".join(['r', 'ty', '56', 'temperature'])
my_list = ['v', '4', '23', 'minutes', 'temperature', 'air', 'was', '-3', 'degrees']
new_list = []
for i in my_list:
    if i.replace("-", ""). isdigit():
        if i.isdigit():
            new_list.append(f"'{int(i):02}'")
        else:
            new_list.append(f"'{i[0]}{int(i):02}'")
    else:
        new_list.append(i)
print(new_list)
print(" ".join(new_list))


my_list = ['design-engineer Igor', 'chief accountant MARINA', 'high-grade turner nICOLAI', 'director aelita']
for i in my_list:
    if i[-1].capitalize():
        print('Hi',(i))
    else:
        my_list.insert(i[-1]).capitalize()
print('Hy'(i))



my_list = ['v', '4', '23', 'minutes', 'temperature', 'air', 'was', '-3', 'degrees']
for i, v in enumerate(my_list)
    if "m" in v:
        my_list[i] = f"'{v}'"
print(my_list)