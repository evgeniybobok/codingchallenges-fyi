#!/usr/bin/env python3
import argparse
import sys

def count_lines_words_chars(data):
    num_lines = len(data)
    num_words = sum(len(line.split()) for line in data)
    num_chars = sum(len(line) for line in data)

    return num_lines, num_words, num_chars

def main():
    parser = argparse.ArgumentParser(description="My version of the wc command")
    parser.add_argument('file_path', nargs='?', type=str, help="Path to the file")
    parser.add_argument('-l', '--lines', action='store_true', help="Count the number of lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count the number of words")
    parser.add_argument('-c', '--chars', action='store_true', help="Count the number of characters")
    parser.add_argument('-b', '--bytes', action='store_true', help="Count the number of bytes")
    args = parser.parse_args()
    # print(args.file_path, args.lines, args.words, args.chars, args.bytes)

    if args.file_path:
        print(f"Counting for file {args.file_path}:")
        # read once for lines, words and chars and once more for bytes
        with open(args.file_path, 'r') as f:
            data = f.readlines()
        with open(args.file_path, 'rb') as f:
            data_bytes = f.read()
    else:
        print("Counting for stdin:")
        # reading as bytes first and then decoding to text
        data_bytes = sys.stdin.buffer.read()
        data = data_bytes.decode('utf-8').splitlines()
    
    num_lines, num_words, num_chars = count_lines_words_chars(data)
    num_bytes = len(data_bytes)


    if args.lines:
        print(f"Lines: {num_lines}")
    if args.words:
        print(f"Words: {num_words}")
    if args.chars:
        print(f"Characters: {num_chars}")
    if args.bytes:
        print(f"Bytes: {num_bytes}")
    
    if not (args.lines or args.words or args.chars or args.bytes):
        print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}, Bytes: {num_bytes}")


if __name__ == '__main__':
    main()