##

def streak_counter(games):
    current_streak = 0
    max_streak = 0
    for game in games:
        if game == "W":
            current_streak += 1
        elif game == "L":
            current_streak = 0
        max_streak = max(max_streak, current_streak)
    return max_streak
