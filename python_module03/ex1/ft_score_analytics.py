import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    scores_len = len(sys.argv[1:])
    scores: list[int] = []
    for score in sys.argv[1:]:
        try:
            scores.append(int(score))
        except Exception as e:
            print(e)

    if len(scores) < 1:
        print(
            "No scores provided. Usage: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
            )
    else:
        total_score = sum(scores)
        max_score = max(scores)
        min_score = min(scores)

        print(f"Total playsers: {scores_len}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {total_score / scores_len:.1f}")
        print(f"High score: {max_score}")
        print(f"Low score: {min_score}")
        print(f"Score range: {max_score - min_score}")
