def asal(x):
    for i in range(2, x-1, 1):
        kalan = x % i
        if kalan == 0:
            return 0
    return 1

def chenIkıAsalinCarpimi(y):
    for k in range(2, y-4, 1):
        if y % k == 0:
            if asal(int(y/k)):
                if asal(k):
                    print("Asal çarpanlar = {}, {}  ".format(k, y/k))
                    return 1
    return 0

toplam = 0

for j in range(2, 100000, 1):
    if asal(j):
        if asal(j+2):
            toplam = toplam + 1
            print("Direk : {}\n".format(j))
        elif chenIkıAsalinCarpimi(j+2):
            toplam = toplam + 1
            print("Bölümünden : {}\n".format(j))

print(toplam)