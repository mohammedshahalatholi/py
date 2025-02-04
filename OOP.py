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

    def indro(self):
        print("Its intro")

class var:
    a=10

class tmp:
    def tests(self):
        print("lets test")

    b=12

obj=app(10,"hello")

obj.cls1("hiiiii")

obj.cls2()

varobj=var

varobj.a
print(varobj)

print(varobj.a)

obj.indro()

tess=tmp()

tess.tests()

print(tess.b)