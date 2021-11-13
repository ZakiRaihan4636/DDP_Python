# pegawai1 dan 2 mempunyai nilai nama, agama, gaji pokok, dan jumlah anak
pegawai1 = ['Ahmad','Islam',4000000,2]
pegawai2 = ['alex','kristen protestan', 6000000,5]

# tunjangan jabatan 
tunjangan_jabatan = 20/100

#if multi kondisi tunjangan keluarga pegawai1
if (pegawai1[3] <= 2):
        tunjangan_keluarga = 10/100 * pegawai1[2]
elif (pegawai1[3] >2):
    tunjangan_keluarga = 20/100 * pegawai1[2]
else:
   tunjangan_keluarga = 0

#gaji kotor pegawai1
gaji_kotor = pegawai1[2] + tunjangan_jabatan * pegawai1[2] + tunjangan_keluarga

zakat_profesi = 0
if (pegawai1[1] == "Islam" and gaji_kotor >= 6000000):
    zakat_profesi = 2.5/100 * gaji_kotor
else:
    zakat_profesi = 0

#gaji bersih pegawai1
gaji_bersih =  gaji_kotor - zakat_profesi

# cetak
print('SLIP GAJI PT. XYZ')
print('------------------')
print('Nama Pegawai\t\t:',pegawai1[0])
print('Agama\t\t\t:',pegawai1[1])
print('Jumlah Anak\t\t:',pegawai1[3])
print('Gaji Pokok\t\t: Rp.',pegawai1[2])
print('Tunjangan Jabatan\t: Rp.',tunjangan_jabatan*pegawai1[2])
print('Tunjangan Keluarga\t: Rp.',tunjangan_keluarga)
print('Gaji Kotor\t\t: Rp.', gaji_kotor)
print('Zakat Profesi\t\t: Rp.', zakat_profesi)
print('Take Home Pay\t\t: Rp.', gaji_bersih)

# # If multi kondisi tunjangan keluarga pegawai2
# if(pegawai2[3] <= 2):
#         tunjangan_keluarga = 10/100 * pegawai2[2]
# elif(pegawai2[3] > 2):
#     tunjangan_keluarga = 20/100 * pegawai2[2]
# else:
#    tunjangan_keluarga = 0

# # gaji kotor pegawai2
# gaji_kotor = pegawai2[2] + tunjangan_jabatan* pegawai2[2] + tunjangan_keluarga

# # zakat profesi
# zakat_profesi = 0
# if(pegawai2[1] == "Islam" and gaji_kotor > 6000000):
#     zakat_profesi = 2,5/100 * gaji_kotor
# else:
#     zakat_profesi = 0

# # gaji_bersih pegawai2
# gaji_bersih =  gaji_kotor - zakat_profesi

# # mencetak
# print('SLIP GAJI PT. XYZ')
# print('------------------')
# print('Nama Pegawai\t\t:',pegawai2[0])
# print('Agama\t\t\t:',pegawai2[1])
# print('Jumlah Anak\t\t:',pegawai2[3])
# print('Gaji Pokok\t\t: Rp.',pegawai2[2])
# print('Tunjangan Jabatan\t: Rp.',tunjangan_jabatan*pegawai2[2])
# print('Tunjangan Keluarga\t: Rp.',tunjangan_keluarga)
# print('Gaji Kotor\t\t: Rp.', gaji_kotor)
# print('Zakat Profesi\t\t: Rp.', zakat_profesi)
# print('Take Home Pay\t\t: Rp.', gaji_bersih)

