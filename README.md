
# Oracle Cloud Infrastructure AI Vision を使った画像分類

## これは何？

"Lemons quality control dataset" を使って、Oracle Cloud Infrastructure AI Service の画像分類を試します。  
レモンの画像を機械学習を用いて "good", "bad", "empty" の3種類に分類します。  

| | | |
| ------------- | ------------- | ------------- |
| good | bad | empty |
| ![](https://github.com/robotduinom/lemon_dataset/blob/main/docs/examples/good_quality/good_quality_585.jpg?raw=true) | ![](https://github.com/robotduinom/lemon_dataset/blob/main/docs/examples/bad_quality/bad_quality_8.jpg?raw=true) | ![](https://github.com/robotduinom/lemon_dataset/blob/main/docs/examples/empty_background/empty_background_385.jpg?raw=true) |


Github: https://github.com/robotduinom/lemon_dataset

Kaggle: https://www.kaggle.com/datasets/yusufemir/lemon-quality-dataset 

## 手順

以下 ４つの Jupyter Notebook ファイルがありますので、順番に実行していくことで、画像分類の一連のワークフローを追うことができます。

+ 1_prepare_images.ipynb (画像ファイルをオブジェクト・ストレージにアップロードする)
+ 2_labeling.ipynb (データセットを作ってラベリングする ~ デフォルト設定で数十分)
+ 3_create_model.ipynb (データセットを使って分類モデルを作成する ~ デフォルト設定で数時間)
+ 4_analyze.ipynb (分類モデルを試す)

## Notebook を実行する前に

1. params.py に適切な設定値を入れて下さい。  
   全ての画像データ (2528個) を扱うとラベリングからモデル作成まで相当な時間がかかります。
   `sampling_factor` を 0 から 1 の範囲の少数で指定して、扱うデータの数を絞ることができます。
    (小さくし過ぎると学習に失敗しますので、0.1 以上を推奨します)

1. 関連するサービスの実行権限があることを確認して下さい。  
   + [オブジェクト・ストレージ](https://docs.oracle.com/ja-jp/iaas/Content/Object/home.htm)
   + [データ・ラベリング](https://docs.oracle.com/ja-jp/iaas/data-labeling/data-labeling/using/home.htm)
   + [VIsion](https://docs.oracle.com/ja-jp/iaas/vision/vision/using/home.htm)

1. git と docker or podman が必要です。  
   GitHub からデータセットを取ってくるのに git が必要です。  
   rar ファイルを解凍するための unrar 用 docker イメージを作って実行します。  
   podman を使っている場合は、Notebook の当該箇所を書き換えるか、エイリアス `alias docker=podman` を作成して下さい。


