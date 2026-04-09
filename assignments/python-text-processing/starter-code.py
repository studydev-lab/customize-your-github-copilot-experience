from collections import Counter
import string


def clean_text(text: str) -> str:
    # TODO: Normalize case, remove punctuation, and normalize whitespace.
    return text


def analyze_text(text: str) -> tuple[int, int, list[tuple[str, int]]]:
    words = text.split()
    total_words = len(words)
    unique_words = len(set(words))
    top_words = Counter(words).most_common(5)
    return total_words, unique_words, top_words


def main() -> None:
    input_file = "sample.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            raw_text = f.read()
    except FileNotFoundError:
        print("Could not find sample.txt. Please add the input file and run again.")
        return

    cleaned = clean_text(raw_text)
    total, unique, top5 = analyze_text(cleaned)

    with open("cleaned_output.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(f"Total words: {total}\n")
        f.write(f"Unique words: {unique}\n")
        f.write("Top 5 words:\n")
        for word, count in top5:
            f.write(f"- {word}: {count}\n")

    print("Analysis complete. Check cleaned_output.txt and report.txt.")


if __name__ == "__main__":
    main()
