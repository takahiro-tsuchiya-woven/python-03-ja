# ここにコードを書いてください
import pandas as pd
from sklearn import datasets

# 1. データの読み込みと概要表示
# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加し、0～2の番号を記入する (各番号が異なる品種を表す)
iris_df['species'] = iris.target

# 最初の5行を表示
print("最初の5行:")
print(iris_df.head())

# 2. データのクリーニングと検証
# 欠損値の確認
print("\n欠損値の確認:")
print(iris_df.isnull().sum())

# 各列のデータ型を確認
print("\n各列のデータ型:")
print(iris_df.dtypes)

# 3. 基本的な分析と基本統計量の計算
# 基本統計量を計算
statistics = iris_df.describe().T

# 基本統計量のDataFrameを新規作成（必要な列のみ選択）
statistics_df = statistics[['mean', '50%', 'std']].copy()
statistics_df.columns = ['mean', 'median', 'std']

# 結果を表示
print("\n基本統計量:")
print(statistics_df)

# CSV形式で保存
statistics_df.to_csv('iris_statistics.csv', index=True)

# 4. 特徴量エンジニアリング
# 新しい特徴量を追加
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 新しい特徴量の基本統計量を計算
new_statistics = iris_df[['sepal_area', 'petal_area']].describe().T

# 新しい特徴量の基本統計量を追加
new_statistics_df = new_statistics[['mean', '50%', 'std']].copy()
new_statistics_df.columns = ['mean', 'median', 'std']

# 統計情報のDataFrameに追加
statistics_df = pd.concat([statistics_df, new_statistics_df])

# 結果を表示
print("\n新しい特徴量の基本統計量を含む:")
print(statistics_df)

# CSV形式で保存
statistics_df.to_csv('iris_statistics_with_new_features.csv', index=True)

# 5. データのフィルタリング
# フィルタリング関数を定義
def filter_data(df, column, threshold):
    return df[df[column] >= threshold]

# 例: 'sepal length (cm)'が5以上の行のみを含むようにフィルタリング
filtered_df = filter_data(iris_df, 'sepal length (cm)', 5)

# 結果を表示
print("\nフィルタリング後のデータ:")
print(filtered_df.head())

# 6. データのエクスポート
# DataFrameをCSV形式で保存
iris_df.to_csv('iris_dataset_with_new_features.csv', index=False)
