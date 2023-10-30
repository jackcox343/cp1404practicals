"""
Word occurrences
Estimate: 20 minutes
Actual: 30
"""

text_to_count = {}
text = input("Text: ")
invividual_words = text.split()
for word in invividual_words:
    try:
        text_to_count[word] += 1
    except KeyError:
        text_to_count[word] = 1
sorted_words = sorted(text_to_count.items())
maximum_text_length = max(len(text) for text in text_to_count.keys())
for text, count in sorted_words:
    print(f"{text:{maximum_text_length}} : {text_to_count[text]}", sep="")
