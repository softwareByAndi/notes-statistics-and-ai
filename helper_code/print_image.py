import os
import matplotlib.pyplot as plt

def print_image(image_path):
    image = plt.imread(image_path)
    # Display the image
    plt.imshow(image)
    plt.axis('off')  # This line removes the axis with numbers around the image
    plt.show()

def print_images(image_paths):
    for image_path in image_paths:
        print('image_path: ', image_path)
        print_image(image_path)

def get_all_image_paths(img_dir):
    img_dir = img_dir + '/'
    img_dir = img_dir.replace('//', '/')
    # pull all image paths
    image_paths = [img_dir + fname for fname in sorted(os.listdir(img_dir))]
    return image_paths

def print_all_images(img_dir):
    # add / if not exists
    image_paths = get_all_image_paths(img_dir)
    print(image_paths)
    print('')
    print_images(image_paths)