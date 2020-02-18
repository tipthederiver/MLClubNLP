import numpy as np
import pandas as pd

def word_encoder(clean_text,targets,frac=.8):
    ## Train-test split:
    train_df = clean_text.sample(frac = frac, replace=False)
    y_train = targets.iloc[train_df.index]
    
    test_df = clean_text.drop(train_df.index)
    y_test = targets.drop(train_df.index)
    
    # Construct Word List
    wordvector_tr = [s.split() for s in list(train_df)]
    TRN_LEN = len(wordvector_tr)
    print("TRN_LEN:", TRN_LEN)

    wordvector_te = [s.split() for s in list(test_df)]
    TES_LEN = len(wordvector_te)
    print("TES_LEN:", TES_LEN)

    lens = [len(s.split()) for s in list(clean_text)]
    MAX_LEN = max(lens)
    print("MAX_LEN:", MAX_LEN)

    wordlist = sorted(list(set([w for s in list(clean_text) for w in s.split()])))
    print("First 5 Words:", wordlist[0:5])
    DIC_LEN = len(wordlist)
    print("DIC_LEN:", DIC_LEN)
    
    # Construct Dictionary
    word_indices = dict((c, i) for i, c in enumerate(wordlist))
    indices_word = dict((i, c) for i, c in enumerate(wordlist))
    
    # Construct Training and Test Sets
    x_train = np.zeros((TRN_LEN,MAX_LEN,DIC_LEN),dtype=np.bool)
    x_test = np.zeros((TES_LEN,MAX_LEN,DIC_LEN),dtype=np.bool)
    
    for i, sentance in enumerate(wordvector_tr):
        for t, word in enumerate(sentance):
            x_train[i,t, word_indices[word]] = 1
        
    for i, sentance in enumerate(wordvector_te):
        for t, word in enumerate(sentance):
            x_test[i,t, word_indices[word]] = 1
            
    encode = {"data": [x_train, y_train, x_test, y_test],
              "word_indices": word_indices,
              "indices_word": indices_word,
              "TRN_LEN": TRN_LEN,
              "TES_LEN": TES_LEN,
              "MAX_LEN": MAX_LEN,
              "DIC_LEN": DIC_LEN,
              "indicies": train_df.index}
            
    return(encode)


filename = "/Users/Admin/Downloads/Kaggle Data/DisasterTweets/train.csv"
data = pd.read_csv(filename)
data.hist()

clean = clean_tweets(data)

encode = encode_words(clean['Cleaned'],data['target'])
[x_train,y_train,x_test,y_test] = encode["data"]

#### Example of decoding data:

print(data['text'].iloc[encode['indicies'][0]])
for i in range(encode["MAX_LEN"]):
    print(encode["indices_word"][np.argmax(x_train[0,i,:])])
