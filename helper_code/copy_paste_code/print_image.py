import os
import matplotlib.pyplot as plt

def print_image(image_path):
    image = plt.imread(image_path)
    # Display the image
    plt.imshow(image)
    plt.axis('off')  # This line removes the axis with numbers around the image
    plt.show()

img_dir = "images/"
images = sorted(os.listdir(img_dir))
print(images)
print('')
for image_path in images:
    print(img_dir + image_path)
    print_image(img_dir + image_path)