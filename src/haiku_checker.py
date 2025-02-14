import re

def is_haiku(text):
    """Check if a given text follows the 5-7-5 haiku pattern."""
    lines = text.strip().split("-") 
    if len(lines) != 3:
        return False  

    syllable_counts = [count_syllables_in_line(line) for line in lines]
    for count in syllable_counts:
        print(count)
    return syllable_counts == [5, 7, 5]

def count_syllables_in_line(line):
    """Count total syllables in a line.""" 
    words = line.strip().split(" ")  # Extract words
    return sum(count_syllables(word) for word in words)

def count_syllables(word):
    """Count vowel groups in a word. Remove silent e unless word ends with le"""
    word = word.lower()
    if word.endswith("e") and not word.endswith("le"):
        word = word[:-1]  
        
    # Count vowel groups
    syllables = re.findall(r'[aeiouy]+', word)
    return max(1, len(syllables))  

