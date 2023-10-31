class Motorcycle: 

    #Atributo de clase
    worth = "Nueva"
    engine= False

    #Atributos de instancia 
    def __init__(self,color,tuition,fuel_liters,number_wheels,brand,model,fabrication_date,top_speed,weigth):
        self.color= color
        self.tuition= tuition
        self.fuel_liters= fuel_liters
        self.number_wheels= number_wheels
        self.brand= brand
        self.model= model
        self.fabrication_date= fabrication_date
        self.top_speed= top_speed
        self.weigth= weigth

    def pull(self):
        if self.engine == True:
            print(f"El ya estaba en marcha")
        else:
            print(f"El motor ha arrancado")

    def stop(self):
        if self.engine == False:
            print(f"El motor ya estaba detenido")
        else:
            print(f"El motor se ha detenido")   
    def consult(self):
        print(f'El precio de la motocicleta {self.brand} {self.model} es de {self.price} $')         