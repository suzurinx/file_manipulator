import sys
import os

def validate_paths(inputpath, outputpath=None):
    if not os.path.isfile(inputpath):
        raise FileNotFoundError(f"入力ファイル {inputpath} が存在しません。")
    if outputpath and os.path.isdir(outputpath):
        raise IsADirectoryError(f"出力パス {outputpath} はディレクトリであり、ファイルではありません。")

def reverse_file(inputpath, outputpath):
    validate_paths(inputpath, outputpath)
    with open(inputpath, 'r') as infile:
        content = infile.read()
    with open(outputpath, 'w') as outfile:
        outfile.write(content[::-1])

def copy_file(inputpath, outputpath):
    validate_paths(inputpath, outputpath)
    with open(inputpath, 'r') as infile:
        content = infile.read()
    with open(outputpath, 'w') as outfile:
        outfile.write(content)

def duplicate_contents(inputpath, n):
    if not isinstance(n, int) or n < 1:
        raise ValueError("複製回数 (n) は正の整数でなければなりません。")
    validate_paths(inputpath)
    with open(inputpath, 'r') as infile:
        content = infile.read()
    with open(inputpath, 'w') as outfile:
        outfile.write(content * n)

def replace_string(inputpath, needle, newstring):
    if not needle:
        raise ValueError("置換対象の文字列 (needle) は空であってはなりません。")
    validate_paths(inputpath)
    with open(inputpath, 'r') as infile:
        content = infile.read()
    content = content.replace(needle, newstring)
    with open(inputpath, 'w') as outfile:
        outfile.write(content)

def main():
    if len(sys.argv) < 3:
        print("使用法: \npython3 file_manipulator.py <コマンド> <入力パス>")
        print("使用例：")
        print("python3 file_manipulator.py reverse example.txt reversed.txt")
        print("python3 file_manipulator.py copy input.txt output.txt")
        print("python3 file_manipulator.py duplicate-contents data.txt 3")
        print("python3 file_manipulator.py replace-string text.txt old_word new_word")
        sys.exit(1)

    command = sys.argv[1]
    if command == 'reverse':
        if len(sys.argv) != 4:
            print("使用法: python3 file_manipulator.py reverse <入力パス> <出力パス>")
            sys.exit(1)
        reverse_file(sys.argv[2], sys.argv[3])
    elif command == 'copy':
        if len(sys.argv) != 4:
            print("使用法: python3 file_manipulator.py copy <入力パス> <出力パス>")
            sys.exit(1)
        copy_file(sys.argv[2], sys.argv[3])
    elif command == 'duplicate-contents':
        if len(sys.argv) != 4:
            print("使用法: python3 file_manipulator.py duplicate-contents <入力パス> <複製回数>")
            sys.exit(1)
        try:
            n = int(sys.argv[3])
        except ValueError:
            print("複製回数 (n) は正の整数でなければなりません。")
            sys.exit(1)
        duplicate_contents(sys.argv[2], n)
    elif command == 'replace-string':
        if len(sys.argv) != 5:
            print("使用法: python3 file_manipulator.py replace-string <入力パス> <置換対象文字列> <新しい文字列>")
            sys.exit(1)
        replace_string(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print(f"不明なコマンド: {command}")
        print("利用可能なコマンド: reverse, copy, duplicate-contents, replace-string")
        sys.exit(1)

if __name__ == '__main__':
    main()
