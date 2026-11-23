from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    name_0="X"
    score_0=0
    for name,score in scores:
        if score>score_0:
            name_0=name
            score_0=score
    return name_0


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
