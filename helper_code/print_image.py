import matplotlib.pyplot as plt


def print_image(image_path):
    image = plt.imread(image_path)
    # Display the image
    plt.imshow(image)
    plt.axis('off')  # This line removes the axis with numbers around the image
    plt.show()
