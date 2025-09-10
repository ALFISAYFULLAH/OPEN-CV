import cv2

# Baca gambar
img = cv2.imread("/home/fluks/Documents/PATH SNU/OPEN CV/pic.jpg")

# Resize
resized = cv2.resize(img, (300, 300))

# Crop
cropped = img[100:300, 200:400]

# Grayscale
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# HSV
hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)

# Simpan hasil
cv2.imwrite("resized.jpg", resized)
cv2.imwrite("cropped.jpg", cropped)
cv2.imwrite("gray.jpg", gray)
cv2.imwrite("hsv.jpg", hsv)

# Tampilkan
cv2.imshow("Resized", resized)
cv2.imshow("Cropped", cropped)
cv2.imshow("Gray", gray)
cv2.imshow("HSV", hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("✅ Semua hasil tersimpan (hari2_resized.jpg, hari2_cropped.jpg, dst.)")