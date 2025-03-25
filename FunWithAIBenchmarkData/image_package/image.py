import matplotlib.pyplot as plt
import matplotlib.image as mpimg
 
def blastoise(file_path):
	img = mpimg.imread(file_path)  # Replace with your image path
	plt.imshow(img)
	plt.axis('off')  # Hide axes
	plt.show()