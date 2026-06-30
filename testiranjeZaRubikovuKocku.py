import serial
import time

# Podešavanje serijskog porta
SERIAL_PORT = '/dev/ttyACM0' 
BAUD_RATE = 115200

# Lista komandi
komande = [
    "BOTE",
    "B0TE",
    "R1TE",
    "R1R1R1TE",
    "L0TE",
    "F1F1TE",
    "B1B1R1R1R1R1L1TE"
]

try:
    # Otvaranje serijske veze BEZ timeout parametra (timeout=None)
    # Ovo govori Pajtonu da čeka odgovor zauvek
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE) 
    print(f"Povezan na {SERIAL_PORT}. Čekam inicijalizaciju Arduina...")
    time.sleep(2) # Pauza za auto-reset Arduina
    
    for i, komanda in enumerate(komande, 1):
        print(f"\n--- Korak {i}/{len(komande)} ---")
        print(f"Šaljem komandu: {komanda}")
        
        # Slanje komande Arduinu
        ser.write((komanda + '\n').encode('utf-8'))
        
        print("Čekam odgovor od Arduina (bez vremenskog ograničenja)...")
        
        # Program ovde stoji i čeka sekunde, minute ili sate – sve dok Arduino ne pošalje '\n'
        odgovor = ser.readline().decode('utf-8').rstrip()
        
        print(f"Odgovor od Arduina: {odgovor}")
            
        # Mala pauza pre slanja sledeće komande
        time.sleep(0.1)

    print("\nSve komande su uspešno izvršene!")

except Exception as e:
    print(f"\nGreška tokom izvršavanja: {e}")

finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
        print("Serijski port zatvoren.")