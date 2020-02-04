def word_counts(data):
	split_tweets = [i.split() for i in data.text]
    word_number = [len(i) for i in split_tweets]
    word_lengths = [[len(j) for j in i] for i in split_tweets]
    mean_word_length = [np.mean(i) for i in word_lengths]
    max_word_length = [np.max(i) for i in word_lengths]
    min_word_length = [np.min(i) for i in word_lengths]
    std_word_length = [np.std(i) for i in word_lengths]
    
    counts = features = pd.DataFrame(np.array([mean_word_length,max_word_length,min_word_length,std_word_length]).T,
             columns=["Mean","Min","Max","Std"])
    
    return(counts)

def clean_tweets(data):
    print("Lets clean some tweets")
    # Clean Some Tweests
    clean_data = data
  
    return(clean_data)
