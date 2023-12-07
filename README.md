# Downloading Google Image Results Automatically
Given a search prompt, this program automatically downloads a specified number of search results from google images into a specified folder(runs on firefox). However, the HTML of the Google Image Search page updates frequently so you have to dig into the HTML to find the right Xpath. 
/_

The imager.py file contains main which grabs the image query data. 
/_

crawler.py contains the crawler class which sets the driver, locates the iamge URL, and retrieves the images.
