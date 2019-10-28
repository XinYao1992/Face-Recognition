import face_recognition

# Load the jpg files into numpy arrays
image = face_recognition.load_image_file("a_man_face.jpg")

# Generate the face encodings
# The returned value of this function is an array. Each element in the array represents one face that was found in the
# image. The entry of each face contains another array with a 128 elements. These 128 elements are the face encoding
# that represents this unique face.
face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    # No faces found in the image.
    print("No faces were found.")

else:
    # Grab the first face encoding
    first_face_encoding = face_encodings[0]

    # Print the results
    print(first_face_encoding)
