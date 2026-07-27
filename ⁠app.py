import random
import streamlit as st

st.title("我が家の献立＆解凍マネージャー")

# 担当ローテーションの設定（4日周期）
cycles = [
    "0: 奥さん担当",
    "1: 俺担当 ① (肉・炒め物系)",
    "2: 俺担当 ② (丼・お手軽系)",
    "3: 俺担当 ③ (魚の日・要解凍)",
]

# ユーザーが今日の担当を選択
selected_index = st.selectbox(
    "今日の担当サイクルを選択（テスト用）",
    range(len(cycles)),
    format_func=lambda x: cycles[x],
)

# 明日の担当を自動計算
tomorrow_index = (selected_index + 1) % len(cycles)

st.markdown("---")

# 解凍・準備チェッカー
st.subheader("🔔 明日の準備・解凍チェッカー")
if tomorrow_index == 3:
    st.warning(
        f"明日は **{cycles[tomorrow_index]}** です！\n\n👉 **骨とりタラ**を今夜のうちに冷蔵庫へ移して解凍してください！"
    )
elif tomorrow_index == 0:
    st.info(f"明日は **{cycles[tomorrow_index]}** です。準備は特に必要ありません。")
else:
    st.success(
        f"明日は **{cycles[tomorrow_index]}** です。冷凍ストック（豚こま・鶏むねなど）の残量を確認しておきましょう。"
    )

st.markdown("---")

# 💡 献立アイデア提案機能
st.subheader("🍳 本日の献立アイデア提案")

# 当番や食材に応じたメニューの引き出し
meat_menus = [
    "豚こまとピーマンのオイスター炒め",
    "鶏むね肉のしっとりレンジ蒸し（ポン酢がけ）",
    "豚バラともやしのレンジ蒸し",
    "鶏肉と野菜の旨辛炒め",
]

fish_menus = ["骨とりタラのホイル焼き（バター醤油）", "タラの和風あんかけ", "タラのソテー（トマトソース）"]

other_menus = [
    "冷蔵庫の残り物で作る炒飯",
    "手軽な完全栄養食（BASE FOOD）でサクッと済ませる",
    "おつまみ風プレート（チーズ、乾物、簡単な小鉢いろいろ）",
]

if st.button("💡 おすすめの献立をランダムで決める！"):
  if selected_index == 3:
    # 魚の日の場合
    chosen_menu = random.choice(fish_menus)
    st.success(今日は魚の日です！おすすめメニュー： **" + chosen_menu + "**")
  elif selected_index in [1, 2]:
    # 俺の担当の場合
    chosen_menu = random.choice(meat_menus)
    st.info(今日の担当にぴったりのメニュー： **" + chosen_menu + "**)
  else:
    # 奥さん担当などの場合
    chosen_menu = random.choice(other_menus)
    st.info(おすすめのアイデア： **" + chosen_menu + "**)

st.markdown("---")

# 現在のストック & ルール確認
st.subheader("📦 現在のストック & 我が家のルール")
st.markdown("""
- **冷凍ストック**: 豚こま、鶏むね肉、骨とりタラ
- **基本ルール**: 
  - 4日周期の当番制（最後は魚の日）
  - 魚の日は前日夜から冷蔵庫で解凍を忘れない
""")
