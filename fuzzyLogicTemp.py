import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

#Variabel INPUT: Suhu Kandang (C)
suhu = ctrl.Antecedent(np.arange(15, 41, 1), 'suhu')
#Variabel INPUT: Kelembaban (%)
kelembaban = ctrl.Antecedent(np.arange(40, 101, 1), 'kelembaban')
#Variabel INPUT: Ras Ayam (1-3)
ras_ayam = ctrl.Antecedent(np.arange(1, 4, 1), 'ras_ayam')
#Variabel OUTPUT: Kecepatan Kipas (%)
kipas = ctrl.Consequent(np.arange(0, 101, 1), 'kipas')

#Fungsi keanggotaan untuk SUHU
suhu['dingin'] = fuzz.trimf(suhu.universe, [15, 15, 25])
suhu['nyaman'] = fuzz.trimf(suhu.universe, [20, 25, 30])
suhu['panas'] = fuzz.trimf(suhu.universe, [25, 40, 40])

#Fungsi keanggotaan untuk KELEMBABAN
kelembaban['kering'] = fuzz.trimf(kelembaban.universe, [40, 40, 70])
kelembaban['normal'] = fuzz.trimf(kelembaban.universe, [60, 75, 90])
kelembaban['lembab'] = fuzz.trimf(kelembaban.universe, [80, 100, 100])

#Fungsi keanggotaan untuk RAS AYAM
#1 = Ras Pedaging (Broiler) - lebih sensitif panas
#2 = Ras Petelur (Layer) - toleransi sedang
#3 = Ras Lokal/Kampung - paling tahan panas
ras_ayam['pedaging'] = fuzz.trimf(ras_ayam.universe, [1, 1, 2])
ras_ayam['petelur'] = fuzz.trimf(ras_ayam.universe, [1.5, 2, 2.5])
ras_ayam['lokal'] = fuzz.trimf(ras_ayam.universe, [2, 3, 3])

#Fungsi keanggotaan untuk KIPAS
kipas['lambat'] = fuzz.trimf(kipas.universe, [0, 0, 40])
kipas['sedang'] = fuzz.trimf(kipas.universe, [20, 50, 80])
kipas['cepat'] = fuzz.trimf(kipas.universe, [60, 100, 100])


#MEMBUAT RULE BASE (aturan Fuzzy) dengan RAS
#RAS PEDAGING (Broiler) - Lebih sensitif terhadap panas
rule1 = ctrl.Rule(suhu['dingin'] & kelembaban['kering'] & ras_ayam['pedaging'], kipas['lambat'])
rule2 = ctrl.Rule(suhu['dingin'] & kelembaban['normal'] & ras_ayam['pedaging'], kipas['lambat'])
rule3 = ctrl.Rule(suhu['dingin'] & kelembaban['lembab'] & ras_ayam['pedaging'], kipas['sedang'])

rule4 = ctrl.Rule(suhu['nyaman'] & kelembaban['kering'] & ras_ayam['pedaging'], kipas['lambat'])
rule5 = ctrl.Rule(suhu['nyaman'] & kelembaban['normal'] & ras_ayam['pedaging'], kipas['sedang'])
rule6 = ctrl.Rule(suhu['nyaman'] & kelembaban['lembab'] & ras_ayam['pedaging'], kipas['sedang'])

rule7 = ctrl.Rule(suhu['panas'] & kelembaban['kering'] & ras_ayam['pedaging'], kipas['cepat'])
rule8 = ctrl.Rule(suhu['panas'] & kelembaban['normal'] & ras_ayam['pedaging'], kipas['cepat'])
rule9 = ctrl.Rule(suhu['panas'] & kelembaban['lembab'] & ras_ayam['pedaging'], kipas['cepat'])

#RAS PETELUR (Layer) - Toleransi sedang
rule10 = ctrl.Rule(suhu['dingin'] & kelembaban['kering'] & ras_ayam['petelur'], kipas['lambat'])
rule11 = ctrl.Rule(suhu['dingin'] & kelembaban['normal'] & ras_ayam['petelur'], kipas['lambat'])
rule12 = ctrl.Rule(suhu['dingin'] & kelembaban['lembab'] & ras_ayam['petelur'], kipas['sedang'])

