f = 'fizz'
b = 'buzz'


def check_fizz(num):
    if(num % 3 == 0):
        print(f)
        
def check_buzz(num):
    if(num % 5 == 0):
        print(b)
        
for i in range(46):
    print(i)
    check_fizz(i)
    check_buzz(i)