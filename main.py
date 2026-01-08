class  Mark :
    def __init__(self,name, m1 , m2 , m3 ):
        self.name = name 
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avrage_print(self):
        avg = (self.m1 + self.m2 + self.m3 ) / 3
        print(f"{self.name} your 3 subject avrage is",avg)
        
marks = Mark("Xavir", 45, 85, 96)
marks.avrage_print()
