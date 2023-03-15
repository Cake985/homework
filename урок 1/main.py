suruna = float(input())
vusota = float(input())
rasxod = int(input())
obuem = int(input())
prozent = int(input())
plochad = suruna*vusota
litrs = (plochad/rasxod)*1.2
kollich = (litrs//obuem) + 1
ostatok = kollich*rasxod - litrs
print(round(plochad,2))
print(round(litrs,2))
print(kollich)
print(ostatok)