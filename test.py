import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("Tsumiki.png")
image2 = cv2.imread("Tsumiki2.png")

def show_image(image , title):
  image = cv2.cvtColor(image , cv2.COLOR_RGB2HLS)
  plt.imshow(image)
  plt.title(title)
  plt.axis("off")
  plt.show()

show_image(image , "Tsumiki.chan")
show_image(image2 , "Tsumiki2")