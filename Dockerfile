FROM python:3.6-slim

RUN apt-get update


# Spacy
RUN apt-get install -y build-essential
RUN pip install spacy
RUN python -m spacy download es_core_news_md

# Others
RUN pip install unidecode

# For Development
WORKDIR /usr/src
CMD bash
