import numpy as np
import cv2
import matplotlib.pyplot as plt

def add_gaussian_noise(image, mean=0, std=25):
    row, col = image.shape
    gauss = np.random.normal(mean, std, (row, col))
    noisy_image = image + gauss
    noisy_image = np.clip(noisy_image, 0, 255)
    return noisy_image.astype(np.uint8), gauss

# Load a fingerprint image
image = cv2.imread('fingerprint.jpg', 0)  # Assuming a grayscale image

# Add Gaussian noise
noisy_image, gauss_noise = add_gaussian_noise(image)

# Display the original image, noisy image, and the Gaussian noise
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')

plt.subplot(1, 3, 2)
plt.title('Noisy Image')
plt.imshow(noisy_image, cmap='gray')

plt.subplot(1, 3, 3)
plt.title('Gaussian Noise')
plt.imshow(gauss_noise, cmap='gray')

plt.show()

# Print Gaussian noise values (first 5x5 section for brevity)
print("Gaussian Noise Values (5x5 section):")
print(gauss_noise[:5, :5])
