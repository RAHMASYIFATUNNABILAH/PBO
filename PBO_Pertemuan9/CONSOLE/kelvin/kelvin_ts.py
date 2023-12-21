print("Konversi suhu Kelvin ke Fahrenheit, Reamur, dan Celsius")

# Input
suhu_kelvin = float(input("Masukkan suhu dalam Kelvin: "))

# Formulas
F = (9/5 * (suhu_kelvin - 273)) + 32
R = (4/5 * (suhu_kelvin - 273))
C = suhu_kelvin - 273

# Output
print(str(suhu_kelvin) + " Kelvin sama dengan:")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(C) + " Celsius")
