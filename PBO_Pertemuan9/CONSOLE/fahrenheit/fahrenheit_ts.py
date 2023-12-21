print("Konversi suhu Fahrenheit ke Kelvin, Reamur, dan Celsius")

# Input
suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))

# Formulas
K = (5/9 * (suhu_fahrenheit - 32)) 
R = (4/9 * (suhu_fahrenheit - 32))
C =(5/9 * (suhu_fahrenheit -32) + 273)

# Output
print(str(suhu_fahrenheit) + " Fahrenheit sama dengan:")
print(str(K) + " Kelvin")
print(str(R) + " Reamur")
print(str(C) + " Celsius")
