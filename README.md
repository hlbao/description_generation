# description_generation

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

Using a package 'Spacy Model: https://spacy.io/' it provides different language which has not been decided. $pip install -U spacy

-----------Update3_Evolutionary_Search----------------------------------------------------------------------------------------
