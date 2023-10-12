#super class
class Shape:
    #attributes and method definition
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
#inheritance
class Circle(Shape):
    #attribute and metod of super_class
    def __init__(self, x, y, size):
        #call superclass
        super().__init__(x, y, size)
        
    def shape(self):
        return "This is a circle"
    
    def draw(self): 
        return f"""
    ({self.x}, {self.y})\n{self.size}
        , - ~ ~ ~ - ,
    , '               ' , 
  ,                       , 
 ,                         , 
,                           ,  
,                           , 
,                           ,
 ,                         , 
  ,                       ,
   ,                    ,
    ' -  , _  _  _  , '
              """
   
              
def main():
    c = Circle(1,2,3) 
    print(c.shape()) 
    print(c.draw())

if __name__ == '__main__':
    main()

      




