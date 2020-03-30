import re
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize, WhitespaceTokenizer, TweetTokenizer
np.random.seed(seed=234)
# The below reads in N lines of text from the 40-million-word news corpus I used (provided by SwiftKey for educational purposes) and divides it into training and test text.
N = 100000
with open("news.txt") as myfile:
    all_articles = [next(myfile) for x in range(N)]
articles = all_articles[0:75000]
test_articles = all_articles[75000:N]
joined_articles = [" ".join(articles)]
joined_test_articles = [" ".join(test_articles)]
# The below takes out apostrophes (don't becomes dont), replacing anything that's not a letter with a space. Any single letter that is not the pronoun "I" or the article "a" is also replaced with a space, even at the beginning or end of a document.
def clean_article(article):
    art0 = re.sub("'", '', article)
    art1 = re.sub("[^A-Za-z]", ' ', art0)
    art2 = re.sub("\s[B-HJ-Zb-hj-z]\s", ' ', art1)
    art3 = re.sub("^[B-HJ-Zb-hj-z]\s", ' ', art2)
    art4 = re.sub("\s[B-HJ-Zb-hj-z]$", ' ', art3)
    return art4.lower()
# The below breaks up the training words into n-grams of length 1 to 5 and puts their counts into a Pandas dataframe with the n-grams as column names.  The maximum number of n-grams can be specified if a large corpus is being used.  The penultimate line can be used to limit the n-grams used to those with a count over a cutoff value.
ngram_bow = CountVectorizer(stop_words = None, preprocessor = clean_article, tokenizer = WhitespaceTokenizer().tokenize, ngram_range=(1,5), max_features = None, max_df = 1.0, min_df = 1, binary = False)
ngram_count_sparse = ngram_bow.fit_transform(joined_articles)
ngram_count = pd.DataFrame(ngram_count_sparse.toarray())
ngram_count.columns = ngram_bow.get_feature_names()
sums = ngram_count.sum(axis = 0)
sums = sums[sums > 2]
ngrams = list(sums.index.values)
# The below similarly breaks up the test words into n-grams of length 5.
test_bow = CountVectorizer(stop_words = None, preprocessor = clean_article, tokenizer = WhitespaceTokenizer().tokenize, ngram_range=(5,5), max_features = None, max_df = 1.0, min_df = 1, binary = False)
ngram_count_sparse_test = test_bow.fit_transform(joined_test_articles)
test_ngram_count = pd.DataFrame(ngram_count_sparse_test.toarray())
test_ngram_count.columns = test_bow.get_feature_names()
test_sums = test_ngram_count.sum(axis = 0)
test_sums = test_sums[test_sums > 1]
test_ngrams = list(test_sums.index.values)
# The helper functions below give the number of occurrences of n-grams in order to explore and calculate frequencies
def number_of_unique_ngrams(n, ngrams):
    grams = 0
    for ng in ngrams:
        ng_split = ng.split(" ")
        if len(ng_split) == n:
            grams += 1
    return grams
def number_of_ngrams(n, ngrams):
    grams = 0
    for ng in ngrams:
        ng_split = ng.split(" ")
        if len(ng_split) == n:
            grams += sums[ng]
    return grams
def base_freq(n, ngrams):
    tot_ngrams = number_of_ngrams(n, ngrams)
    freqs = pd.Series()
    for ng in ngrams:
        ng_split = ng.split(" ")
        if len(ng_split) == n:
            freqs[ng] = sums[ng] / tot_ngrams
    return freqs
# For use in later functions so as not to re-calculate multiple times:
bf = base_freq(1, ngrams)
# The function below finds any n-grams that are completions of a given prefix phrase with a specified number (could be zero) of words 'chopped' off the beginning.  For each, it calculates the count ratio of the completion to the (chopped) prefix, tabulating them in a series to be returned by the function.  If the number of chops equals the number of words in the prefix (i.e. all prefix words are chopped), the 1-gram base frequencies are returned.
def find_completion_scores(prefix, chops, factor = 0.4):
    cs = pd.Series()
    prefix_split = prefix.split(" ")
    l = len(prefix_split)
    prefix_split_chopped = prefix_split[chops:l]
    new_l = l - chops
    if new_l == 0:
        return factor**chops * bf
    prefix_chopped = ' '.join(prefix_split_chopped)
    for ng in ngrams:
        ng_split = ng.split(" ")
        if (len(ng_split) == new_l + 1) and (ng_split[0:new_l] == prefix_split_chopped):
            cs[ng_split[-1]] = factor**chops * sums[ng] / sums[prefix_chopped]
    return cs
# The below tries different numbers of 'chops' up to the length of the prefix to come up with a (still unordered) combined list of scores for potential completions of the prefix.
def score_given(given, fact = 0.4):
    sg = pd.Series()
    given_split = given.split(" ")
    given_length = len(given_split)
    for i in range(given_length+1):
        fcs = find_completion_scores(given, i, fact)
        for i in fcs.index:
            if i not in sg.index:
                sg[i] = fcs[i]
    return sg
#The below takes the potential completion scores, puts them in descending order and re-normalizes them as a pseudo-probability (from 0 to 1).
def score_output(given, fact = 0.4):
    sg = score_given(given, fact)
    ss = sg.sum()
    sg = sg / ss
    sg.sort_values(axis=0, ascending=False, inplace=True)
    return sg