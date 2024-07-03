import glob
from typing import List, Dict,Set

FILES_POS = 'M03/data/aclImdb/train/pos/*.txt'
FILES_NEG = 'M03/data/aclImdb/train/neg/*.txt'
PUNCTUATION = ',.!()"\\/\'*,'
HTML = '<br />'

def clean_review(content):
    content = content.lower().replace(HTML, '')
    for punc in PUNCTUATION:
        content = content.replace(punc, '')
    return content


def load_review(files : List) -> List[Set]:
    files_to_read = glob.glob(files)
    dict_={}
    for file in files_to_read:
        with open(file, encoding='utf-8') as reader:
            content = reader.read()
        content = clean_review(content).split()
        content = set(content)
        for word in content:
            dict_[word] = dict_.get(word, 0) + 1
            
    return dict_
            


possitive_comms = load_review(FILES_POS)
negative_comms = load_review(FILES_NEG)

# Get user sentence to check
user_review = input("Enter statement that sentiment You wish to count: ")
user_review = user_review.lower().split()
#Get sentence sentiment
sentence_sentiment = 0
for word in user_review:
    pos_counter = possitive_comms.get(word, 0)
    neg_counter = negative_comms.get(word, 0)
    all_ = pos_counter + neg_counter
    if all_ !=0:
        word_sentiment = (pos_counter - neg_counter) / all_
        word_sentiment = round(word_sentiment, 2)
    else:
        word_sentiment = 0
    print(word, word_sentiment)
    
    sentence_sentiment += word_sentiment
sentence_sentiment /= len(user_review)
sentence_sentiment = round(sentence_sentiment, 2)


# Report

if sentence_sentiment > 0:
    label = 'positive'
elif sentence_sentiment <0:
    label = 'negative'
else:
    label = 'neutral'
print('---')
print(f'Sentence is {label}, sentiment = {sentence_sentiment}')