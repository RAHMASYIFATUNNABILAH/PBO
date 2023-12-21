class Reamur:
    def __init__(self, suhu):
        self.suhu = suhu
    
    def get_reamur(self):
        val = self.suhu
        return val
    
    def get_fahrenheit(self):
        val = (9/4 * self.suhu) + 32
        return val
    
    def get_celsius(self):
        val = (5/4 * self.suhu)
        return val

    def get_kelvin(self):
        val = (5/4 * self.suhu) + 273
        return val

suhu_reamur = float(input("Masukkan suhu dalam Reamur: "))
R = Reamur(suhu_reamur)
val = R.get_reamur()

F = R.get_fahrenheit()
C = R.get_celsius()
K = R.get_kelvin()

print(str(val) + " Reamur, sama dengan:")
print(str(F) + " Fahrenheit")
print(str(C) + " Celsius")
print(str(K) + " Kelvin")
