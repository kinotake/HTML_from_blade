# 処理の順序付けを行うためのファイルです。
import re
import defs

new_dir_name = "ChiakiNagashimaedit"

file_path = "ChiakiNagashimaedit/views_original/address.blade.php"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

appear_items = []

section_string = "@section"
# section文に関して、第二引数がある場合は初めと終わりのディレクティブの数を揃えるため、先に書き換えてしまいます。 ex.@section('title','商品詳細ページ')。レイアウトの崩れに関与しないことが多いので、ただの改行。

if section_string in content:
    matches = re.findall(r'.*@section[^,]*,.*', content)

    count = 0

    for match in matches:
        print("@sectionのmatchの中身です")
        print(match)
        appear_lines,count = defs.count_lines(file_path, match ,count)

        lines = open(file_path, encoding="utf-8").readlines()
        lines[appear_lines-1] = "\n"
        open(file_path, "w", encoding="utf-8").writelines(lines)

    # ファイルが書き換わったため、後続の処理でエラーが出ないように再読み込みしています。
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()


# section文
section_string = "@section"

if section_string in content:
    matches = re.findall(r'.*@section.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@section",match))

if section_string in content:
    matches = re.findall(r'.*@endsection.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@endsection",match))

# if文

if_string = "@if"

if if_string in content:
    matches = re.findall(r'.*@if.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@if",match))

if if_string in content:
    matches = re.findall(r'.*@endif.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@endif",match))

foreach_string = "@foreach"

if foreach_string in content:
    matches = re.findall(r'.*@foreach.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@foreach",match))

if foreach_string in content:
    matches = re.findall(r'.*@endforeach.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@endforeach",match))

error_string = "@error"

if error_string in content:
    matches = re.findall(r'.*@error.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@error",match))

if error_string in content:
    matches = re.findall(r'.*@enderror.*', content)

    count = 0

    for match in matches:

        appear_lines,count = defs.count_lines(file_path, match ,count)

        appear_items.append((appear_lines,"@enderror",match))

# ちょっとややこいですが、endの表記が出てきた時点で、一番近い行の条件式を探して、pairsでセットにしています。
all_sorted_lines = sorted(set(num for num, _, _ in appear_items))
start_lines = [appear_line for appear_line, name, original in appear_items if name in ('@section', '@if','@foreach','@error')]

stack = []
pairs = []

for l in all_sorted_lines:
    if l in start_lines:
        stack.append(l)
    else:
        if stack:
            start = stack.pop()
            pairs.append((start, l))
            print(pairs)


# 取り出す
for appear_lines,content,match in appear_items:
    print("=================最終的なデータ値（行数、中身、原文）===================")
    print(appear_lines,content,match)


