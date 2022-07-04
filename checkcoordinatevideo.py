# importing the module
import cv2

INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.2
NMS_THRESHOLD = 0.4
CONFIDENCE_THRESHOLD = 0.4

def resizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)
# function to display the coordinates of
# of the points clicked on the image

def click_event(event, x, y, flags, params):
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)

    # checking for right mouse clicks
    if event == cv2.EVENT_RBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)

        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x, y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)

# driver function
video = cv2.VideoCapture('dataset/test 1.mp4')
    # new_img = cv2.imread('pedestrian.jpg', 0)

    #width = 1280
    #height = 720
cv2.namedWindow('image')
cv2.setMouseCallback('image', click_event)

while True:
    rc, img = video.read()
    if type(img) == type(None):
        break
        #resize = resizeWithAspectRatio(frame, width=1280)
        #image = cv2.resize(img, (width, height))
        #resultImage = image.copy
        #imgpoly = cv2.rectangle(image,(46,46),(50,50),(255,255,255))
    resize = resizeWithAspectRatio(img, width=1280)
    cv2.imshow('image', resize)

    # setting mouse handler for the image
    # and calling the click_event() function

    # wait for a key to be pressed to exit
    if cv2.waitKey(33) == ord('q'):
        break

    # close the window
cv2.destroyAllWindows()