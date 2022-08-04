import pickle

class Vehiculo:
    marca=''
    placa=''

    def __init__(self,marca,placa):
        self.marca=marca
        self.placa=placa
    def getMarca(self):
        return self.marca
v=Vehiculo('Aveo','AJ123')

datos=open('d.bin','wb')
pickle.dump(v,datos)
datos.close()

datos=open('d.bin','rb')
p=pickle.load(datos)
datos.close()

print(p.getMarca(),p.placa)










