price = [0.0920, 0.0709]
price_tax = [0.0927, 0.0574]

taxes = [0.0362, 0.001926, 0.003474, 0.00075, 0.0281]

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
print("Already paid: 4592,74 €")
print("Total to pay: " + str((int((result[0]*1.21)*100)/100) - 4592.74) + " €")
