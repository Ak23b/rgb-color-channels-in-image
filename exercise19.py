from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Loading our image and showing its shape and dimensions
img = Image.open("yourImage.png")
img_arr = np.array(img)

print("Shape:\n",img_arr.shape)
print("Dimensions:\n",img_arr.ndim)

# Plotting the Image
plt.imshow(img_arr)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Converting the Image to grayscale
gray = img.convert("L")
gray_arr = np.array(gray)

plt.imshow(gray_arr,cmap="Grays")
plt.title("Gray Image")
plt.axis("off")
plt.show()

# Splitting into RGB and plotting each color channel
R = img_arr[:,:,0]
G = img_arr[:,:,1]
B = img_arr[:,:,2]

plt.imshow(R,cmap="Reds")
plt.title("Red Channel Image.")
plt.axis("off")
plt.show()

plt.imshow(G,cmap="Greens")
plt.title('Green Channel')
plt.axis("off")
plt.show()

plt.imshow(B,cmap="Blues")
plt.title("Blue Channel Image")
plt.axis("off")
plt.show()