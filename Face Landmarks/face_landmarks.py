import PIL.Image
import PIL.ImageDraw
import face_recognition # give us access to face detection model & face landmark detection model in DLIB

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("people.jpg")

# Find all facial features in all the faces in the image
# The results of the function is the list that contains one entry for each face found in the image.
# If no face found in the image, this list would be empty.
# Each face will be a Python Dictionary Object:
# The keys of dictionary are the names of facial feature. Such as eye, right eye, chin.
# The value of dictionary are the list of X, Y coordinates of the points that correspond to that facial feature.
# For example, each eye is a list of a few points that trace a line from the end of the eye to another.
face_landmarks_list = face_recognition.face_landmarks(image)

number_of_faces = len(face_landmarks_list)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)

# Create a PIL drawing object to be able to draw lines later
draw = PIL.ImageDraw.Draw(pil_image)

# Loop over each face
for i in range(len(face_landmarks_list)):
    face_landmarks = face_landmarks_list[i]
    print("Person {}:".format(i + 1))

    # Loop over each facial feature (eye, nose, mouth, lips, etc)
    for name, list_of_points in face_landmarks.items():
        # Print the location of each facial feature in this image
        print("The {} in this face has the following points: {}".format(name, list_of_points))

        # Let's trace out each facial feature in the image with a line!
        draw.line(list_of_points, fill="red", width=2)
    print("\n")

pil_image.show()
