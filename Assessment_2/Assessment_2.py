class employee: 
    def __init__(self, name, sal): 
        self.__name=name # private attribute; use two underscores 
        self.__salary=sal
class engineer(employee): 
    def info(self): 
        print('{}: salary is {}'.format(self.__name, self.__salary)) 

person = engineer('Bob', 4000) 
person.info()