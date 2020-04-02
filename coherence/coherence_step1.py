# Importing modules
import pandas as pd
import os
import re
import gensim

from gensim.utils import simple_preprocess

os.chdir('..')
# Read data into papers
paper = pd.read_csv('./dataset1and2/paper.csv')

# sample only 2 - for demonstration purposes
paper = paper.sample(2)


def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))  # deacc=True removes punctuations
data = papers.paper_text_processed.values.tolist()
data_words = list(sent_to_words(data))
print(data_words[:1])

