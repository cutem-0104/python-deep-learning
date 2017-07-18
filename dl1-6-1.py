# python 3.4.2で動作確認
# Dropboxへのアップロードを行うため、別途下記リンクを参考に設定が必要
# https://auxin01.wordpress.com/2016/08/22/raspberry-pi_raspbian_dropbox-uploader2016/

# 機械学習に必要なライブラリのインポート
import numpy as np
import matplotlib

# matplotlib.pylotインポート前に
# 記述するとsavefig(グラフを画像ファイルに出力)がつかえる
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ターミナルコマンド実行できるライブラリ
import subprocess

# オペレーティングインターフェース（ファイル名取得)
import os.path

# 日付を扱う
from datetime import datetime, timedelta

# スタックトレースの表示
import traceback

# データの作成
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# グラフの描画
plt.plot(x, y)
plt.show()

# ファイル名の取得
file_name = os.path.basename(__file__)
# ファイル名と拡張子を分ける
name, ext = os.path.splitext(file_name)

# グラフをpngファイルで出力
save_dir = "tmpFile/" + name + ".png"
plt.savefig(save_dir)

# 現在の時間を取得(日本時間に変換)
str_date = (datetime.now() + timedelta(hours=9)).strftime('%Y%m%d%H%M%S')

try:
    # ホームディレクトリの取得
    homedir = os.getenv("HOME")

    # pngファイルのパス取得
    file_dir =  homedir + "/Work/python/" + save_dir

    # Dropboxアップロードのシェルスクリプトを実行する
    command = "bash"
    shellscript = "/usr/local/bin/dropbox_uploader.sh"
    method = "upload"
    upload_name = name + "_" + str_date + ".png"
    res = subprocess.check_call([command, shellscript, method, file_dir, upload_name])
    print("dropboxにアップロードしました。")
except:
    print("Error.")
    traceback.print_exc()