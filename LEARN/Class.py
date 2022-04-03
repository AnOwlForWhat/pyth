class Person:
    def __init__(self, name, age ,gender, national):
        self.name = name
        self.age = age
        self.national = national
        self.gender = gender

P = Person("anowlforwhat",4,"male","OWL_WORLD")

print('and his name is',P.name,'!!!!')
print('his was',P.age,'years old')
print('his in',P.national)
print(P.gender)
 
 