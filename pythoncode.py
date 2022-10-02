#question 1
class vehicle:
    def __init__(self,brand_name,model,colour,price):
        self.brand_name = brand_name
        self.model = model
        self.colour = colour
        self.price = price
    def specs(self):
        print("brand_name:",self.brand_name)
        print("model:",self.model)
        print("colour:",self.colour)
        print("price:" ,self.price)
a1=vehicle("Mc Laren Automotive","P1","yellow","1.3cr")
a2=vehicle("BMW Automotive","i8","white","2.62cr")
a3=vehicle("Mercedez benz","G class","black","1.64cr")

a1.specs()
a2.specs()
a3.specs()
