immutable_var = (1,'privet',True,[0,1,0,1]) #Почему то такой вариант immutable_var = tuple(1,'privet',True,[0,1,0,1]) не работает
print(type(immutable_var))
print(immutable_var)
immutable_var1 = tuple([1,'privet',True,[0,1,0,1]])#Кажется его надо было выделить в квадратные скобки
print(immutable_var1)
#immutable_var1[0]=15
#print(immutable_var1) #We cant change the elements in the tuple because its data type is unchanged
#Программа остановилась на этом этапе, я ее захеширую

mutable_list = [1,000,142,-13]+[52,'Кириешки']
print(type(mutable_list))
print(mutable_list)
print(mutable_list[1::2])
List_2 = mutable_list[1::2]
print(List_2)
List_2[0] = 1
print(List_2)
List_2.remove(-13)
List_2.extend(['хочу','сейчас'])
List_2.append('Пока')
print(List_2)
