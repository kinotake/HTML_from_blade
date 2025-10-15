import shutil
import subprocess
import os
import sys
import tempfile

name = "ChiakiNagashima"
repository_url = "git@github.com:Estra-Coachtech/coachtech-mockcase-1.git"

# 一時ディレクトリを作成し、そこにリポジトリをクローンする
with tempfile.TemporaryDirectory() as temp_dir:
    temp_repo_path = os.path.join(temp_dir, name)
    clone_command = f"git clone {repository_url} {temp_repo_path}"
    print(f"Executing: {clone_command}")
    subprocess.run(clone_command, shell=True, check=True)

    new_dir_name = name + "edit"
    os.makedirs(new_dir_name, exist_ok=True)

    # viewファイルのコピー

    d_dir_path_views = os.path.join(new_dir_name, "views_original")
    os.makedirs(d_dir_path_views, exist_ok=True)

    source_path_views = os.path.join(temp_repo_path, "src", "resources", "views")
    destination_path_views = d_dir_path_views

    # コピー元ディレクトリが存在するか確認
    if os.path.exists(source_path_views):
        for item in os.listdir(source_path_views):
            s = os.path.join(source_path_views, item)
            d = os.path.join(destination_path_views, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print(f"Copied {source_path_views} to {destination_path_views}")
    else:
        print(f"Source directory does not exist: {source_path_views}")

    # cssファイルのコピー

    d_dir_path_css = os.path.join(new_dir_name, "css_original")
    os.makedirs(d_dir_path_css, exist_ok=True)

    source_path_css = os.path.join(temp_repo_path, "src", "public", "css")
    destination_path_css = d_dir_path_css

    # コピー元ディレクトリが存在するか確認
    if os.path.exists(source_path_css):
        for item in os.listdir(source_path_css):
            s = os.path.join(source_path_css, item)
            d = os.path.join(destination_path_css, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print(f"Copied {source_path_css} to {destination_path_css}")
    else:
        print(f"Source directory does not exist: {source_path_css}")

    # rebase_css.py を実行
    rebase_css_script_path = os.path.join(os.path.dirname(__file__), "rebase_css.py")
    if os.path.exists(rebase_css_script_path):
        print(f"Executing {rebase_css_script_path}...")
        subprocess.run([sys.executable, rebase_css_script_path], check=True)
    else:
        print(f"rebase_css.py not found at {rebase_css_script_path}")



