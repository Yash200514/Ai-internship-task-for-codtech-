import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def load_image(path):
    img = Image.open(path)
    img = img.resize((512, 512))
    img = np.array(img) / 255.0
    img = img.astype(np.float32)
    img = img[np.newaxis, ...]
    return img

def main():
    print("Loading images...")

    content_image = load_image("content.jpg")
    style_image = load_image("style.jpg")

    print("Loading model...")
    model = hub.load(
        "https://tfhub.dev/google/magenta/arbitrary-image-stylization-v1-256/2"
    )

    print("Applying style transfer...")
    stylized_image = model(tf.constant(content_image),
                           tf.constant(style_image))[0]

    output = np.squeeze(stylized_image.numpy())
    plt.imsave("output.jpg", output)

    print("Stylized image saved as output.jpg")

if __name__ == "__main__":
    main()
