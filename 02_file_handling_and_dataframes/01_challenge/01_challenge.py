# ここにコードを書いてください
import os
from pathlib import Path
import shutil

# ディレクトリのパスを設定
data_dir = Path("data/text_files")
output_file = data_dir / "merged_books.txt"
library_dir = data_dir / "library"

# 書籍の名前が付いたファイルを1つのテキストファイルに保存
def merge_books(data_dir, output_file):
    books_content = {}

    # ディレクトリ内のファイルをリストアップ
    for filename in os.listdir(data_dir):
        file_path = data_dir / filename
        
        # ディレクトリをスキップ
        if file_path.is_dir():
            continue
        
        # Chapter_x.txt ファイルはスキップ
        if filename.startswith("Chapter_"):
            continue
        
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            books_content[filename] = content

    # 辞書の内容を1つのテキストファイルに保存
    with open(output_file, 'w', encoding='utf-8') as file:
        for title, content in books_content.items():
            file.write(f"=== {title} ===\n")
            file.write(content)
            file.write("\n\n")

# Chapter_x.txt ファイルを library ディレクトリに移動し、ファイルとサイズを一覧表示
def organize_chapters(data_dir, library_dir):
    # library ディレクトリを作成
    if not library_dir.exists():
        print(f"Creating {library_dir}")
        try:
            library_dir.mkdir(parents=True, exist_ok=True)
            if library_dir.exists():
                print(f"{library_dir} created successfully.")
            else:
                print(f"Failed to create {library_dir}.")
                return
        except Exception as e:
            print(f"Exception occurred while creating {library_dir}. Error: {e}")
            return
    
    # library ディレクトリの存在を再確認
    if not library_dir.exists():
        print(f"{library_dir} still does not exist after creation attempt.")
        return

    # Chapter_x.txt ファイルを library ディレクトリに移動
    for chapter_file in data_dir.glob("Chapter_*.txt"):
        print(f"Moving {chapter_file} to {library_dir / chapter_file.name}")
        shutil.move(str(chapter_file), str(library_dir / chapter_file.name))

    # library ディレクトリに移動し、ファイルとサイズを一覧表示
    os.chdir(library_dir)
    print("Files in 'library' directory with their sizes:")
    for file in library_dir.iterdir():
        if file.is_file():
            print(f"{file.name}: {file.stat().st_size} bytes")

if __name__ == "__main__":
    # 書籍ファイルのマージ
    merge_books(data_dir, output_file)
    print(f"Books merged into {output_file}")

    # Chapter ファイルの整理
    organize_chapters(data_dir, library_dir)