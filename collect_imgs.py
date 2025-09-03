import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

# Try with camera index 0 (default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("❌ Cannot open webcam. Try changing the index (0, 1, 2, ...)")

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'📸 Collecting data for class {j}')

    # Wait until user presses 'q' to start capturing for this class
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame. Check your camera connection.")
            break

        cv2.putText(frame, 'Ready? Press "Q" to start :)',
                    (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1.0, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Capture dataset_size images for this class
    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Failed to grab frame. Skipping...")
            continue

        cv2.imshow('frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        img_path = os.path.join(class_dir, f'{counter}.jpg')
        cv2.imwrite(img_path, frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
