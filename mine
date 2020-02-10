import bz2
import os
import spacy

from constants
import MINED_FOLDER, LOG_FORMAT


def is_useful(doc, minlen=9, maxlen=18):
	"""Condition Function."""
	min_c = len(doc) >= minlen
	max_c = len(doc) <= maxlen
	upper_c = doc[0].text[0].isupper()
	end_c = doc.text.endswith(':\n') or doc.text.endswith(': \n')
	return min_c and max_c and upper_c and not end_c


def already_mined(folder_name):
	"""If mining process fails, this function will restart it."""
	file_name = folder_name + '.txt'
	return file_name in os.listdir(MINED_FOLDER) 


def mine_extracted(nlp, parent_folder_path='wikiextractor/extracted'):
	docs = []
	for folder_name in os.listdir(parent_folder_path):
		logging.info('INFO: Procesing text and selecting docs in {}... '.format(folder_name), end='', flush=True)
		if already_mined(folder_name):
			logging.info('Already mined'.format(folder_name))
		else:
			folder_path = '{}/{}'.format(parent_folder_path, folder_name)
			docs = mine_folder(nlp, folder_path)
			with open(MINED_FOLDER+folder_name+'.txt', 'w') as outputfile:
				for file_docs in docs:
					for doc in file_docs: 
						outputfile.write(str(doc))
			logging.info('Mine completed'.format(folder_name))


def mine_folder(nlp, folder_path='wikiextractor/extracted/originaltext'):
	docs = []
	for document_name in os.listdir(folder_path):
		document_path = '{}/{}'.format(folder_path, document_name)
		docs.append(mine_document(nlp, document_path))
	return docs


def mine_document(nlp, document_path='wikiextractor/extracted/originaltext/wiki_00.bz2'):
	docs = []
	with bz2.open(document_path, 'rt') as inputfile:
		line = inputfile.readline()
		while line:
			doc = nlp(line)
			if is_useful(doc):
				docs.append(doc)
			line = inputfile.readline()
	return docs


if __name__ == "__main__":
	logging.basicConfig(format=LOG_FORMAT, level=logging.DEBUG)

	mine_extracted(nlp)
