# Pokemon_opt

このスクリプトは N vs N のポケモンバトルを最適化するために開発されたものです。(12/30/2020現在)

# Requirements

このスクリプトはPython3が必要です。  
またこのスクリプトを動作させるには、以下のライブラリが必要です。

* NumPy
* OpenJij
* PyQUBO

# 実行方法

このリポジトリをクローンします。そのディレクトリに移動後、以下のコマンドで実行することができます。

```
$ python pokemon.py
```

# 使い方

`make_instance.py`の`enemy`と`skill`変数を設定することで、相手ポケモンのタイプとわざを変更することが可能です。
これらの変数はリストになっています。リストの並びは左から順に以下の通りです。

> [ノーマル、ほのお、みず、でんき、くさ、こおり、かくとう、どく、じめん、ひこう、エスパー、むし、いわ、ゴースト、ドラゴン、あく、はがね、フェアリー]

指定したいタイプの数字を1に、それ以外の数字を0にすることで、問題に指定したタイプを反映させることができます。
