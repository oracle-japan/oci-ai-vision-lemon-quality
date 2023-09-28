
# Oracle Cloud Infrastructure AI Vision を使った画像分類

## これは何？

"Lemons quality control dataset" を使って、Oracle Cloud Infrastructure AI Service の画像分類を試します。  
レモンの画像を機械学習を用いて "good", "bad", "empty" の3種類に分類します。  

| good | bad | empty |
| ------------- | ------------- | ------------- |
| ![](https://storage.googleapis.com/kagglesdsdata/datasets/2502063/4245788/lemon_dataset/good_quality/good_quality_1000.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230928%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230928T075424Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=a3cce87aeea39c8e57225700877ea738aba1f639a3978380248e2c1d718df0e17f8062417567ff319af1b8a27eb443da9e609e358c6048669851c7eaf6f40856a96dae3733e3d9ff90d2a9e2842f8deda67db18bb89f01e23b9bad9417d7f159072f54cdfb0b419090bd2a4dca9c2c2b2290564558312d6f3bca893cc39bd8ce43d0de3adf0d9415b247f057caa2fc55548800190e8a6bb9ec59f211e0b220c6730f657b51f57a631343f669c34bba8393a7200033e25331c268952f306f3ab33d0714d37e242eb64f6d7cb005ed84a8c11d18acaa8894dc03308e0814b50a46b33dac3d91aa2c20b1f295f0abad48f9743f47f6dd65b698e188f40fe956803b) | ![](https://storage.googleapis.com/kagglesdsdata/datasets/2502063/4245788/lemon_dataset/bad_quality/bad_quality_106.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230928%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230928T075533Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=8eba2c895335788b45e1541bd8a14e6b15e52748fd61d7294f8c2c241de28e8f9807efcf1ced865876cf193246118f0af8e3ddc4ab9741312742fdb0b68eb30ef09319e52c01424d2cec1b2f32c51b06456c064f93801a08d11f4f85bb7cfbccadeb1f78eb975f3065b5fdb63dc2980a7f896e7447ccaac7a2d414fb32d11a24a07003f8947b312b82821a12fef0dc487e24be2be1b87fbfa440fee14648ad0f56534ca8f645533219f9c9e946412251d11042d5c01387bb8132094a75217cc723ec0c338f33a5802da93c034e15001c79001f3763bb4c154941cb65f4ede27b81e68c5fa1925fdb3b952d474f9a8b829e6400b38dafcc1eb2c9c68223f3f19c) | ![](https://storage.googleapis.com/kagglesdsdata/datasets/2502063/4245788/lemon_dataset/empty_background/empty_background_0.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230926%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230926T000454Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=6b3fb0dd45cba87789c0fa20635992ad1455ec91b6ee26a3baa43eafe5efdbadfdc9240681f3dae1bdd332d62c02b0527779d654ac91827e2cb41374e6d2e86cabdc9a4180c85b3897210207516dc6c128878eaddaeb37e1b07178ab299e95b032fd5e7344f34e9224c45ae5dd9a5fdfd9a1d4adc0be345af89ffefd2e1489dac16f222d4db74ad940f89b51668b1296818d7f8155ff2531b7bdbee469781797167e204670bd9647196d9f28144d861684612e2b02cad40bc974ba861ece3bd3c511ff3be74a69ab5c9f793903c628653b3a6b96695faf728cce838fbee60223fb64695b2d998297e3504de98657c42ddb22ea82fcf5a76280327860609f616f) |


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

1. 関連するOCIのサービス＆ツールの準備と実行権限があることを確認して下さい。  
   + [SDK for Python](https://docs.oracle.com/ja-jp/iaas/Content/API/SDKDocs/pythonsdk.htm)
   + [オブジェクト・ストレージ](https://docs.oracle.com/ja-jp/iaas/Content/Object/home.htm)
   + [データ・ラベリング](https://docs.oracle.com/ja-jp/iaas/data-labeling/data-labeling/using/home.htm)
   + [VIsion](https://docs.oracle.com/ja-jp/iaas/vision/vision/using/home.htm)

1. 諸々のツール、モジュールのインストールが必要です。  
   + GitHub からデータセットを取ってくるのに git が必要です。  
   + rar ファイルを解凍するための unrar 用 docker イメージを作って実行します。  
     podman を使っている場合は、Notebook の当該箇所を書き換えるか、エイリアス `alias docker=podman` を作成して下さい。
   + python の必要なモジュールは pip を使ってインストールして下さい。   