rule13 = ctrl.Rule(suhu['nyaman'] & kelembaban['kering'] & ras_ayam['petelur'], kipas['lambat'])
rule14 = ctrl.Rule(suhu['nyaman'] & kelembaban['normal'] & ras_ayam['petelur'], kipas['sedang'])
rule15 = ctrl.Rule(suhu['nyaman'] & kelembaban['lembab'] & ras_ayam['petelur'], kipas['sedang'])

rule16 = ctrl.Rule(suhu['panas'] & kelembaban['kering'] & ras_ayam['petelur'], kipas['sedang'])
rule17 = ctrl.Rule(suhu['panas'] & kelembaban['normal'] & ras_ayam['petelur'], kipas['cepat'])
rule18 = ctrl.Rule(suhu['panas'] & kelembaban['lembab'] & ras_ayam['petelur'], kipas['cepat'])

# RAS LOKAL (Kampung) - Paling tahan panas
rule19 = ctrl.Rule(suhu['dingin'] & kelembaban['kering'] & ras_ayam['lokal'], kipas['lambat'])
rule20 = ctrl.Rule(suhu['dingin'] & kelembaban['normal'] & ras_ayam['lokal'], kipas['lambat'])
rule21 = ctrl.Rule(suhu['dingin'] & kelembaban['lembab'] & ras_ayam['lokal'], kipas['sedang'])

rule22 = ctrl.Rule(suhu['nyaman'] & kelembaban['kering'] & ras_ayam['lokal'], kipas['lambat'])
rule23 = ctrl.Rule(suhu['nyaman'] & kelembaban['normal'] & ras_ayam['lokal'], kipas['sedang'])
rule24 = ctrl.Rule(suhu['nyaman'] & kelembaban['lembab'] & ras_ayam['lokal'], kipas['sedang'])

rule25 = ctrl.Rule(suhu['panas'] & kelembaban['kering'] & ras_ayam['lokal'], kipas['sedang'])
rule26 = ctrl.Rule(suhu['panas'] & kelembaban['normal'] & ras_ayam['lokal'], kipas['sedang'])
rule27 = ctrl.Rule(suhu['panas'] & kelembaban['lembab'] & ras_ayam['lokal'], kipas['cepat'])

all_rules = [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
             rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18,
             rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27]

sistem_kontrol = ctrl.ControlSystem(all_rules)
simulasi = ctrl.ControlSystemSimulation(sistem_kontrol)


def konversi_ras(nama_ras):
    """Mengkonversi nama ras ke nilai numerik"""
    ras_dict = {
        'pedaging': 1,
        'broiler': 1,
        'petelur': 2,
        'layer': 2,
        'lokal': 3,
        'kampung': 3
    }
    return ras_dict.get(nama_ras.lower(), 2)  # default petelur

print("SISTEM KONTROL SUHU KANDANG AYAM DENGAN VARIABEL RAS")
print("=" * 60)

def test_sistem(suhu_val, kelembaban_val, ras_val, ras_nama):
    """Fungsi untuk testing sistem"""
    simulasi.input['suhu'] = suhu_val
    simulasi.input['kelembaban'] = kelembaban_val
    simulasi.input['ras_ayam'] = ras_val
    simulasi.compute()

    print(f"Ras: {ras_nama}")
    print(f"Suhu: {suhu_val}°C, Kelembaban: {kelembaban_val}%")
    print(f"Kecepatan Kipas: {simulasi.output['kipas']:.2f}%")

    #Memberikan rekomendasi berdasarkan kecepatan kipas
    speed = simulasi.output['kipas']
    if speed < 30:
        status = "KIPAS LAMBAT - Suhu optimal"
    elif speed < 70:
        status = "KIPAS SEDANG - Kondisi normal"
    else:
        status = "KIPAS CEPAT - Butuh pendinginan ekstra!"

    print(f"Rekomendasi: {status}")
    print("-" * 50)

#Test case: Kondisi panas (35 Celcius) dengan berbagai ras
print("\nPERBANDINGAN BERBAGAI RAS PADA SUHU 35°C:")
test_sistem(35, 75, 1, "PEDAGING (Broiler)")
test_sistem(35, 75, 2, "PETELUR (Layer)")
test_sistem(35, 75, 3, "LOKAL (Kampung)")

