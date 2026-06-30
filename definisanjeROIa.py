import cv2

# --- Podešavanja ---
putanja_slike = "slikaRubikoveKocke.jpg" 
skala = 0.5          # Faktor smanjenja (promeni na 1.0 ako ne želiš smanjenje)
max_clicks = 15      # Maksimalan broj ROI-a
roi_size = 40         # Dimenzija ROI-a (7x7)
half_size = roi_size // 2  # 3 piksela od centra za 7x7 kvadrat

# Globalna lista za čuvanje koordinata
rois = []

def click_event(event, x, y, flags, param):
    global rois, img_display
    
    # Detekcija levog klika i provera limita
    if event == cv2.EVENT_LBUTTONDOWN and len(rois) < max_clicks:
        # Računanje granica (xmin, xmax, ymin, ymax)
        ymin = y - half_size
        ymax = y + half_size
        xmin = x - half_size
        xmax = x + half_size
        
        # Dodavanje u listu
        rois.append((xmin, xmax, ymin, ymax))
        
        # Crtanje kvadrata i broja na ekranu
        cv2.rectangle(img_display, (xmin, ymin), (xmax, ymax), (0, 0, 255), 1)
        cv2.putText(img_display, str(len(rois)), (xmin, ymin - 2), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)
        
        cv2.imshow("Odabir ROI-a", img_display)
        print(f"Klik {len(rois)}/15 zabeležen na poziciji ({x}, {y})")
        
        if len(rois) == max_clicks:
            print("\nOdabrano svih 15 ROI-a! Zatvaram prozor i generišem kod...")

# --- Glavni deo programa ---

img_original = cv2.imread(putanja_slike)

if img_original is None:
    print(f"Greška: Slika na putanji '{putanja_slike}' nije pronađena!")
else:
    # Smanjivanje rezolucije slike
    nova_sirina = int(img_original.shape[1] * skala)
    nova_visina = int(img_original.shape[0] * skala)
    img_smanjena = cv2.resize(img_original, (nova_sirina, nova_visina), interpolation=cv2.INTER_AREA)
    img_display = img_smanjena.copy()
    
    cv2.namedWindow("Odabir ROI-a")
    cv2.setMouseCallback("Odabir ROI-a", click_event)
    
    print(f"Slika je smanjena na {skala*100}% ({nova_sirina}x{nova_visina})")
    print("Klikni 15 puta na sliku redosledom kojim želiš da ti se ispisuju boje.")
    
    cv2.imshow("Odabir ROI-a", img_display)
    
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or len(rois) == max_clicks:
            break
            
    cv2.destroyAllWindows()

    # --- FORMATIRAN ISPIS ZA COPY-PASTE ---
    print("\n" + "="*50)
    print("Samo kopiraj blok ispod i prelepi ga u glavni kod:")
    print("="*50 + "\n")
    
    print("ZADATI_ROI = [")
    for i, roi in enumerate(rois):
        zarez = "," if i < len(rois) - 1 else ""
        print(f"    ({roi[0]}, {roi[1]}, {roi[2]}, {roi[3]}){zarez}  # ROI {i+1}")
    print("]")
    print("\n" + "="*50)