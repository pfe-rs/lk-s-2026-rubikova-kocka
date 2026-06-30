import serial
import time
import cv2
import numpy as np

# --- 1. PODEŠAVANJE SLIKE I SKALE ---
PUTANJA_SLIKE = "slikaRubikoveKocke.jpg"  # Unesi tačnu putanju do slike
SKALA = 0.5                        # Faktor smanjenja (mora biti isti kao u prvom kodu!)

# --- 2. KOORDINATE TVOJIH 15 ROI-a ---
# Ovde prelepiš blok koji ti je izbacio prethodni (prvi) kod
ZADATI_ROI = [
    (167, 207, 235, 275),  # ROI 1
    (323, 363, 314, 354),  # ROI 2
    (525, 565, 444, 484),  # ROI 3
    (699, 739, 316, 356),  # ROI 4
    (853, 893, 219, 259),  # ROI 5
    (936, 976, 354, 394),  # ROI 6
    (783, 823, 462, 502),  # ROI 7
    (603, 643, 590, 630),  # ROI 8
    (605, 645, 788, 828),  # ROI 9
    (613, 653, 933, 973),  # ROI 10
    (432, 472, 918, 958),  # ROI 11
    (443, 483, 772, 812),  # ROI 12
    (401, 441, 570, 610),  # ROI 13
    (233, 273, 478, 518),  # ROI 14
    (110, 150, 394, 434)  # ROI 15
]


# --- 3. DEFINISANJE HSV OPSEGA ZA SVAKU BOJU ---
BOJE_HSV = {
    'Y': ((20, 100, 100), (35, 255, 255)),    # Žuta
    'G': ((35, 60, 60), (85, 255, 255)),     # Zelena
    'B': ((90, 60, 60), (130, 255, 255)),    # Plava
    'O': ((10, 100, 100), (20, 255, 255)),    # Narandžasta
    'W': ((0, 0, 160), (180, 50, 255)),      # Bela
}
CRVENA_LOW1, CRVENA_HIGH1 = (0, 70, 70), (10, 255, 255)
CRVENA_LOW2, CRVENA_HIGH2 = (170, 70, 70), (180, 255, 255)


def prepoznaj_boju_u_roi(roi_bgr):
    """Analizira ROI i vraća dominantno slovo boje ako prelazi 50% udela piksela."""
    ukupno_piksela = roi_bgr.shape[0] * roi_bgr.shape[1]
    roi_hsv = cv2.cvtColor(roi_bgr, cv2.COLOR_BGR2HSV)
    
    rezultati = {}
    for boja, (low, high) in BOJE_HSV.items():
        maska = cv2.inRange(roi_hsv, np.array(low), np.array(high))
        rezultati[boja] = cv2.countNonZero(maska)
        
    maska_r1 = cv2.inRange(roi_hsv, np.array(CRVENA_LOW1), np.array(CRVENA_HIGH1))
    maska_r2 = cv2.inRange(roi_hsv, np.array(CRVENA_LOW2), np.array(CRVENA_HIGH2))
    rezultati['R'] = cv2.countNonZero(maska_r1) + cv2.countNonZero(maska_r2)
    
    dominantna_boja = 'F'
    max_piksela = 0
    
    for boja, broj in rezultati.items():
        if broj > max_piksela:
            max_piksela = broj
            dominantna_boja = boja
            
    if max_piksela > (ukupno_piksela / 2):
        return dominantna_boja
    else:
        return 'F'


# --- GLAVNI KOD ZA SERIJSKU KOMUNIKACIJU ---

SERIAL_PORT = 'COM9'
BAUD_RATE = 115200

komande = ["BOTE", "B0TE", "R1TE", "R1R1R1TE", "L0TE", "F1F1TE", "B1B1R1R1R1R1L1TE"]

# Učitavanje originalne slike sa računara
img_original = cv2.imread(PUTANJA_SLIKE)

if img_original is None:
    print(f"Greška: Slika na putanji '{PUTANJA_SLIKE}' nije pronađena!")
    exit()

# Smanjivanje rezolucije slike na isti način kao u prvom kodu
nova_sirina = int(img_original.shape[1] * SKALA)
nova_visina = int(img_original.shape[0] * SKALA)
img_smanjena = cv2.resize(img_original, (nova_sirina, nova_visina), interpolation=cv2.INTER_AREA)

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE) 
    print(f"Povezan na {SERIAL_PORT}. Čekam inicijalizaciju Arduina...")
    time.sleep(2) # Pauza za auto-reset Arduina
    
    for i, komanda in enumerate(komande, 1):
        print(f"\n--- Korak {i}/{len(komande)} ---")
        print(f"Šaljem komandu: {komanda}")
        
        ser.write((komanda + '\n').encode('utf-8'))
        print("Čekam odgovor od Arduina...")
        
        odgovor = ser.readline().decode('utf-8').rstrip()
        print(f"Odgovor od Arduina: {odgovor}")
        
        # --- ANALIZA BOJA NA SMANJENOJ SLICI ---
        string_stranice = ""
        
        # Pravimo kopiju smanjene slike za crtanje kvadratnih ROI-a u ovom koraku
        frame_prikaz = img_smanjena.copy()
        
        # Prolazimo kroz svih 15 ROI-a
        for roi_koordinate in ZADATI_ROI:
            xmin, xmax, ymin, ymax = roi_koordinate
            
            # Isecanje ROI-a iz smanjene slike
            roi_isečak = img_smanjena[ymin:ymax+1, xmin:xmax+1]
            
            # Prepoznavanje boje
            boja_karakter = prepoznaj_boju_u_roi(roi_isečak)
            string_stranice += boja_karakter
            
            # Iscrtavanje zelenih kvadratića na prikazu
            cv2.rectangle(frame_prikaz, (xmin, ymin), (xmax, ymax), (0, 255, 0), 1)
        
        print(f"PREPOZNATE BOJE (15 ROI): {string_stranice}")
        
        # Prikaz i čuvanje rezultata analize za taj korak
        cv2.imshow('Analiza smanjene staticke slike', frame_prikaz)
        cv2.imwrite(f"analiza_korak_{i}.jpg", frame_prikaz)
        
        cv2.waitKey(1000)  # Drži prozor otvoren 1 sekundu
        time.sleep(0.1)

    print("\nSve komande su uspešno izvršene!")
    print("Pritisni bilo koji taster na prozoru sa slikom za kraj.")
    cv2.waitKey(0)

except Exception as e:
    print(f"\nGreška tokom izvršavanja: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serijski port zatvoren.")
    cv2.destroyAllWindows()