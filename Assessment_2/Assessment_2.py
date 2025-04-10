class employee: 
    def __init__(self, name, sal): 
        self._name=name # private attribute; use two underscores 
        self._salary=sal
class engineer(employee): 
    def info(self): 
        print('{}: salary is {}'.format(self._name, self._salary)) 

person = engineer('Bob', 4000) 
person.info()