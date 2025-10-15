# from mkdir import new_dir_name←環境実装時には取得のために必要です
# 最後に拡張子変更してね！
import re
import defs

new_dir_name = "ChiakiNagashimaedit"

file_path = "ChiakiNagashimaedit/views_original/mypage.blade.php"
search_string = "@error"

# ファイルを開いて中身を取得
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

if search_string in content:
    # @error〜@enderror の中身をすべて抽出
    matches = re.findall(r'@error(?:\(.*?\))?\s*(.*?)\s*@enderror', content, re.DOTALL)

    for match in matches:
        replaced = re.sub(r'{{.*?}}', "エラー文が入ります", match)

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = re.sub(re.escape(match), replaced, content, count=1)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)

        # 最初の＠の処理を削除
        rm_first = re.sub(r".*@error.*\n?", "", new_content, count=1)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rm_first)

        rm_end = re.sub(r".*@enderror.*\n?", "", rm_first, count=1)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rm_end)

        content = rm_end

# includeに対する処理
include_string = "@include"

if include_string in content:
    matches = re.findall(r'.*@include.*', content)
    print("=================合致したinclude文===================")
    print(matches)

    for match in matches:
        start = match.find("@include('") + len("@include('")
        end = match.find("'", start)

        include_file_path = match[start:end]

        html_first = '<iframe src="'
        html_end = '"></iframe>'

        html_result = html_first + include_file_path + html_end

        rebase_html = re.sub(r".*@include.*", html_result, content, count=1)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rebase_html)

        content = rebase_html

# if文とforeachは互いに入れ子構造になる場合があるため、処理を2回繰り返します。

if_string = "@if"

if if_string in content:
    matches = re.findall(r'.*@if.*', content)


    print("=================合致したif文===================")
    print(matches)
    for match in matches:

        result = defs.count_lines(file_path, match)