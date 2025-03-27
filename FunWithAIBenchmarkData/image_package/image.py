# File Name: image.py
# Student Name: Colton Ramsey, Lucas Iceman, Zach Bell
# email: ramseyc6@mail.uc.edu, icemanlc@mail.uc.edu, bellzj@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: 03/25/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Modify a VS Python project to add some data visualization.

# Brief Description of what this module does: This module creates a function to be called in the main that opens up 
# the image of Blastoise the pokemon.
# Citations: ChatGPT to understand how to show an image.
# Anything else that's relevant: None


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
def blastoise(file_path):
	img = mpimg.imread(file_path)  # Replace with your image path
	plt.imshow(img)
	plt.axis('off')  # Hide axes
	plt.show()