#super class
class Base:
    #attributes and method definition
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
#inheritance
class Circle(Base):
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
    c = Circle(1,4,3) 
    print(c.shape()) 
    print(c.draw())

main()

      




