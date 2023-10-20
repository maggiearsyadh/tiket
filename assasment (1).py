#NIM : 607012330021
#NAMA : Maggie Arsyad H

nama = input('masukan nama pelanggan : ')
kode_penerbangan = int(input('masukan kode penerbangan :\n [1]tujuan : jakarta\n [2]tujuan : surabaya\n [3]tujuan : denpasar\n masukan kode penerbangan : '))

if kode_penerbangan == 1 :
    jumlah= int(input('masukan jumlah pesanan : '))
    harga = jumlah * 50000
    if jumlah >3 :
        diskon = harga*0.10
        total_bayar = harga - diskon
    else :
        diskon = 0
        total_bayar = harga - diskon

elif kode_penerbangan == 2 :
    jumlah= int(input('masukan jumlah pesanan'))
    harga = jumlah * 110000
    if jumlah >3 :
        diskon = harga*0.10
        total_bayar = harga - diskon
    else :
        diskon = 0
        total_bayar = harga - diskon

elif kode_penerbangan == 3 :
    jumlah= int(input('masukan jumlah pesanan'))
    harga = jumlah * 150000
    if jumlah >3 :
        diskon = harga*0.10
        total_bayar = harga - diskon
    else :
        diskon = 0
        total_bayar = harga - diskon

else :
    print ('kode penerbangan tidak ada')

print ('halo', nama, 'anda memilih kode penerbangan',kode_penerbangan,'total bayar anda', total_bayar)



