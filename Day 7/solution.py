##Ring Ring ☎️

import string
def find_unique_words(transcript):
    # convert to lowercase
    transcript = transcript.lower()
    
    # remove punctuation
    for p in string.punctuation:
        transcript = transcript.replace(p, "")
    
    # split words
    words = transcript.split()
    
    # get unique words using set
    unique_words = set(words)
    
    # return count
    return len(unique_words)
