# Surveillance-Vision
Have you ever wanted to detect human faces with your webcam? Have you ever wanted to save timestamped snapshots of people sitting in front of your computer?  Have you ever wanted to be able to shut down such a program with a rad hand gesture?

No?! Well, here you get it anyways.

This project is written in Python and is dependent on Numpy and OpenCV, both freely available libraries. We'll also be utilizing two different sets of Haar Cascades -- one for human faces and one for a closed fist.

A Haar Cascade is simply a classifier we can use to detect a specific object.

The Haar Cascade is by superimposing the positive image over a set of negative images. The training is generally done on a server and on various stages. Better results are obtained by using high quality images and increasing the amount of stages for which the classifier is trained. You can either choose to create your own Haar Cascade, which would require you to collect thousands of images and find a server to train it on, or you can just use the ones in this project.



