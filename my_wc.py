#!/usr/bin/env python3
import argparse

def count_all(filepath):
    # read the file once, count everything
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
    parser = argparse.ArgumentParser(description="My version of the wc command")
    parser.add_argument('file_path', type=str, help="Path to the file")
    parser.add_argument('-l', '--lines', action='store_true', help="Count the number of lines")
    parser.add_argument('-w', '--words', action='store_true', help="Count the number of words")
    parser.add_argument('-c', '--chars', action='store_true', help="Count the number of characters")
    parser.add_argument('-b', '--bytes', action='store_true', help="Count the number of bytes")
    args = parser.parse_args()
    # print(args.file_path, args.lines, args.words, args.chars, args.bytes)
    num_lines, num_words, num_chars, num_bytes = count_all(args.file_path)

    if args.lines:
        print(f"Lines: {num_lines}")
    if args.words:
        print(f"Words: {num_words}")
    if args.chars:
        print(f"Characters: {num_chars}")
    if args.bytes:
        print(f"Bytes: {num_bytes}")

    if not (args.lines or args.words or args.chars or args.bytes):
        print("No optional argument provided, printing all:")
        print(f"Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}, Bytes: {num_bytes}")


if __name__ == '__main__':
    main()