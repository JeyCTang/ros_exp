import cv2

# image path
path = r'./geeks14.png'

# Reading an image in default mode
src_img = cv2.imread(path)

# Window name is the name when we display the image
window_name = 'Image'

# Using cv2.cvtColor() method
# Color space: cv2.COLOR_BGR2GRAY
# Color space: cv2.COLOR_BGR2RGB
# Color space: CV2.COLOR_BGR2HSV
image = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)

# Display the image
cv2.imshow(window_name, image)

cv2.waitKey(0)

cv2.destroyAllWindows()