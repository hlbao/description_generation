import re

# Raw Strings ROMA CHARS (support)
ROMAN = r'(M{1,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'\
		+ r'|M{0,4}(CM|C?D|D?C{1,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'\
		+ r'|M{0,4}(CM|CD|D?C{0,3})(XC|X?L|L?X{1,3})(IX|IV|V?I{0,3})'\
		+ r'|M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|I?V|V?I{1,3}))'

CENT_ROMAN = r'(((s|S)iglo(s)?)|(s.))\s(({0}\,\s)*{0}\sy\s)?{0}'.format(ROMAN)

R_ROMAN = re.compile(ROMAN)
R_CENT_ROMAN = re.compile(CENT_ROMAN)
R_NUM = re.compile(r'\#?([0-9]+(\,|\.|\s|\:))*[0-9]+')
R_TAG = re.compile(r'\<.*?\>')
R_PARENTHESIS = re.compile(r'\(.*?\)')
R_FORMULA = re.compile(r'formula_([0-9])+')

# Spacy Model: https://spacy.io/

#langeage selection
#ES_MODEL = 'es_core_news_md'
# Spanish multi-task CNN trained on the AnCora and WikiNER corpus. Assigns context-specific token vectors, POS tags, dependency parse and named entities. Supports identification of PER, LOC, ORG and MISC entities.


#EN_MODEL = 'en_core_web_md'


ENTS = ('PER', 'LOC', 'ORG', 'MISC')

NUM_TOKEN = 'NUM'
FORMULA_TOKEN = 'FORM'
TOKENS = ENTS + (NUM_TOKEN, FORMULA_TOKEN)
TOKEN_THROW_RATIO = 0.5
LOG_FORMAT = '%(levelname)s (%(asctime)-15s) for %(funcName)s: %(message)s'
MINED_FOLDER = 'mined/'
CLEANED_FOLDER = 'cleaned/'#see documents in github
