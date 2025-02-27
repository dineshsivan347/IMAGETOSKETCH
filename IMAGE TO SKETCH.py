import cv2
import os
import pygame.camera

def conv(inputfile, outputfile):
    image = cv2.imread(inputfile)
    if image is None:
        print("Error: Unable to open file:", inputfile)
        return

    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (19, 19), 0)
    invertedblur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    cv2.imwrite(outputfile, sketch)

def count_files_in_directory(directory):
    return len(os.listdir(directory))

#main
# initializing the camera
pygame.camera.init()
# make the list of all available cameras
camlist = pygame.camera.list_cameras()
# Using the function
directory = (r'C:\Users\Public\Documents')
file_count = count_files_in_directory(directory)
print(f'The number of files in the {directory} directory is: {file_count//2}')

input_file = r"C:\\Users\\Public\\Documents\\Filename" + f"{file_count//2}.jpg"
output_file = r"C:\\Users\\Public\\Documents\\sketch" + f"{file_count//2}.png"

# if camera is detected or not
# Open the camera
cap = cv2.VideoCapture(0)

# Initialize the image capture flag
image_captured = False

while True:
    # Check for the 's' key to capture the image
    if cv2.waitKey(1) & 0xFF == ord('s'):
        # Save the image to a file
        cv2.imwrite(input_file, frame)

        # Check if the image was saved correctly
        if os.path.exists(input_file):
            print("Image saved to:", input_file)

            # Convert the captured image
            conv(input_file, output_file)

            # Set the image capture flag
            image_captured = True

        # Break the loop
        break
    # Check for the 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

        # Exit the while loop
        break

    # Capture frame-by-frame
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    # Display the frame
    cv2.imshow('Camera Preview', frame)



# Check if the image was capture
if image_captured:
    print("Image captured and saved to:", input_file)

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

