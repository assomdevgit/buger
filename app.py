import streamlit as st # streamlit
from widget.menu_list import get_menu_list
# st. -> ctrl + space

st.image("https://upload.wikimedia.org/wikipedia/commons/8/85/Burger_King_logo_%281999%29.svg", width=200)
st.title("버거킹 메뉴")

menus = ["프리미엄", "와퍼&주니어", "음료"]

# 버거킹 메뉴 리스트
get_menu_list(menus)