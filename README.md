# Pix2Pix Urban Animals

Project 2: AI and Creativity

Web Scraping :
- Data scraped from Google Images
- https://github.com/hardikvasa/google-images-download
	
Generate Training/Validation Dataset :

- image-format.py 
	- transform images to jpeg, adjust size to 286 by 286
	- parameters: dataset, folder directory, new folder directory
- edge_detection.ipynb 
	- generate edges of dataset (creates image B)
- combine_AandB.py
	- https://github.com/phillipi/pix2pix
	- complete the image to edge training set.
- split.py - split dataset to training, validation datasets (default ratio = 0.8,0.2)

To run the code:
 Run pix2pix-keras.ipynb with a training data of edge2images generated from the previous steps.
