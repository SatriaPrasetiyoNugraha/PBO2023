import math
print("Menghitung Luas Dan Volume Tabung")

# variabel
jari_jari = 7
tinggi = 10

# rumus luas selimut tabung
luas_ST = 2 * math.pi * jari_jari * tinggi

# Rumus luas permukaan tabung
luas_PT = (2 * math.pi * jari_jari * tinggi) + \
    2 * math.pi * jari_jari * jari_jari
# Menghitung volume tabung
volume_tabung = math.pi * jari_jari * jari_jari * tinggi

# output
print(f"Luas selimut tabung adalah: {luas_ST}")
print(f"Luas permukaan tabung adalah: {luas_PT}")
print(f"Volume tabung adalah: {volume_tabung}")
