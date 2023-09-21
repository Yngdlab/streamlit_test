import streamlit as st
import pandas as pd
import random

# ポート番号の選択肢
port_options = ['COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'COM10']

# プルダウンメニューを表示
selected_port = st.selectbox("ポート番号を選択してください:", port_options)

# 選択されたポート番号を表示
st.write("選択されたポート番号:", selected_port)

st.title("グラフ表示のテスト")
st.write("ここにコンテンツを追加します。")

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

