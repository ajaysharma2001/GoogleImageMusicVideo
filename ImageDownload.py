from google_images_download import google_images_download
import json

with open('word_data.json') as f:
	data = json.load(f)

data_list = data['words']
word_list = []

for item in data_list:
	word_list.append(item['word'])


response = google_images_download.googleimagesdownload()   
"""
arguments = {"keywords":"b","limit":1,"print_urls":True, "format":'jpg'}
paths = response.download(arguments)
print(paths)
print(({word_list[1]: []}, 0) == paths)
({'b': []}, 0)
"""

for word in word_list:
	limit = 1
	paths = ({word: []}, 0)
	while paths == ({word: []}, 0):
		arguments = {"keywords":word,"limit":limit,"print_urls":True, "format":'jpg', "exact_size":'1920, 1080'}
		paths = response.download(arguments)
		print(paths)
		limit = limit + 1
	limit = 1


