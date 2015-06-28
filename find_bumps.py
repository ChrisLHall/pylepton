import numpy as np
import scipy
import cv2
import time
import sys

def DetectBlobs(image):
  # Setup SimpleBlobDetector parameters.
  params = cv2.SimpleBlobDetector_Params()

  # Change thresholds
  params.minThreshold = 5
  params.maxThreshold = 150
  params.filterByArea = 1
  params.minArea = 30

  detector = cv2.SimpleBlobDetector(params)
  points = detector.detect((image * 255).astype('uint8'))
  keypoints_render = DrawKeypoints(image, points)
  return points, keypoints_render

def DrawKeypoints(vis, keypoints, color = (0, 255, 255)):
  result = np.zeros((vis.shape[0], vis.shape[1], 3), dtype='uint8')
  for kp in keypoints:
    x, y = kp.pt
    cv2.circle(result, (int(x), int(y)), int(kp.size), color)
  return result

if __name__ == "__main__":
  testimage = cv2.imread(sys.argv[1])
  inv = 255 * np.ones(testimage.shape, dtype='uint8') - testimage
  points, pointpic = DetectBlobs(255 * np.ones(testimage.shape) - testimage)
  print points


  final_image = np.zeros(testimage.shape, dtype='float')
  #final_image += testimage
  final_image += pointpic
  final_image += inv

  final_image = np.clip(final_image, 0.0, 255.0)

  cv2.imwrite("output/out_" + str(time.time()) + ".bmp", final_image)
