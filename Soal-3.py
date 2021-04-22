nilai_ut = input("Masukkan nilai ujian teori: ")
nilai_up = input("Masukkan nilai ujian praktek: ")

nilai_ut = float(nilai_ut)
nilai_up = float(nilai_up)

if nilai_ut >= 70 and nilai_up >= 70:
    print("Selamat, anda lulus!")
elif nilai_up <70 and nilai_ut >= 70:
    print("Anda harus mengulang ujian praktek.")
elif nilai_ut <70 and nilai_up >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")