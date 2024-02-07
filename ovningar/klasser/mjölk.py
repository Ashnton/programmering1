# Klass för att skapa kunder och hålla koll på köp
class Kund:
    # Funktion för att definiera ny kund i systemet med nödvändig information
    def __init__(self, namn):
        self.namn = namn
        self.produkter = []
        self.ska_betala = 0
        
    def lägg_till_produkt(self, produkt, antal):
        # Lägg till produkten och antalet som köpts i kundens lista av produkter
        self.produkter.append((produkt, antal))
        
    def hämta_produkter(self):
        # Returnera en sträng som innehåller information om kundens produkter och antal
        return '\n'.join([f"{produkt.visa_mjölkinfo()} (Antal i kundkorgen: {antal})" for produkt, antal in self.produkter])
        
    def ändra_ska_betala(self, ändring):
        self.ska_betala += ändring

# Klass för att skapa mjölkpaket
class Mjölkpaket:
    # Funktion för att definiera ett nytt mjölkpaket
    def __init__(self, typ, storlek, pris, antal):
        self.typ = typ
        self.storlek = storlek
        self.pris = int(pris.split()[0])  # Konverterar priset till ett heltal
        self.antal = antal
        
    # Visar all information tillgänglig om en viss instans av klassen i ett snyggt format
    def visa_mjölkinfo(self):
        return 'Typ: {} \nStorlek: {} \nPris: {} kr \nAntal: {}'.format(self.typ, self.storlek, self.pris, self.antal)

    def ändra_antal(self, minskat_antal):
        if ((self.antal - minskat_antal) < 0):
            return False
        else:
            self.antal -= minskat_antal
            return True

    def hämta_pris(self):
        return self.pris

# Programmets huvudfunktion
def main(mjölkkylen):
    # Låter användaren skapa sin kundprofil
    kund = Kund(input('Vad heter du? '))
    
    while True:
        kommando = input('Vad vill du göra? ')
        if kommando == "Visa mjölkpaket":
            # Loopar igenom alla mjölkpaket i kylen för att visa för användaren vad som finns tillgängligt
            for mjölk in mjölkkylen:
                print(mjölk.visa_mjölkinfo())

            # Frågar användaren vilket mjölkpaket den vill köpa
            köpa_mjölk = input('Vilket mjölkpaket vill du köpa? (Lätt, Mellan, Standard) ')
            antal_mjölk = int(input('Hur många paket vill du ha? '))
            for mjölk in mjölkkylen:
                if mjölk.typ.lower() == köpa_mjölk.lower():
                    if mjölk.ändra_antal(antal_mjölk):
                        kund.lägg_till_produkt(mjölk, antal_mjölk)  # Lägg till produkten med antalet som köpts
                        kund.ändra_ska_betala(mjölk.hämta_pris() * antal_mjölk)
                        break
                    else:
                        print("Det finns inte tillräckligt med", mjölk.typ, "mjölk tillgänglig.")
                        break
            else:
                print("Ogiltig mjölktyp.")

        elif kommando == "Visa kundkorgen":
            print(kund.hämta_produkter())

# Definierar mjölkpaketen innan programmet körs
lättmjölk = Mjölkpaket('Lätt', '1l', '19 kr', 3)
mellanmjölk = Mjölkpaket('Mellan', '1l', '19 kr', 5)
standardmjölk = Mjölkpaket('Standard', '1l', '19 kr', 4)

# Lista för att spara våra definierade objekt
mjölkkylen = [lättmjölk, mellanmjölk, standardmjölk]

main(mjölkkylen)
