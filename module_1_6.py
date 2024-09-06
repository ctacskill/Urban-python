my_dict = {'Dmitriy':2003,'Sasha':2006,'Galya':2005,'Emil':2000}
print('Dict:',my_dict)
print('Existing value:',my_dict.get('Dmitriy'))
print('Not existing value:',my_dict.get('Alexandr'))
my_dict.update({'Alexandr': 2006,'Vasya':1999})
a = my_dict.pop('Dmitriy')
print('Deleted value:',a)
print('Modified dictionary:',my_dict)

my_set = {1,'Ctac','Ctac',True,(1,2,3),1,1,1}
print('Set:',my_set)
my_set.add('stick')
my_set.add(52)
my_set.remove('Ctac')
print('modified set:',my_set)
