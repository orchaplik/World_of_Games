def add_score(diff):
    points_of_winning = (diff * 3) + 5
    print(f"you won {points_of_winning}")
    return points_of_winning


def read_score(diff):
    with open('scores.txt') as f:
        lines = f.readlines()
    pass
