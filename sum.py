def jumlah_total(nilai):
    z = 0
    x = nilai
    jml = len(x)

    for i in range(jml):
        y = x[i]
        z +=y
        return z

nilai = [10, 9, 8, 9, 10, 8, 8]
jml_total = (sum(nilai))

print(jml_total)
