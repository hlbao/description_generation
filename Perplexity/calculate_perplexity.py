def compute_perplexity(lang_trigram, test_doc):
    """Function that computes perplexity
    Input: Lang_trigram: Language model trigram
        Test_doc: Document to compute perplexity on
    Return: Perplexity of given document based on given 
            language model
    """
    sum_log_prob = 0
    length_counter = 0
    for i in range(len(test_doc)):
        for j in range(len(test_doc[i])-3):
            markov_hist = test_doc[i][j:j+2]
            key = test_doc[i][j+2]
            sum_log_prob += np.log2(lang_trigram[markov_hist][key])
            length_counter += 1
    Hm = (-1/length_counter)*sum_log_prob
    perplexity = 2**Hm
    return perplexity

# open the test document
with open('training.de') as f:
    test_doc = []
    big_test_line = ''
    for line in f:
        line = preprocess_line(line)
        big_test_line += line
        test_doc.append(line)


model_br_test_perplexity = compute_perplexity(
                            model_br_nested_trigrams_prob,test_doc)
print('model_br_test_perplexity: {:.1f}'
      .format(model_br_test_perplexity))

english_test_perplexity = compute_perplexity(
                            english_trigrams_prob,test_doc)
print('english_test_perplexity:{:.1f}'
      .format(english_test_perplexity))
