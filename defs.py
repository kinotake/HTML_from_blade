import re

def count_lines(file_path, match,count):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

        count = count+1

        indexes = [i for i, line in enumerate(lines) if match in line]

        if len(indexes) > 1:

            correct_line = indexes[count-1]

            # リストは０から始まるため、リストの行数＋1がファイル上での行数になります。
            appear_line = correct_line + 1
        else:

            correct_line = indexes[0]
            # リストは０から始まるため、リストの行数＋1がファイル上での行数になります。
            appear_line = correct_line + 1

        return appear_line,count
