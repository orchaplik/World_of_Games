
scores_path = "scores.txt"


def read_score():
    with open(scores_path) as f:
        line = f.readline()
    return line


def add_score(diff):
    curr_score = read_score()
    points_of_winning = ((diff * 3) + 5)
    mew_score = int(curr_score) + points_of_winning
    print(f"your points are {mew_score}")
    with open(scores_path, 'w') as f:
        f.write(f"{mew_score}")
    return mew_score
