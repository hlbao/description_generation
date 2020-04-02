# Importing modules
import pandas as pd
import os
import re


os.chdir('..')
# Read data into papers
paper = pd.read_csv('./dataset1and2/paper.csv')
# Print head
paper.head()
# sample only 2 - for demonstration purposes
paper = paper.sample(2)
# Print out the first rows of papers
papers.head()
