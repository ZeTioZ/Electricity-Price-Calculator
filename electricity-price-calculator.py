# Premier prix: Prix au kWh (jour) en €
# Deuxième prix: Prix au kWh (nuit) en €
price = [0.0869, 0.0587]

# Première taxe: Frais de distribution au kWh (jour) en €
# Deuxième taxe: Frais de distribution au kWh (nuit) en €
price_tax = [0.1016, 0.0628]

# Première taxe: Frais de transport au kWh en €
# Deuxième taxe: Cotisation sur l'énergie au kWh en €
# Troisième taxe: Cotisation fédérale au kWh en €
# Quatrième taxe: Redevance de raccordement au kWh en Wallonie en €
# Cinquième taxe: Certificats verts au kWh en Wallonie en €
taxes = [0.0344, 0.001926, 0.003386, 0.00075, 0.0261]

# Montant d'électricité déjà payé d'après les relevés de factures
already_paid = 4592.74

# Première valeure: Montant de kWh consommés de jour
# Deuxième valeure: Montant de kWh consommés de nuit
kwh = [11951, 12341]

def calculate_price(electricity):
	result = 0
	day = 0
	night = 0
	for i in range(0, 2):
		result += price[i] * electricity[i]
		result += price_tax[i] * electricity[i]

		for tax in taxes:
			result += tax * electricity[i]
		if i == 0:
			day = result
		else:
			night = result - day
	return [int(result * 100)/100, int(day * 100)/100, int(night * 100)/100]

result = calculate_price(kwh);

print("Day H.T.V.A: " + str(result[1]) + " €")
print("Night H.T.V.A: " + str(result[2]) + " €")
print("Total H.T.V.A: " + str(result[0]) + " €")
print("------------------------------------")
print("Day T.V.A: " + str(int((result[1]*1.21)*100)/100) + " €")
print("Night T.V.A: " + str(int((result[2]*1.21)*100)/100) + " €")
print("Total T.V.A: " + str(int((result[0]*1.21)*100)/100) + " €")
print("------------------------------------")
print("Already paid: " + str(already_paid) + " €")
print("Total to pay: " + str((int((result[0]*1.21)*100)/100) - already_paid) + " €")
