import streamlit as st
import pandas as pd
import random
import matplotlib.pyplot as plt  
import os

# ポート番号の選択肢
port_options = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10']

# プルダウンメニューを表示
selected_port = st.selectbox("ポート番号を選択してください:", port_options)

# 選択されたポート番号を表示
st.write("選択されたポート番号:", selected_port)

st.title("グラフ表示のテスト")
st.write("ここにコンテンツを追加します。")

# Excelファイルを開く
excel_file_path = "C:\\Users\\yhbda\\マイドライブ\\M1＆M2\\研究関連\\VSCode\\サンプルデータ.xlsx"
df = pd.read_excel(excel_file_path)

# 1列目のデータをリストに変換
column1_data = df.iloc[:, 0].tolist()

# 1列目のデータがリストに格納されます
print(column1_data)
# 2列目のデータをリストに変換
column2_data = df.iloc[:, 1].tolist()

# 2列目のデータがリストに格納されます
print(column2_data)

# データをDataFrameに変換
data = pd.DataFrame({'x': column1_data, 'y': column2_data})

# グラフを表示
fig, ax = plt.subplots()
ax.plot(data['x'], data['y'], label='データ')  # データをプロットし、ラベルを設定

# ラベルを追加
ax.set_xlabel('wavelength (nm)')
ax.set_ylabel('absorbance (-)')

# サイドバーウィジェット
st.sidebar.title("サイドバー")
st.sidebar.button("サイドバーボタン")

# カラムレイアウトを作成
col1, col2 = st.columns(2)

# カラム1にウィジェットを配置
with col1:
    st.button("左側のボタン")

# カラム2にウィジェットを配置
with col2:
    st.button("右側のボタン")

# ランダムな16進数を生成
def generate_random_hex_list(length):
    random_hex_list = []
    for _ in range(length):
        random_hex = hex(random.randint(0, 0xFFFF))[2:]
        random_hex_list.append(random_hex)
    return random_hex_list

def hex_list_to_decimal(hex_list):
    decimal_list = []
    for hex_value in hex_list:
        decimal_value = int(hex_value, 16)  # 16進数から10進数に変換
        decimal_list.append(decimal_value)
    return decimal_list

# ランダムな16進数のリストを生成
random_hex_list = generate_random_hex_list(10)
print("ランダムな16進数リスト:", random_hex_list)

# 16進数のリストを10進数に変換
decimal_list = hex_list_to_decimal(random_hex_list)
print("10進数リスト:", decimal_list)

if st.button("ランダムなグラフを表示"):
    # グラフの表示
    st.line_chart(decimal_list)


if st.button("過去の結果"):
    # グラフの表示
    st.pyplot(fig)

# ダウンロードファイル名の入力ウィジェットを表示
download_filename = st.text_input("ダウンロードファイル名を入力してください (拡張子を含まない):")
download_filename = f"{download_filename}.xlsx"

if st.button("データをエクセルファイルにエクスポート"):
    if data is not None:
        if download_filename:
            # ファイルを指定したファイル名でエクセルファイルに書き込む
            data.to_excel(download_filename, index=False)
            
            # ファイルをダウンロードディレクトリに移動
            download_dir = os.path.expanduser("~/Downloads")  # ダウンロードディレクトリのパス
            new_location = os.path.join(download_dir, download_filename)
            os.rename(download_filename, new_location)

            st.success(f"データが '{download_filename}' としてエクセルファイルにエクスポートされ、ダウンロードディレクトリに保存されました。")
        else:
            st.warning("ダウンロードファイル名を入力してください。")
    else:
        st.warning("データが読み込まれていません。")
