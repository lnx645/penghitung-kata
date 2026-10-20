# 📝 Penghitung Kata (Analisis Teks CLI)

Program CLI Python untuk menganalisis teks dari file atau stdin. Menampilkan:
- Jumlah kata, kalimat, karakter, dan paragraf
- 10 kata teratas berdasarkan frekuensi (mengabaikan kata umum:
  `dan`, `yang`, `di`, `ke`, `dari`)

## Cara Menjalankan

```bash
# Dari file
python3 main.py contoh.txt

# Dari stdin (pipe)
echo "Halo dunia. Halo lagi." | python3 main.py

# Interaktif: tempel teks lalu tekan Ctrl+D
python3 main.py
```
