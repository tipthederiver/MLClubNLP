# MLClubNLP
Natural Langauge Processing using Disaster Tweets

To load the cleaning functions into a Jupyter notebook, drop the following line into the notebook:

`%load https://raw.githubusercontent.com/tipthederiver/MLClubNLP/master/clean.py`


## To Do:

### Data Cleaning:

Build a function that takes training or test data and:


|Task|Creator|Delegate|Status|
|-|-|-|-|
|Convert to lowercase|-|-|-|
|Remove punctutaion, replace with blank space|-|-|-|
|Find/implament a word standardization list (eg "Standard Deviation" to "std")|-|-|-|
|Run spell checker|-|-|-|
|Create list of hashtags, add to training, add feature with hashtag count|-|Nate|Done|
|Remove @names|-|-|-|
|Remove URL's but note they are there|-|-|-|
|Clearn the those location values that are not real locations|Zheying|-|-|

Function should return a data frame with the following features

|cleaned text|locations|key words|hashtags|hashtag count|url count|All Caps|Uncommon Words|
|-|-|-|-|-|-|-|-|
|string|string|string|string|int|int|binary|string|


### Build Model:

Model should act as RNN/BERT on cleaned text, RNN/BERT on the Uncommon Words, and classifier on other data. 
