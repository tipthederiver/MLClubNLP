def char_counts(data):
	split_tweets = [i.split() for i in data.text]
	word_number = [len(i) for i in split_tweets]
	word_lengths = [[len(j) for j in i] for i in split_tweets]
	mean_word_length = [np.mean(i) for i in word_lengths]
	max_word_length = [np.max(i) for i in word_lengths]
	min_word_length = [np.min(i) for i in word_lengths]
	std_word_length = [np.std(i) for i in word_lengths]
    
	counts = pd.DataFrame(np.array([word_number, mean_word_length,max_word_length,min_word_length,std_word_length]).T,
             columns=["Word Numb", "Char Mean","Char Min","Char Max","Char Std"])
    
	return(counts)

def find_hash(data):
	# Expects a dataframe with a .text column containing the tweets
	# Find hash returns a dataframe with two columns, one for each tweet:: 
	# Hashtags - a string containing the hashtags seperated by spaces
	# Hashcount - the number of hashtags in the tweet
    
	hashtags = [re.findall(r"#(\w+)", i) for i in data.text]
	hashstring = [' '.join(i) for i in hashtags]
	num_hashtags = [len(i) for i in hashtags]
    
	hash_dict = {"Hashtags": hashstring, "Hashcount": num_hashtags}
	hashinfo = pd.DataFrame(hash_dict)
    
	return(hashinfo)

def clean_tweets(data):
	print("Lets clean some tweets")
	# Clean Some Tweests
	clean_data = data
  
	return(clean_data)
