class operation:
    def v(self,x,y):
        pass
class add(operation):
    def v(self,x,y):
        return x+y
class power(operation):
    def v(self,x,y):
        return x**y
rr=[add(),power()]
for i in rr:
    print(i.v(3,3))
    
