#python 3.4.2で動作確認

import numpy as np
import matplotlib

# matplotlib.pylotインポート前に
# 記述するとsavefigがつかえる
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ターミナルコマンド実行
import subprocess

# ファイル名取得
import os.path

# 日付を扱う
from datetime import datetime, timedelta

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

save_dir = "tmpFile/" + name + ".png"

plt.savefig(save_dir)

# 現在の時間を取得(日本時間に変換)
str_date = (datetime.now() + timedelta(hours=9)).strftime('%Y%m%d%H%M%S')

try:
    command = "bash"
    shellscript = "/usr/local/bin/dropbox_uploader.sh"
    method = "upload"
    file_dir = "/home/pi/Work/python/" + save_dir
    upload_name = name + "_" + str_date + ".png"

    # Dropboxアップロードのシェルスクリプトを実行する
    res = subprocess.check_call([command, shellscript, method, file_dir, upload_name])
    print("dropboxにアップロードしました。")
except:
    print("Error.")
    traceback.print_exc()