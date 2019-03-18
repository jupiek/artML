##Pix2Pix Extension

Web Scraping :
	Data scraped from Google Images
	
Generate Training/Validation/Test Dataset :
	image-format.py - transform images to jpeg, adjust size to 286 by 286
			- parameters: dataset, folder directory, new folder directory
	edge_detection.ipynb - generate edges of dataset (creates image B)
	combine_AandB.py (located in AWS) - complete the image to edge training set.
	split.py - split dataset to training, validation,test datasets (default ratio = 0.6,0.2,0.2)

Run:
  pix2pix-keras.ipynb - specify which dataset you want to train on
