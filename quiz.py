def distribusi_statis_beban(daftar_pekerjaan, jumlah_pekerja):
    akumulasi_beban = [0] * jumlah_pekerja
    
    # Menggunakan metode Round-Robin untuk pembagian tugas statis
    for indeks, waktu_tugas in enumerate(daftar_pekerjaan):
        id_pekerja = indeks % jumlah_pekerja
        akumulasi_beban[id_pekerja] += waktu_tugas
        print(f"Pekerjaan dengan bobot {waktu_tugas} dialokasikan ke Pekerja-{id_pekerja + 1}")

    print("\n=== REKAPITULASI HASIL ===")
    for i, beban in enumerate(akumulasi_beban):
        print(f"Beban akhir Pekerja-{i + 1} : {beban}")

    waktu_maksimal = max(akumulasi_beban)
    waktu_ideal = sum(daftar_pekerjaan) / jumlah_pekerja

    print(f"\nWaktu komputasi tertinggi (Static Max Time) : {waktu_maksimal}")
    print(f"Kondisi Ideal (Total Beban / Pekerja)       : {waktu_ideal}")
    
    if waktu_maksimal == waktu_ideal:
        print("-> Kesimpulan: Program berhasil mencapai kondisi distribusi ideal.")
    else:
        selisih = waktu_maksimal - waktu_ideal
        print(f"-> Kesimpulan: Distribusi belum ideal. Terdapat selisih waktu sebesar {selisih} dari target ideal.")

# Data array tugas dengan ukuran bervariasi (uneven)
pekerjaan_acak = [15, 4, 25, 9, 6, 11, 14, 8, 2]
total_pekerja = 3

distribusi_statis_beban(pekerjaan_acak, total_pekerja)