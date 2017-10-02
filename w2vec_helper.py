from collections import Counter


def create_lookup_tables(text):
    """
    Create lookup tables for vocabulary
    :param text: The text of tv scripts split into words
    :return: A tuple of dicts (vocab_to_int, int_to_vocab)
    """
   
    counts = Counter(text)
    vocab = sorted(counts, key=counts.get, reverse=True)
    int_to_vocab = {ii: word for ii, word in enumerate(vocab)}
    vocab_to_int = {word: ii for ii, word in int_to_vocab.items()}
    
    return (vocab_to_int,int_to_vocab)
    
    
def token_lookup():
    """
    Generate a dict to turn punctuation into a token.
    :return: Tokenize dictionary where the key is the 
     punctuation and the value is the token
    """
    
    dictionary = {'.': "||Period||",\
                  ',': "||Comma||",\
                  '"': "||Quotation_Mark||",
                  ';': "||Semicolon||",
                  '!': "||Exclamation_Mark||",
                  '?': "||Question_Mark||",
                  '(': "||Left_Parentheses||",
                  ')': "||Right_Parentheses||",
                  '--': "||Dash||",
                  '\n': "||Return||"}
    
    
    return dictionary
    
    
def preprocess(text):

    # Replace punctuation with tokens so we can use them in our model
    
    text = text.lower()
    text = text.replace('.', ' <PERIOD> ')
    text = text.replace(',', ' <COMMA> ')
    text = text.replace('"', ' <QUOTATION_MARK> ')
    text = text.replace(';', ' <SEMICOLON> ')
    text = text.replace('!', ' <EXCLAMATION_MARK> ')
    text = text.replace('?', ' <QUESTION_MARK> ')
    text = text.replace('(', ' <LEFT_PAREN> ')
    text = text.replace(')', ' <RIGHT_PAREN> ')
    text = text.replace('--', ' <HYPHENS> ')
    text = text.replace('?', ' <QUESTION_MARK> ')
    
    
    # text = text.replace('\n', ' <NEW_LINE> ')
    text = text.replace(':', ' <COLON> ')
    words = text.split()
    
    
    # Remove all words with  5 or fewer occurences
    word_counts = Counter(words)
    trimmed_words = [word for word in words if word_counts[word] > 5]

    return trimmed_words    
        