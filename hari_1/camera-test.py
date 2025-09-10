import cv2

# Buka kamera
cap = cv2.VideoCapture(0)

# Dapatkan ukuran frame
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Buat VideoWriter (nama file, codec, fps, ukuran)
out = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', out, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Simpan frame ke file
    out.write(frame)

    # Tampilkan juga biar bisa lihat real-time
    cv2.imshow("Rekam", frame)

    # Tekan 'q' untuk berhenti
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video berhasil disimpan!")