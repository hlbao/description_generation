# Importing modules
import pandas as pd
import os
os.chdir('..')
# Read data into papers
papers = pd.read_csv('./data/NIPS Papers/papers.csv')
# Print head
papers.head()
# sample only 2 - for demonstration purposes
papers = papers.sample(2)
# Print out the first rows of papers
papers.head()
