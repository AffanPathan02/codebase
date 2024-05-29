import cv2
import numpy as np
import hashlib
import matplotlib.pyplot as plt

# Step 1: Load the image
image = cv2.imread('noisy_fingerprint.jpg', 0)  # Assuming a grayscale image

# Step 2: Convert to binary matrix using a threshold
_, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Step 3: Flatten the binary matrix to a 1D array
binary_array = binary_image.flatten()

# Step 4: Convert the binary array to bytes
binary_bytes = bytes(binary_array)

# Step 5: Apply SHA-256 hash to the binary data
sha256_hash = hashlib.sha256(binary_bytes).hexdigest()

# Output the SHA-256 hash
print("SHA-256 Hash of the Binary Image:")
print(sha256_hash)

# Output the binary matrix (print first 5 rows for brevity)
print("Binary Matrix (first 5 rows):")
print(binary_image[:5, :])

# Apply erosion to remove small structures and noise
kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(binary_image, kernel, iterations=1)

# Apply dilation to fill in gaps and smooth the image
dilation = cv2.dilate(erosion, kernel, iterations=1)

# Display the original and processed images side by side
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', dilation)



# Find the contours in the binary image
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw the contours on the original image
cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
print(len(contours))

# Display the original image with contours
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
