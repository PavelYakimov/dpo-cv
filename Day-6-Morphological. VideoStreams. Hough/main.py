import cv2
import numpy as np

def choose_red(img, img_hsv):
    # lower mask (0-10)
    lower_red = np.array([30, 50, 50])
    upper_red = np.array([50, 255, 255])
    mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

    # upper mask (170-180)
    lower_red = np.array([50, 50, 50])
    upper_red = np.array([80, 255, 255])
    mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

    # join my masks
    mask = mask0 + mask1

    # set my output img to zero everywhere except my mask
    output_img = img.copy()
    output_img[np.where(mask == 0)] = 0

    # or your HSV image, which I *believe* is what you want
    # output_hsv = img_hsv.copy()
    # output_hsv[np.where(mask == 0)] = 0

    return output_img

def our_hough_circles(testImage):
  img = cv2.medianBlur(testImage,5)
  circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=40,minRadius=70,maxRadius=90)
  if circles is None:
      return False, circles
  else:
      circles = np.uint16(np.around(circles))
      return True, circles

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = choose_red(frame, hsv_image)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    success, circles = our_hough_circles(gray)
    if success:
        for i in circles[0, :]:
            #draw the outer circle
            cv2.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # draw the center of the circle
            cv2.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

# Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()