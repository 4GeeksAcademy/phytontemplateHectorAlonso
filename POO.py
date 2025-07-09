
class Persona:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def incrementar_edad(self):
        self.age += 1

persona1 = Persona("hector", 34)
persona2 = Persona("hori", 25)

print(persona1.name, persona1.age)
print(persona2.name, persona2.age)

persona1.incrementar_edad()

###########################################
# herencia

class Animal:
    def __init__(self, name):
        self. name = name

    #polimorfismo
        def ruido(self):
            print(f{self.name}, hace ruido...)

    class Perro(Animal):
        def ruido (self):
            print("guau guau")


perro = Perro("Neo")
jirafa = Animal("Sr jirafa")


#Encapsulamiento
class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo 

    def ver_saldo(self):
        return(self.__saldo)

cuenta = CuentaBancaria("pepe", 1000)

print(cuenta.ver_saldo)