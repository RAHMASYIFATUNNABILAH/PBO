print("Konversi Suhu Celcius")

def get_reamur(suhu):
    return (4/5 * float(suhu))

def get_fahrenheit(suhu):
    return (9/5 * float(suhu) + 32)

def get_kelvin(suhu):
    return (float(suhu) + 273)

# Input
suhu_celcius = input("Masukkan suhu dalam Celcius: ")

# Formulas
R = get_reamur(suhu_celcius)
F = get_fahrenheit(suhu_celcius)
K = get_kelvin(suhu_celcius)

# Output
print(suhu_celcius + " Celcius sama dengan ")
print(str(R) + " Reamur")
print(str(F) + " Fahrenheit")
print(str(K) + " Kelvin")
