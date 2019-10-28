import PIL.Image # Python Image Library
import PIL.ImageDraw
import face_recognition # Face recognition library which gives us access to the face detection model in DLIB

# In this file, we will being using a pre-trained HOG face detector to detect all faces
# To perform face detection within this library, we just need to load an
# image file, and then run the image file through the model

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all the faces in the image
# This function will return a list of faces found in the image.
# If no face was found, the list will be empty.
# Each face that is returned will contain four points. These points are the pixel locations of the face in the image.
# Given as the top, right, bottom, and left coordinates.
face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

for face_location in face_locations:
    # Print the location of each face in this image. Each face is a list of co-ordinates
    # in (top, right, bottom, left) order.
    top, right, bottom, left = face_location # destructuring
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Let's draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")

# Display the image on screen
pil_image.show()
