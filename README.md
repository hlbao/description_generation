# TextGeneration

------------------DateReader--------------------------------------------------------------------------------------------------

1. Data Reader is a program that reads data items from a files (here linguistic corpora, perticularly wikipedia extractor sets) into machine learning + evolutionary computation program, and creates training/testing examples. This part of the project is just to make sure that you find your actual data and have a program that can interact with your data: Read the data from a folders/files and have your data items in the form of learning examples. Depending on how clean/structured is your data this step might need a bit of work for you.

2. Notice in this data-reader repository, we just focus on the reading+mining of data from wiki. It definitely needs more efforts to do cleaning or structured operations. So far we have not implemented that, but we will work on this during the entire cycle of this project.

3. This repository includes two parts, the first is a Wikipedia crawler, mainly through BeautifulSoup (aka bs4 to extract information) and requests library. The second one is mining and pre-processing documents. The output is wikiextractor/extracted/originaltext.

4. Next two parts are 1. put processed data into structured machine learning to classify/clean; 2. put classified data to evolutionary algorithm program to generate text, we will updata as the processing of the project.

5. 
