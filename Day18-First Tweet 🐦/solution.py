###
def tweet_balance(tweet):
    if not tweet:
        return 140
    
    words = tweet.split()
    total = 0
    
    for word in words:
        if word.startswith('@'):
            total += 20
        elif word.startswith('http://') or word.startswith('https://'):
            total += 23
        else:
            total += len(word)
    
    # add spaces only if words exist
    total += max(0, len(words) - 1)
    
    return 140 - total
