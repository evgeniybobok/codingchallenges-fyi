#!/usr/bin/env python3

def count_lines_words_symbols_bytes(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    num_chars = sum(len(line) for line in lines)

    with open(filepath, 'rb') as f:
        file_bytes = f.read()
        num_bytes = len(file_bytes)

    return num_lines, num_words, num_chars, num_bytes

def main():
    print(count_lines_words_symbols_bytes('text.txt'))

if __name__ == '__main__':
    main()