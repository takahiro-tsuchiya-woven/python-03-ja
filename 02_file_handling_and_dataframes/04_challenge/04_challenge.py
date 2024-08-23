# ここにコードを書いてください

import pandas as pd
from sklearn.datasets import load_wine

wine_data = load_wine()

wine_df = pd.DataFrame(
    data=wine_data.data,
    columns=wine_data.feature_names,
)
wine_df["target"] = wine_data.target


# 1. カスタムインデックスの設定:
# データから有用なインサイトを得るために、カスタムインデックスを設定します。
wine_df_indexed = wine_df.set_index("target").sort_index()
print(
    "==============================================\n"
    "カスタムインデックスの設定されたデータフレーム\n"
    "==============================================\n"
)
print(wine_df_indexed.head())


# 2. 複雑なフィルタリング:
# 複数列の条件指定や範囲指定クエリのような複雑なフィルタリング操作のための関数を作成します。
def filter_wine(df, alcohol_threshold, malic_acid_threshold):
    return df[
        (df["alcohol"] > alcohol_threshold) & (df["malic_acid"] < malic_acid_threshold)
    ]


filtered_wines = filter_wine(wine_df, 13, 2)
print(
    "==========================\n"
    "フィルタリングされたデータ\n"
    "==========================\n"
)
print(filtered_wines.head())

# 3. データ変換:
# データ変換を適用します (例: 有益な観察情報や基本統計量を保存する新しい列を作成する)。
wine_df["magnesium_to_flavanoids"] = wine_df["magnesium"] / wine_df["flavanoids"]
print(
    "===================================================\n"
    "magnesium_to_flavanoids列が追加されたデータフレーム\n"
    "===================================================\n"
)
print(wine_df[["magnesium", "flavanoids", "magnesium_to_flavanoids"]].head())

# 4. データの要約:
# データをより深く理解するために、データのグループ化、集計、ピボット処理を行います。
summary_stats = wine_df.groupby("target").agg(
    {"alcohol": ["mean", "std"], "malic_acid": ["mean", "std"]}
)
print(
    "===============================================\n"
    "ワインの等級に関する統計データ（平均と標準偏差）\n"
    "===============================================\n"
)
print(summary_stats)
