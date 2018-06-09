# real-coded-genetic-algorithm

==================

## Demo

matplotlibをインストールしていること
sample_xxx.pyのコメントアウトを解除して実行すること


* 交叉の作成分布の画像化
    * plot_blx_alpha : BLX_alphaの子個体分布サンプル
    * plot_simplex : の子個体分布サンプル

python sample_plot.py

* 実際の最適化の挙動のサンプルコードと画像化
    * demo_1
        * Sphere関数に対してSimplex+JGGの組み合わせで実行
    * demo_2
        * Rosenbrock関数に対してSimplex+JGGの組み合わせで実行
    * demo_3
        * Rosenbrock関数に対してSimplex+JGG,BLX_alpha+JGGの組み合わせで実行

python sample_main.py



## Required

* Python3
* numpy
* maplotlib (if execute sample code)

## Constitution

* crossover.py
    * 交叉方法の定義
* evaluator.py
    * 評価関数の定義
* generation_selector.py
    * 次世代に残す個体の定義
* generator.py
    * 初期個体の遺伝子生成の定義
* individual.py
    * 個体の定義
* sample_main.py
    * Demoのエントリポイント
* sample_plot.py
    * 交叉のイメージプロットサンプル
    * コメントアウトを削除して実行
* parent_selector.py
    * 個体の選択を定義
* society.py
    * 個体を管理し、世代交代などを行う
