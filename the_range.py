#range
for x in range(10):
  print(x)

print('---------------')


###map
numbers = [1,2,3,4,5,6]
result_map = map(lambda x : x*x , numbers)
print(list(result_map))

print('-------------')


#filter
programming = ['Python','Csharp','C++','C','java']
pro = filter(lambda p:p.startswith('C'),programming)
print(list(pro))

print('------------------')



#zip
names = ['mohamed','elsayed','ali']
degrees = [10,20,30]
final = zip(names,degrees)
print(list(final))