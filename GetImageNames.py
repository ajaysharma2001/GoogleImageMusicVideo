import json

with open('result.json') as f:
	data = json.load(f)

data = data['results']
words_list = []
words = {"words": []}

def PrettyData(my_json):
	print(json.dumps(my_json, indent = 4, sort_keys=True))

for key in data:
	words_list.extend(key['alternatives'][0]['words'])

words['words'] = words_list

with open('word_data.json', 'w') as outfile:
	json.dump(words, outfile, indent=4, sort_keys=True)
