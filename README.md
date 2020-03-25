# description_generation

general description:

What is text generation, in terms of Artificial Intelligence?

The creation of grammatically correct text in the same domain of the original globally, but with different meaning or content to each of the texts individually. In this context the domain is the set of semantic field, form of writing, length of texts, etc.

Mining

Data mining will represent the automation part. The goal would be to obtain a considerable amount (on the order of hundreds of thousands) of text samples. Each text, to facilitate the preparation of the pilot test, will consist of simple sentences. These phrases in turn will go through a process of filtering, cleaning and simplification.

Learning

Train a model whose input is n words where n is the expected word, or expected output. It, in other words, must learn which is the next most likely word given a sequence of words. So we apply classification and n-gram model. A key design decision is how long the input sequences should be. They need to be long enough to allow the model to learn the context for the words to predict. This input length will also define the length of seed text used to generate new sequences when we use the model.
With enough time and resources, we could explore the ability of the model to learn with differently sized input sequences. But for now, we will pick a length of 50 words for the length of the input sequences, somewhat arbitrarily. Details see classification.py


Search

Finally, we are faced with the concept of optimization. We will have to implement a search algorithm which selects and properly orders words from the generated vocabulary in order to achieve coherent and coherent sentences.
so, we use evolutionary search for generation (so far have not finished). Choose a path by browsing the words in the dictionary until you find a phrase. This means that, given a word, just an example, the three most probable words are selected to be the second word (9 different possibilities in the second step). This continues until we find the reserved word in our vocabulary that leads to the end of the sequence or phrase (EOL, from the English End Of Line).


------Update1_DateReader------------------------------------------------------------------------------------------------------

Data Reader is a program that reads data items from a files (here linguistic corpora, perticularly wikipedia extractor sets) into machine learning + evolutionary computation program, and creates training/testing examples. This part of the project is just to make sure that you find your actual data and have a program that can interact with your data: Read the data from a folders/files and have your data items in the form of learning examples. Depending on how clean/structured is your data this step might need a bit of work for you.

Notice in this data-reader repository, we just focus on the reading+mining of data from wiki. It definitely needs more efforts to do cleaning or structured operations. So far we have not implemented that, but we will work on this during the entire cycle of this project.

This repository includes two parts, the first is a Wikipedia crawler, mainly through BeautifulSoup (aka bs4 to extract information) and requests library. The second one is mining and pre-processing documents. The output is wikiextractor/extracted/originaltext.

Next two parts are 1. put processed data into structured machine learning to classify/clean; 2. put classified data to evolutionary algorithm program to generate text, we will updata as the processing of the project.

Set Up environment

cd descriptiongeneration/text

docker build -t descriptiongeneration .

Run for Development

docker run -it -v .../descriptiongeneration:/usr/src descriptiongeneration bash

Steps

Inside text folder

cd usr/src/text

notice wikiextractor can also used through https://github.com/attardi/wikiextractor.git and 

wget http://download.wikimedia.org/eswiki/latest/eswiki-latest-pages-articles.xml.bz2

The first update see wikiextractor.py, mine.py (mining sentences from extracted wiki data), and mined.zip (mined data).

----------Update2_Date_Clean--------------------------------------------------------------------------------------------------

TODO:

Refactor mine.py, clean.py

For the second update, see clean.py, cleaned.zip (cleaned data), contants.py (aiming to remove special char).

documentcovert.py is just a small programe for converting text to csv.

Using a package 'Spacy Model: https://spacy.io/' it provides different language which has not been decided. 

$pip install -U spacy

-----------Update2_Basic_Classificaition--------------------------------------------------------------------------------------

Previously using vector to represent everything. Idea is using TF-IDF to exract key words. Split: Test set (30%), Training set (70%). Accuracy: 71.54%, however, I noticed this is wrong.


