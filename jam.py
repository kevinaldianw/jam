print("Masukkan Jam(0-23):")
jam = int(input())
print("Masukkan Menit(0-59):")
menit = int(input())
print("Masukkan Tambahan Menit(bebas):")
tambahan = int(input())

bagi = tambahan/60
modulo = tambahan%60

menit = menit + modulo
jam = jam + bagi

if(menit >= 60):
    menit = menit - 60
    jam = jam + 1


while(jam>=24):
    jam = jam - 24

print("Hasil:",int(jam),":",int(menit))
