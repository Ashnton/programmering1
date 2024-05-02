class Animal:
    def __init__(self, namn, färg, ålder):
        self.namn = namn
        self.färg = färg
        self.ålder = ålder 
        
    def visa_egenskaper(self):
        print("Djuret heter:", self.namn)
        print("Djurets färg är:", self.färg)
        print("Djurets ålder är:", self.ålder, "år")
    
horse = Animal("häst", "brun", 15)
cat = Animal("katt", "svart", 4)
dog = Animal("hund", "vit", 6)

horse.visa_egenskaper()
cat.visa_egenskaper()
dog.visa_egenskaper()