import streamlit as st

# ページ設定
st.set_page_config(
    page_title="我が家の献立＆解凍マネージャー", page_icon="🍳", layout="centered"
)

st.title("🍳 我が家の献立＆解凍マネージャー")

# --- 1. ルールと状態の定義 ---
cycle_names = {0: "奥さん担当", 1: "俺担当 ①", 2: "俺担当 ②", 3: "俺担当 ③ (魚の日)"}

# サンプル在庫データ
if "inventory" not in st.session_state:
    st.session_state.inventory = {
        "骨とりタラ (冷凍)": {"needs_thaw": True, "stock": "500g"},
        "メンチカツ (冷凍)": {"needs_thaw": True, "stock": "あり"},
        "冷凍餃子": {"needs_thaw": False, "stock": "あり"},
        "ロースハム (チルド)": {"needs_thaw": False, "stock": "あり"},
        "ベーコン (チルド)": {"needs_thaw": False, "stock": "あり"},
        "ウインナー": {"needs_thaw": False, "stock": "あり"},
        "豚こま肉": {"needs_thaw": False, "rule": "奥さん専用"},
    }

# --- 2. 本日の担当と翌日の予測 ---
st.header("📅 本日のローテーション")
day_index = st.selectbox(
    "今日の担当サイクルを選択（テスト用）",
    options=[0, 1, 2, 3],
    format_func=lambda x: cycle_names[x],
    index=1,
)

next_index = (day_index + 1) % 4

st.info(f"👉 **今日の担当:** {cycle_names[day_index]}")
st.success(f"📌 **明日の担当:** {cycle_names[next_index]}")

# --- 3. 解凍リマインド機能 ---
st.divider()
st.header("🧊 解凍・準備チェッカー")

if next_index == 3:
    st.warning(
        "⚠️ **【重要・前日リマインド】**\n\n明日は**魚の日（骨とりタラ）**です！\n今夜のうちに、冷凍庫から**「骨とりタラ」を冷蔵庫へ移して解凍**してください。"
    )
elif next_index == 2:
    st.info(
        "💡 明日はメンチカツの予定です。凍ったままトースター調理か、前日解凍か確認してね。"
    )
else:
    st.info("💡 明日は解凍が必要な特別食材はありません。スムーズにいけます！")

# --- 4. 在庫とルールの確認 ---
st.divider()
st.header("🛒 現在のストック & ルール確認")
for item, info in st.session_state.inventory.items():
    rule_text = (
        f" （⚠️ {info['rule']}）" if "rule" in info else ""
    )
    thaw_text = "要解凍" if info.get("needs_thaw") else "そのままでOK"
    st.text(f"・ {item}: {info.get('stock', '')} [{thaw_text}]{rule_text}")
