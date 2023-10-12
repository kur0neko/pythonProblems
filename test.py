from print_caps import allcaps

@allcaps
def greet():
    return "hello World!"

def main(): 
    msg=greet()
    print(msg)
main()
