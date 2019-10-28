## Face recognition as a multi-step pipeline
- Locate and extract faces from each image
- Identify face features in each image
- Align faces to match pose template
- Represent faces as measurements, encode faces using a trained neural network
- Compare to other faces, check euclidean distance between face encodings
	- Euclidean distance between faces
	- Distance rules
		- < 0.6 match
		- >= 0.6 not match

## Face Detection Algorithms
- Viola-Jones
	- Uses decision trees to detect faces based on light and dark areas
	- Very fast and great for low-powered devices
	- Not very accurate
- Histogram of oriented gradients (HOG)
	- Looks for the shift from light to dark areas in an image
	- Slower than Viola Jones, but more accurate
	- Runs well on normal computers without special hardware
	
	- HOG is a simplified representation of an image that still captures enough detail to detect faces
	- A HOG representation is not affected by a small change in lighting
	- A HOG representation is not affected by a small change in object's shape
- Convolutional neural network
	- Uses a deep learning algorithm (neural network) to detect faces
	- Very accurate, but needs a lot of training data
	- Runs best on computers with dedicated GPUs
	

## Automatic Face Landmark Estimation
- The same face landmark estimation model should work for any face
- However, models don't transfer to other domains. For example, a model trained on human faces doesn't work for cartoons.
- We can just use standard pre-trained model and it should work for all of our images. If you want to identify face landmarks in cartoons then we need to build a new model from scratch using cartoon faces as training data.

## Face Alignment
- Adjusting a raw face image so that key facial features (like nose, eyes, and mouth) line up with a predefined template.
- Processes:
	- Step1: detect face landmarks
	- Step2: calculate affine tranformation
		- Affine transformation: a linear mapping between sets of points where parallel lines will remain parallel. Basically, this means we can move, rotate, and stretch our image, but we cannot do more complex thing like twisting or warping image.

## Why do we need to align face images?
- Different people's heads will be rotated in different ways in different photos.
- Correcting for head angle and rotation will make our face recognition system more accurate.


## Face Encodings
- Comparing faces directly among known faces and unknown faces
	- Too slow
	- Doesn't capture the structure of each face
- Representing faces as measurements
	- The size of the checkbones
	- The width of the mouth
	- So on
- The process of taking an image of a face and turning it to a set of measurements
- A real face-encoding system will capture a large number of face measurements (typically 128 or more)
- Instead of trying to decide on 128 ways to measure a face, we'll use machine learning to create those measurements.

## How to measure faces
- Deep metric learning
	- Using deep learning to have a computer come up with a way to measure something that you don't know how to measure yourself. 
- Encoding faces with a trained model
	- an face image -> face encoding model -> a set of 128 measurements
- When we write the code for our face recognition system, we'll be using a pre-trained model instead of training a new one.

## What do the Face Measurements mean?
- We don't know!
- Model interpretability is a common problem in machine learning
- When models are hard to interpret, they can often have hidden biases. Watch out for it!
- They don't perform equally well for all people. They are just a reflection of the data that they were trained on, and the data sets are almost never fair representations of the real world. 

## Euclidean distance
- The distance between two points in space along a straight line.
- Face Distance Threshold
	- Set a face maximum distance that is still considered the same face. By default, 0.6.
	- If distance(a, b) > 0.6, then not a match
	- If distance(a, b) <= 0.6, then they match
	- The lower the distance, the better they match
	- Distance(a, b) = square root of ((a1-b1)^2 + (a2-b2)^2 + (a3-b3)^2)
- Advantages
	- Fast to calculate and easy to parallelize
	- Works nicely with other common machine learning algorithms, list k-nearest neighbors (KNN)
	- Make it easy to store and query face measurements using a standard database











































