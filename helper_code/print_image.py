import os
import matplotlib.pyplot as plt


def print_image(image_path):
    image = plt.imread(image_path)
    # Display the image
    plt.imshow(image)
    plt.axis('off')  # This line removes the axis with numbers around the image
    plt.show()

def print_all_images(img_dir):
    # add / if not exists
    img_dir = img_dir + '/'
    img_dir = img_dir.replace('//', '/')
    # pull all image paths
    image_paths = [img_dir + fname for fname in sorted(os.listdir(img_dir))]
    print(image_paths)
    print('')
    # print all images
    for image_path in image_paths:
        print('image_path: ', image_path)
        print_image(image_path)