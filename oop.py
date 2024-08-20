"""
Anda diminta untuk membuat sebuah sistem sederhana untuk mengelola kendaraan di sebuah rental mobil.
Ada dua jenis kendaraan yang tersedia: Mobil dan Motor.
Setiap kendaraan memiliki metode untuk menghitung biaya sewa berdasarkan jumlah hari.

noted : 1. Buatlah sebuah `class` abstrak bernama `Kendaraan` yang memiliki metode abstrak
`hitungBiayaSewa(int hari)`.

2. Implementasikan kelas `Mobil` dan `Motor` yang meng-extend `Kendaraan`.
Kelas `Mobil` memiliki biaya sewa Rp 500.000 per hari.
Kelas `Motor` memiliki biaya sewa Rp 100.000 per hari.

3. Buatlah sebuah metode yang menerima objek Kendaraan dan jumlah hari sebagai parameter, 
lalu menampilkan biaya sewa berdasarkan jenis kendaraan.


4. Buatlah beberapa objek dari Mobil dan Motor,
lalu tampilkan biaya sewanya menggunakan metode yang telah dibuat.
// Input
Mobil mobil = new Mobil("Toyota");
Motor motor = new Motor("Yamaha");

tampilkanBiayaSewa(mobil, 3); // Output: 1500000
tampilkanBiayaSewa(motor, 3); // Output: 300000
"""
#https://github.com/ganggaa

from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def hitungBiayaSewa(self, hari):
        pass
    
class Mobil(Kendaraan):
    def __init__(self, merk):
        self.merk = merk
    def hitungBiayaSewa(self, hari):
        return 500000 * hari
    
class Motor(Kendaraan):
    def __init__(self, merk):
        self.merk = merk
    def hitungBiayaSewa(self, hari):
        return 100000 * hari
    
def tampilkanBiayaSewa(kendaraan, hari):
    print(kendaraan.hitungBiayaSewa(hari))
    
mobil = Mobil("Toyota");
motor = Motor("Yamaha");

tampilkanBiayaSewa(mobil, 3); 
tampilkanBiayaSewa(motor, 3);