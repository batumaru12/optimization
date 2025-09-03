# 最適化による収率推定
最適化により実験データから，より収率が高くなる実験環境を推定する．

## アップデート

- \[2025.09.02\] ログが[sample_log.csv](https://github.com/batumaru12/optimization/blob/main/optimization/data/sample_log.csv "log faile")のように保存されるようになりました。

## 環境準備

<details>
<summary>準備方法（venv）</summary>

仮想環境作成

```shell
python -m venv [仮想環境名]
```

作った環境へ移動
```shell
.\[仮想環境名]\Scripts\activate
```


必用パッケージのインストール

```shell
pip install -r requirements.txt
```

確認
```shell
pip list
```

以下のように表示されれば準備完了


```shell
Package         Version
--------------- -----------
joblib          1.5.1
numpy           2.3.2
packaging       25.0
pandas          2.3.2
pip             25.0.1
pyaml           25.7.0
python-dateutil 2.9.0.post0
pytz            2025.2
PyYAML          6.0.2
scikit-learn    1.7.1
scikit-optimize 0.10.2
scipy           1.16.1
six             1.17.0
threadpoolctl   3.6.0
tzdata          2025.2
```

</details>

<details>
<summary>準備方法（Anaconda）</summary>
仮想環境作成（Anaconda使用時）

```shell
conda create -n [仮想環境名] python=3.12
```

作った環境へ移動

```shell
conda activate [仮想環境名]
```

必用パッケージのインストール

```shell
pip install -r requirements.txt
```

確認
```shell
conda list
```

以下のように表示されれば準備完了

```shell
# Name                    Version                   Build  Channel
joblib                    1.5.1                    pypi_0    pypi
numpy                     2.3.2                    pypi_0    pypi
packaging                 25.0                     pypi_0    pypi
pandas                    2.3.2                    pypi_0    pypi
pip                       25.0.1                   pypi_0    pypi
pyaml                     25.7.0                   pypi_0    pypi
python-dateutil           2.9.0.post0              pypi_0    pypi
pytz                      2025.2                   pypi_0    pypi
PyYAML                    6.0.2                    pypi_0    pypi
scikit-learn              1.7.1                    pypi_0    pypi
scikit-optimize           0.10.2                   pypi_0    pypi
scipy                     1.16.1                   pypi_0    pypi
six                       1.17.0                   pypi_0    pypi
threadpoolctl             3.6.0                    pypi_0    pypi
tzdata                    2025.2                   pypi_0    pypi
```

</details>

## データ準備

最適化を行う上で用意するデータは2つ．

### 実験データ

実際に実験した結果を.csvファイルで保存する．`[任意名]_optimization.csv`が最適化を行う対象ファイルとなる．

1行目に値の名前を入れること．また，最適化対象である収率（yield）は必ず含めること．

<details>
<summary>例</summary>

|current|Init_molarity|electrolyte|temp|time|yield|
|:----|:----|:----|:----|:----|:----|
|1|10|0.05|60|180|46|
|2|20|0.2|25|60|22|
|3|10|0.1|40|120|62|
|4|15|0.1|40|60|53|
|5|5|0.05|25|120|14|

</details>

### 最大値・最小値設定ファイル

`[任意名]_setup.csv`に最大値や最小値を設定する．

1行目に値の名前を入れること．2行目が最小値，3行目が最大値を入れる．

<details>
<summary>例</summary>

|current|Init_molarity|electrolyte|temp|time|
|:----|:----|:----|:----|:----|
|1|5|0.05|20|60|
|6|30|0.25|80|240|

</details>
