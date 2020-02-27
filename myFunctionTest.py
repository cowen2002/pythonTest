' my function test code'
__author__ = 'kuang wei'
'''this code is testing for function'''

#avg function can accept multiple number
def avg(*num):   #as a tuple
    sum = 0
    count = 0
    for n in num:
        sum = sum+n
        count+=1
    return sum/count
    
#this function can accept any parameter
def func1(**kwargs):   #as a dict
    for key, value in kwargs.items():
        print(key,'=',value)
        




if __name__ == '__main__':
    print(avg(1,2,3,4,5,6))
    func1(key1='hello', key2='world', key3=3)
