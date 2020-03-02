'''lambda function'''
remainder=lambda num: num% 2
#print(remainder(5))

product=lambda x,y: x*y
#print(product(2,3))

def testfunc(num):
    return lambda x: x*num
result1=testfunc(10)
result2=testfunc(1000)
#print(result1(9))
#print(result2(9))

def myfunc(n):
    return lambda a: a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)
#print(mydoubler(11))
#print(mytripler(11))

'''filtered list'''
num_list=[2,6,8,10,11,4,12,7,13,0,21]
filtered_list=list(filter(lambda num:(num>7),num_list)) #create a filter that remain those only larger than 7
#print(filtered_list)

'''mapped list'''
mapped_list=list(map(lambda num:num%2,filtered_list)) #create a list that contians all the remainder devided by 2
print(mapped_list)