print(type(15 * 3))
print(type(15 / 3))
print(type(15 // 2))
print(type(15 ** 2))
######
weather = "'v', '4', '23', 'minutes', 'temperature', 'air', 'was', '-3', 'degrees'"
print(weather[-1])
print(type(weather[1:9]))
print(weather[2:14])
print(weather.split(';'))
print(weather)
print(len(weather))
#print(weather.find())
print(weather.isdigit())
print(weather.upper())
####
my_list_1 = ['v', '4', '23', 'minutes', 'temperature', 'air', 'was', '-3', 'degrees']
print(type(my_list_1))
print(my_list_1[3])
print(my_list_1[1:5])
len(my_list_1)
#my_list_1.insert(2, '04')
#my_list_1.remove('4')
#my_list_1.remove('-3')
my_list_1[2] = '04'
my_list_1[8] = '-03'
my_list_1.pop(2)

#my_list_1.insert(8,'-03')

print(my_list_1)



############
my_list = ['design-engineer Igor', 'chief accountant MARINA', 'high-grade turner nICOLAI', 'director aelita']
str  = "'design-engineer Igor', 'chief accountant MARINA', 'high-grade turner nICOLAI', 'director aelita'"
print( 'Privet', my_list[0])
print('Hy',my_list[2])
print('hy', my_list[1])
print('Hy', my_list[3])
#str.lower()

#str.upper()
str_1 = 'MARINA'
print(str_1.capitalize())
str_2 = 'nICOLAI'
print(str_2.capitalize())
str_3 = 'aelita'
print(str_3.capitalize())
#str.title('design-engineer Igor')
