print("Konversi Suhu Reamur")

def get_fahrenheit(suhu):
    return (9/4 * float(suhu) + 32)

def get_celsius(suhu):
    return (5/4 * float(suhu))

def get_kelvin(suhu):
    return (5/4 * float(suhu) + 273)

# Input
suhu_reamur = input("Masukkan suhu dalam Reamur: ")

# Formulas
F = get_fahrenheit(suhu_reamur)
C = get_celsius(suhu_reamur)
K = get_kelvin(suhu_reamur)

# Output
print(suhu_reamur + " Reamur sama dengan ")
print(str(F) + " Fahrenheit")
print(str(C) + " Celsius")
print(str(K) + " Kelvin")
