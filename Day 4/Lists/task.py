# CARA CARI LIST DIMULAI DARI 0 BUKAN DARI 1 , BISA DARI -1 ITU PALING BELAKANG
states_of_america = ['Delaware', 'Pennsylvania', 'New Jersey', 'Georgia', 'Connecticut', 'Massachusetts', 'Maryland', 'South Carolina', 'New Hampshire', 'Virginia', 'New York', 'North Carolina', 'Rhode Island', 'Vermont', 'Kentucky', 'Tennessee', 'Ohio', 'Louisiana', 'Indiana', 'Mississippi', 'Illinois', 'Alabama', 'Maine', 'Missouri', 'Arkansas', 'Michigan', 'Florida', 'Texas', 'Iowa', 'Wisconsin', 'California', 'Minnesota', 'Oregon', 'Kansas', 'West Virginia', 'Nevada', 'Nebraska', 'Colorado', 'North Dakota', 'South Dakota', 'Montana', 'Washington', 'Idaho', 'Wyoming', 'Utah', 'Oklahoma', 'New Mexico', 'Arizona', 'Alaska', 'Hawaii']
# print(states_of_america[0]) DEPAN
# print(states_of_america[-1]) PALING BELAKANG

# BISA UBAH NAMA DARI NOMOR MANA AJA
# states_of_america[0] = "Delase"
# print(states_of_america)

# BISA TAMBAH NAMA BARIS TERAKHIR PAKE APPEND
# states_of_america.append("Marilend")
# print(states_of_america)

# BISA TAMBAH NAMA DI akhir BARIS
states_of_america.extend(["Marilend", "JackieLand"])
print(states_of_america)