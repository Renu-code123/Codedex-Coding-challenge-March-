###Cherry Blossoms 🌸
def cherry_blossoms(temps):
    n = len(temps)
    
    # If less than 5 days → impossible
    if n < 5:
        return -1
    
    # Initial window sum (first 5 days)
    window_sum = sum(temps[:5])
    
    # Check first window
    if window_sum / 5 > 15:
        return 5  # day number (1-indexed)
    
    # Slide the window
    for i in range(5, n):
        window_sum += temps[i]      # add next day
        window_sum -= temps[i - 5]  # remove old day
        
        if window_sum / 5 > 15:
            return i + 1  # 1-indexed day
    
    return -1
