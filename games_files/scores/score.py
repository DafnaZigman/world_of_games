

def add_score(difficulty):
    points_of_wining = (difficulty * 3) + 5

    from games_files.scores.utils import scores_file_name, bad_return_code

    try:
        with open(scores_file_name, "r") as f:
            score = int(f.read())
    except:
        score = 0
    score += points_of_wining
    with open(scores_file_name, "w") as f:
        f.write(str(score))
    return score

