
# Oracle Cloud Infrastructure AI Vision を使った画像分類

## これは何？

"Lemons quality control dataset" を使って、Oracle Cloud Infrastructure AI Service の画像分類を試します。  
レモンの画像を機械学習を用いて "good", "bad", "empty" の3種類に分類します。  

| good | bad | empty |
| ------------- | ------------- | ------------- |
| ![](https://storage.googleapis.com/kagglesdsdata/datasets/2502063/4245788/lemon_dataset/good_quality/good_quality_1007.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230816%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230816T073711Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=0ebacc0a8b356ef19acc0c5459e8f1408b225a496bd562c424f0d89e1490ce2ba6def6687887df36105bc30ff5a16b3d8915820c12cbe6f0fe67132d4ec38e544c939555b76ad3211fd7d976fc2e33eba0577b5f25e0d4d5d86e3640b65b0282a0d58a91e805437abc2249b7bc1f3cf01c6d64039cb33c9b335170cf49cd63f9e151f220fb89009350d766767bca4926b28070c366ef70d616a632276a9271aeab3e57c87c4f90b94ddc1efb947a4e2658d6be38c35fddd477199da2997a8077624c2aa9331e85d1e096ff14ee007304382900be03bd251efada5cf423db8bd659990d74f5549253836dc616e4bb6a07a54dadd3f23bb9db430231e5bd9c1413) | ![](https://storage.googleapis.com/kagglesdsdata/datasets/2502063/4245788/lemon_dataset/bad_quality/bad_quality_107.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230816%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230816T073729Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=146c8aad5f7c287381fe7c2307a279f4b6619c222834e963a390830ac6ce90739989fa6b28fbe34068c0aee6bb92ef826ba3c21f12696609b48e387043ae04cc9e64278d759c09c1d519ab44200bc2a814819f9a573f4823e25769f42683b91c1b911022bac674d5dc0afa8b99ccfad2c73f089f5641488be6ca12acbff9cef59b5d6871d445a8aa70612f40f38affdbc550dc1dc1b2d47066926ec7e9ce4f344c523baf43d2a92fb6ef88a78e4abd7331a51815d1cebd3ba80c3ef39f3691febb08ab7dbe2cc42c53ff941510e9350efeb3cec54ea40c2428e445b9e9a958e6ad60791f6d1e72c7f6acfacdb39b7744c22e9b9a795c702b0eae87b02e431776) | ![](https://storage.googleapis.com/kagglesdsdata/datasets/2502063/4245788/lemon_dataset/empty_background/empty_background_108.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=databundle-worker-v2%40kaggle-161607.iam.gserviceaccount.com%2F20230816%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230816T073745Z&X-Goog-Expires=345600&X-Goog-SignedHeaders=host&X-Goog-Signature=81f1912dd17e532f890b56d59408c9c8657cd761bb73bab2a1762a4ca62082da459983b1a17d749b528daae76967b4b19bf3d1f338eb05e9d378121908f438bc40f4db5931fb94b4ea01737b8d48ca304414b9a9d38f7d7ccd069f86ecf33a0b62c7f6c98307b2e345a97236cf029e3b8465f625c2c1df7f50deac2f70792a0bc74da0e0fb036afd528d0d4c1214a2c4977eb8f0a868c7c975e5674100d37a103f41fde37461b1e2bb005f559a5cba7e92baaa4ce07c0d5bd27d3dda008eb40240ff7982d996d79d486263e5eb97bf3ab0342a2886e9dda1c61cd02bd23e370921cec044129a788fc1a68a811b702db0b85c261559493aea52510e463d0e97d4) |


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

