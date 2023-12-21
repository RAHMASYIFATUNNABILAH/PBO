print("Konversi Suhu Fahrenheit")

def get_celsius(suhu):
    C = (5/9 * (float(suhu) - 32))
    return C

def get_reamur(suhu):
    R = (4/9 * (float(suhu) - 32))   
    return R

def get_kelvin(suhu):
    K =(5/9 * (float(suhu) - 32) + 273)
    return K

# Entry
suhu_fahrenheit = input("Masukkan suhu dalam Fahrenheit: ")

# Rumus
C = get_celsius(suhu_fahrenheit)
R = get_reamur(suhu_fahrenheit)
K = get_kelvin(suhu_fahrenheit)

# Output
print(suhu_fahrenheit + " Fahrenheit sama dengan ")
print(str(C) + " Celcius")
print(str(R) + " Reamur")
print(str(K) + " Kelvin")