print("\nPERBANDINGAN BERBAGAI RAS PADA SUHU 28°C:")
test_sistem(28, 70, 1, "PEDAGING (Broiler)")
test_sistem(28, 70, 2, "PETELUR (Layer)")
test_sistem(28, 70, 3, "LOKAL (Kampung)")

print("\nPERBANDINGAN BERBAGAI RAS PADA SUHU 18°C:")
test_sistem(18, 60, 1, "PEDAGING (Broiler)")
test_sistem(18, 60, 2, "PETELUR (Layer)")
test_sistem(18, 60, 3, "LOKAL (Kampung)")

#VISUALISASI FUNGSI KEANGGOTAAN RAS
def plot_fuzzy_sets():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

    suhu.view(ax=ax1)
    ax1.set_title('Fungsi Keanggotaan - Suhu Kandang')

    kelembaban.view(ax=ax2)
    ax2.set_title('Fungsi Keanggotaan - Kelembaban')

    ras_ayam.view(ax=ax3)
    ax3.set_title('Fungsi Keanggotaan - Ras Ayam')

    kipas.view(ax=ax4)
    ax4.set_title('Fungsi Keanggotaan - Kecepatan Kipas')

    plt.tight_layout()
    plt.show()
    #Uncomment untuk melihat visualisasi
    #plot_fuzzy_sets()

#SIMULASI INTERAKTIF DENGAN RAS
def simulasi_interaktif():
    print("\n" + "="*60)
    print("SIMULASI INTERAKTIF DENGAN VARIABEL RAS")
    print("="*60)

    try:
        input_suhu = float(input("Masukkan suhu kandang (°C) [15-40]: "))
        input_kelembaban = float(input("Masukkan kelembaban (%) [40-100]: "))

        print("\nPilih ras ayam:")
        print("1. Pedaging/Broiler (sensitif panas)")
        print("2. Petelur/Layer (toleransi sedang)")
        print("3. Lokal/Kampung (tahan panas)")

        pilihan_ras = input("Masukkan pilihan ras [1/2/3] atau nama ras: ")

        #Konversi input ras
        if pilihan_ras in ['1', 'pedaging', 'broiler']:
            ras_nama = "PEDAGING"
            ras_val = 1
        elif pilihan_ras in ['2', 'petelur', 'layer']:
            ras_nama = "PETELUR"
            ras_val = 2
        elif pilihan_ras in ['3', 'lokal', 'kampung']:
            ras_nama = "LOKAL"
            ras_val = 3
        else:
            print("Pilihan tidak valid, menggunakan default (Petelur)")
            ras_nama = "PETELUR"
            ras_val = 2

        if 15 <= input_suhu <= 40 and 40 <= input_kelembaban <= 100:
            test_sistem(input_suhu, input_kelembaban, ras_val, ras_nama)
        else:
            print("Input suhu atau kelembaban di luar range yang valid!")

    except ValueError:
        print("Input harus berupa angka!")

#Uncomment untuk menjalankan simulasi interaktif
simulasi_interaktif()

#ANALISIS PENGARUH RAS TERHADAP KECEPATAN KIPAS

def analisis_pengaruh_ras():
    """Analisis bagaimana ras mempengaruhi kecepatan kipas pada berbagai suhu"""
    print("\n" + "="*60)
    print("ANALISIS PENGARUH RAS TERHADAP KECEPATAN KIPAS")
    print("="*60)

    suhu_test = [20, 25, 30, 35]
    kelembaban_test = 70

    print(f"Kelembaban tetap: {kelembaban_test}%")
    print("\nSuhu(°C) | Pedaging | Petelur | Lokal")
    print("-" * 40)

    for s in suhu_test:
        speeds = []
        for ras_val in [1, 2, 3]:
            simulasi.input['suhu'] = s
            simulasi.input['kelembaban'] = kelembaban_test
            simulasi.input['ras_ayam'] = ras_val
            simulasi.compute()
            speeds.append(simulasi.output['kipas'])

        print(f"{s:7} | {speeds[0]:8.1f} | {speeds[1]:7.1f} | {speeds[2]:5.1f}")

#Uncomment untuk melihat analisis
analisis_pengaruh_ras()
