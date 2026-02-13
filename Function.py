def greet():
    print("Hello!")

def greetUser(name):
    print("Hello! " + name)

def add(a,b):
    return (a + b)


greet()
greetUser("Gokul")
greetUser("Manoj")
value = add(1,2)
value1 = add(3,value)

print(value1)
def sub(a,b):
 return (a-b)

mark1=sub(33,43)
mark2=sub(10,mark1)


def div(c,d):
  print (c/d)
def multi(e,f):
  print(e*f)
print(mark2)
div(10,77)
multi(98376,5)




fruits = ["apple", 'carrot', "cherry","banana"]
for x in fruits:
  if x == "banana":
    break
  print(x) 



class car:
    def __init__ (self,tyre4,light2):
        self.tyre4= tyre4
        self.light2=light2
    def greet(self):
        
       print('toyoto has',self.tyre4,'tyres and',self.light2,'light','and its a sydon baded model')

suzhuki= car(4,2)
suzhuki.greet()






class car1:
    def __init__ (self,model,name):
     self.model=model
     self.name=name
    def greet (self):
     print (self.name,self.model,'has 4 tyres and 2 light with inbuild airbag')
nissan =car1('hatchbag','toyoto')
nissan.greet()
    
