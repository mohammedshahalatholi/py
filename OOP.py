class app:
    def __init__(self,a,b):
        print("its consector",a)
        self.a=a
        self.b=b
    def cls1(self,h):
        print(h)
        print("hi object 1",h,"and value from consector",self.a)

    def cls2(self):
        print(self.a)
        print("its b",self.b)


obj=app(10,"hello")

obj.cls1("hiiiii")

obj.cls2()



class var:
    a=10


varobj=var

varobj.a

print(varobj)

print(varobj.a)