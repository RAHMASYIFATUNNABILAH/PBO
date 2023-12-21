print("Konversi suhu Reamur ke Fahrenheit, Celsius, dan Kelvin")

# Input
suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))

# Formulas
F = (9/4 * suhu_reamur) + 32
C = (5/4 * suhu_reamur)
K = (5/4 * suhu_reamur) + 273

# Output
print(str(suhu_reamur) + " Reamur sama dengan:")
print(str(F) + " Fahrenheit")
print(str(C) + " Celsius")
print(str(K) + " Kelvin")
