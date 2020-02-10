import re

# Raw Strings (support)
LETTER = r'(M{1,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'\
		+ r'|M{0,4}(CM|C?D|D?C{1,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'\
		+ r'|M{0,4}(CM|CD|D?C{0,3})(XC|X?L|L?X{1,3})(IX|IV|V?I{0,3})'\
		+ r'|M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|I?V|V?I{1,3}))'

CENT_LETTER = r'(((s|S)iglo(s)?)|(s.))\s(({0}\,\s)*{0}\sy\s)?{0}'.format(LETTER)

# Regex
R_LETTER = re.compile(LETTER)
R_CENT_LETTER = re.compile(CENT_LETTER)
R_NUM = re.compile(r'\#?([0-9]+(\,|\.|\s|\:))*[0-9]+')
R_TAG = re.compile(r'\<.*?\>')
R_PARENTHESIS = re.compile(r'\(.*?\)')
R_FORMULA = re.compile(r'formula_([0-9])+')
ENTS = ('PER', 'LOC', 'ORG', 'MISC')
NUM_TOKEN = 'NUM'
FORMULA_TOKEN = 'FORM'
TOKENS = ENTS + (NUM_TOKEN, FORMULA_TOKEN)
TOKEN_THROW_RATIO = 0.5

LOG_FORMAT = '%(levelname)s (%(asctime)-15s) for %(funcName)s: %(message)s'

# Folders
MINED_FOLDER = 'mined/'
