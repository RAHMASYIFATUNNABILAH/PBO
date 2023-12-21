print("Konversi Suhu Kelvin")

def get_fahrenheit(suhu):
    F = (9/5 * (float(suhu) - 273)) + 32
    return F

def get_reamur(suhu):
    R = (4/5 * (float(suhu) - 273))   
    return R

def get_celsius(suhu):
    C = float(suhu) - 273
    return C

# Entry
suhu_kelvin = input("Masukkan suhu dalam Kelvin: ")

# Rumus
F = get_fahrenheit(suhu_kelvin)
R = get_reamur(suhu_kelvin)
C = get_celsius(suhu_kelvin)

# Output
print(suhu_kelvin + " Kelvin sama dengan ")
print(str(F) + " Fahrenheit")
print(str(R) + " Reamur")
print(str(C) + " Celsius")
