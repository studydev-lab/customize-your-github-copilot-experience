def summarize_scores(scores: list[int]) -> tuple[int, int, float]:
    valid_scores = [score for score in scores if 0 <= score <= 100]
    if not valid_scores:
        raise ValueError("No valid scores provided.")
    return min(valid_scores), max(valid_scores), sum(valid_scores) / len(valid_scores)


def add_or_update_student(
    records: dict[str, dict[str, object]],
    student_id: str,
    name: str,
    grade: int,
) -> None:
    records[student_id] = {"name": name, "grade": grade}


def get_student(records: dict[str, dict[str, object]], student_id: str) -> dict[str, object] | str:
    return records.get(student_id, "Student not found")


def compare_topics(student_a_topics: set[str], student_b_topics: set[str]) -> tuple[set[str], set[str], list[str]]:
    only_a = student_a_topics - student_b_topics
    only_b = student_b_topics - student_a_topics
    shared_sorted = sorted(student_a_topics & student_b_topics)
    return only_a, only_b, shared_sorted


def main() -> None:
    # Lists and tuples
    sample_scores = [95, 88, 120, 73, -4, 100]
    print("Score summary:", summarize_scores(sample_scores))

    # Dictionaries
    students: dict[str, dict[str, object]] = {}
    add_or_update_student(students, "S001", "Mina", 92)
    add_or_update_student(students, "S002", "Joon", 85)
    print("S001:", get_student(students, "S001"))
    print("S999:", get_student(students, "S999"))

    # Sets
    topics_a = {"lists", "tuples", "dictionaries", "loops"}
    topics_b = {"sets", "dictionaries", "loops", "functions"}
    only_a, only_b, shared = compare_topics(topics_a, topics_b)
    print("Only A:", only_a)
    print("Only B:", only_b)
    print("Shared:", shared)


if __name__ == "__main__":
    main()
