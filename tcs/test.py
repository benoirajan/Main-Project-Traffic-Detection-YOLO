class Employee:
    def __init__(self,name,des,sal,ot): 
        self.name = name 
        self.des = des 
        self.sal=sal 
        self.ot = ot 
        self.os = False 

    def p(self):
        return "{} {}".format(self.name,self.os)

def isEl(emp,thresh):
    for e in emp:
        ott = 0
        for ot in e.ot.values():
            ott += ot
        if ott >= thresh:
            e.os = True

def urate(emp,rph):
    ott=0
    for e in emp:
        if e.os:
            for ot in e.ot.values():
                ott += ot
    return ott*rph

# e = Employee("Kala","pani",2093,{"mar":4})
# print(e.p())
# e2 = Employee("Kala","pani",2093,{"mar":5})
# k = [e,e2]
# isEl(k,4)

# print(urate(k,2))
# exit(0)
ol = []

n  = int(input())
for i in range(n):
    nme = input()
    des = input()
    sal = float(input())
    ot = dict()
    for k in range(int(input())):
        m = input()
        ot[m]=float(input())

    ol.append(Employee(nme,des,sal,ot))


isEl(ol,int(input()))
for e in ol:
    print(e.p())

print(urate(ol,int(input())))