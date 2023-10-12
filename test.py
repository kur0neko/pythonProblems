#from print_caps import allcaps

#@allcaps
#def greet():
    #return "hello World!"

#def main(): 
    #msg=greet()
   # print(msg)
#main()
from log import timestamp

@timestamp
def hi(): 
    print('hi')


def main(): 
    hi()
    
main()


