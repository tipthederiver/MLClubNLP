# MLClubNLP
Natural Langauge Processing using Disaster Tweets

https://www.kaggle.com/c/nlp-getting-started/data

To load the cleaning functions into a Jupyter notebook, drop the following line into the notebook:

`%load https://raw.githubusercontent.com/tipthederiver/MLClubNLP/master/clean.py`


## To Do:

### Data Cleaning:

Build a function that takes training or test data and:


|Task|Creator|Delegate|Status|
|-|-|-|-|
|Convert to lowercase|-|Zheying|Done|
|Remove punctutaion, replace with blank space|-|Zheying|Done|
|Find/implament a word standardization list (eg "Standard Deviation" to "std")|-|Shuo|-|
|Run spell checker|-|Nate|-|
|Create list of hashtags, add to training, add feature with hashtag count|-|Nate|Done|
|Remove @names|-|Zheying|Done|
|Remove URL's but note they are there|-|Ruobing|Done|
|Clean the those location values that are not real locations|Zheying|-|-|
|Construct unique word feature, listing only words not in 1000 most common words|Nate|-|Done|
|Remove Emojis|Zheying|-|Done|
|Remove all charaters that are not english|All|-|-|
|Number of misspelled words| Juan |-|-|

Function should return a data frame with the following features

|cleaned text|locations|key words|hashtags|hashtag count|url count|All Caps|Uncommon Words|Number of Mispelled|
|-|-|-|-|-|-|-|-|-|
|string|string|string|string|int|int|binary|string|number|


### Build Model:

Model should act as RNN/BERT on cleaned text, RNN/BERT on the Uncommon Words, and classifier on other data. 
http://karpathy.github.io/2015/05/21/rnn-effectiveness/

Text Generation with RNN's
https://machinelearningmastery.com/develop-character-based-neural-language-model-keras/

Encodings: 

|Encodings Type|Classifier|Creator|Delegate|Status|
|-|-|-|-|-|
|Bag of words | Deep NN| Juan | - |-|
|Tokenization | Word Level RNN| Nate|-|-|
|One Hot Encodings| Character Level RNN | Zheying | -| -|
|One Hot Encodings| Character Level CNN | Nate | - | - |
