#!/usr/bin/env python3
"""
Script to convert Bengali test file into a properly formatted dictionary for codetypo.
"""
import re
from pathlib import Path

def extract_bengali_words(file_path):
    """Extract Bengali words from a text file."""
    # Bengali Unicode range: U+0980 to U+09FF
    bengali_pattern = re.compile(r'[\u0980-\u09FF]+')
    words = set()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Skip comment lines
            if line.strip().startswith('#'):
                continue
                
            # Remove comments and split into words
            clean_line = re.sub(r'#.*$', '', line).strip()
            if not clean_line:
                continue
                
            # Extract Bengali words
            for word in bengali_pattern.findall(clean_line):
                words.add(word)
    
    return sorted(words)

def create_dictionary(words, output_path):
    """Create a dictionary file with word->word format."""
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in words:
            if word.strip():
                f.write(f"{word}->{word}\n")

def main():
    # Paths
    test_file = Path(__file__).parent.parent / 'codetypo' / 'tests' / 'data' / 'bn_test.txt'
    output_dict = Path(__file__).parent.parent / 'codetypo' / 'data' / 'dictionary_bn.txt'
    
    # Extract words and create dictionary
    words = extract_bengali_words(test_file)
    create_dictionary(words, output_dict)
    
    print(f"Created dictionary with {len(words)} Bengali words at: {output_dict}")

if __name__ == '__main__':
    main()
