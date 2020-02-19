import argparse
import io
import json
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict

credentials = service_account.Credentials.from_service_account_file("api-key.json")

def transcribe_file_word_time_offsets(speech_file, language):
		print("Start")

		from google.cloud import speech
		from google.cloud.speech import enums
		from google.cloud.speech import types

		client = speech.SpeechClient(credentials = credentials)

		with io.open(speech_file, 'rb') as audio_file:
			content = audio_file.read()

		audio = types.RecognitionAudio(content = content)

		config = types.RecognitionConfig(
			encoding = enums.RecognitionConfig.AudioEncoding.FLAC,
			language_code = language,
			enable_word_time_offsets = True)

		response = client.recognize(config, audio)

		result_json = MessageToJson(response)

		with open('data.json', 'w') as outfile:
			json.dump(result_json, outfile)

		result_json = MessageToDict(response)
		with open("result.json", "w") as jsonFile:
			json.dump(result_json, jsonFile, indent=4, sort_keys=True)
		
if __name__ == '__main__':
    transcribe_file_word_time_offsets("mono.flac", "en-US")