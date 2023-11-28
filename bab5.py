def konversiIpk(ipk):
    if ipk >= 80:
        ipk = "A"
        # elif = ElseIf
    elif ipk >= 60:
        ipk = "B"
    elif ipk >= 40:
        ipk = "C"
    else:
        ipk = "D"
    print("Hasil konversi dalam sub program = " + ipk)
    return ipk

#Main                
print("Masukan Ipk ")
ipk = float(input())
tempatSkor = konversiIpk(ipk)
print("Hasil konversi ipk ke skor (dalam main) = " + tempatSkor)