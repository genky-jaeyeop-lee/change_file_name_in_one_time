import os

# ユーザーが変更するフォルダのパスを入力
directory = input("ファイル名を変更するフォルダのパスを入力してください: ").strip()

# フォルダが存在するか確認
if not os.path.exists(directory):
    print(" 指定されたフォルダが存在しません。プログラムを終了します。")
    exit()

# 変更するファイル名のマッピング設定
rename_map = {
    "在コン会議-1": "Genky食品部会議",
    "在コン部会議-1": "Genky食品部会議",
    "在コン会議-2": "在コン部会議",
    "在コン部会議-2": "在コン部会議"
}

# 変更されたファイルの数を記録する変数
count = 0

# サブフォルダも含めて検索
for root, _, files in os.walk(directory):
    for filename in files:
        old_path = os.path.join(root, filename)

        # 変更するファイル名を検索
        for key, value in rename_map.items():
            if key.lower() in filename.lower():  # 大文字・小文字を区別せず比較
                new_filename = filename.replace(key, value)
                new_path = os.path.join(root, new_filename)

                # ファイル名を変更
                os.rename(old_path, new_path)
                print(f" 変更完了: {filename} → {new_filename}")
                count += 1
                break  # 1回変更したら追加の変更を防ぐ

# 最終的に変更されたファイルの数を出力
print(f"\n 合計 {count} 個のファイルが変更されました。")


