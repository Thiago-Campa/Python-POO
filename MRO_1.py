class A:
    def hablar(self):
        print("Hola desde A")
        
class J:
    def hablar(self):
        print("Hola desde J")
        
class B(A):
    pass

class C(B,J):
    pass
        
class G(B,A):
    pass

g = G()

g.hablar() 