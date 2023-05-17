import cv2

# Load the pre-trained YOLOv3 model
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# Load the class labels
with open('coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Load the image
image = cv2.imread('"C:/Users/mohammed rafik m/OneDrive/Documents/computer vision/Picture1.jpg"')

# Create a blob from the image
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

# Set the input blob for the network
net.setInput(blob)

# Run forward pass and get the detections
detections = net.forward()

# Loop over the detections
for detection in detections:
    confidence = detection[5]
    if confidence > 0.5:
        class_id = np.argmax(detection[6:])
        if classes[class_id] == 'watch':
            # Extract the bounding box coordinates
            box = detection[0:4] * np.array([image.shape[1], image.shape[0], image.shape[1], image.shape[0]])
            (center_x, center_y, width, height) = box.astype("int")

            # Calculate the top-left corner of the bounding box
            x = int(center_x - (width / 2))
            y = int(center_y - (height / 2))

            # Draw the bounding box and label on the image
            cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)
            cv2.putText(image, 'Watch', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Display the image with detections
cv2.imshow('Object Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
