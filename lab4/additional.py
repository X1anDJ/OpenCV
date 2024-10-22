import cv2

# Load images
image1 = cv2.imread('mountain1.png')
image2 = cv2.imread('mountain2.png')

# ORB Detector
orb = cv2.ORB_create()
keypoints1, descriptors1 = orb.detectAndCompute(image1, None)
keypoints2, descriptors2 = orb.detectAndCompute(image2, None)

# FLANN Matcher for ORB
FLANN_INDEX_LSH = 6
index_params = dict(algorithm=FLANN_INDEX_LSH, table_number=6, key_size=12, multi_probe_level=1)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Find matches and apply ratio test
matches = flann.knnMatch(descriptors1, descriptors2, k=2)
good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

# Draw matches
image_matches = cv2.drawMatches(image1, keypoints1, image2, keypoints2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display the result
cv2.imshow('ORB Matches', image_matches)
cv2.waitKey(0)
cv2.destroyAllWindows()
