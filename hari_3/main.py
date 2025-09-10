import cv2

# Baca gambar
img = cv2.imread("/home/fluks/Documents/PATH SNU/OPEN CV/pic.jpg")
resized = cv2.resize(img, (300, 300))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(resized, (7, 7), 0)

# Edge detection
edges = cv2.Canny(gray, 100, 200)

# Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Simpan hasil
cv2.imwrite("blur.jpg", blur)
cv2.imwrite("edges.jpg", edges)
cv2.imwrite("threshold.jpg", thresh)

# Tampilkan hasil
cv2.imshow("Original", resized)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("✅ Semua hasil tersimpan (hari3_blur.jpg, hari3_edges.jpg, hari3_threshold.jpg)")