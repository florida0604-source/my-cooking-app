
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
