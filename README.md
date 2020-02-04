# MLClubNLP
Natural Langauge Processing using Disaster Tweets

To load the cleaning functions into a Jupyter notebook, drop the following line into the notebook:

`%load https://raw.githubusercontent.com/tipthederiver/MLClubNLP/master/clean.py`


## To Do:

### Data Cleaning:

Build a function that takes training or test data and:


|Task|Creator|Delegate|Status|
|-|-|-|-|
|Convert to lowercase|-|Zheying|-|
|Remove punctutaion, replace with blank space|-|Zheying|-|
|Find/implament a word standardization list (eg "Standard Deviation" to "std")|-|Shuo|-|
|Run spell checker|-|Nate|-|
|Create list of hashtags, add to training, add feature with hashtag count|-|Nate|Done|
|Remove @names|-|Zheying|-|
|Remove URL's but note they are there|-|Ruobing|-|
|Clean the those location values that are not real locations|Zheying|-|-|
|Construct unique word feature, listing only words not in 1000 most common words|Nate|-|-|
|Remove Emojis|Zheying|-|-|
|Remove all charaters that are not english|All|-|-|

Function should return a data frame with the following features

|cleaned text|locations|key words|hashtags|hashtag count|url count|All Caps|Uncommon Words|
|-|-|-|-|-|-|-|-|
|string|string|string|string|int|int|binary|string|


### Build Model:

Model should act as RNN/BERT on cleaned text, RNN/BERT on the Uncommon Words, and classifier on other data. 
