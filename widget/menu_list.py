import streamlit as st

def get_menu_detail(name, size, price):
    return dict(name=name, size=size, price=price)

menu1 = get_menu_detail(
    "기네스와퍼", "R/L", "5000/7000",
)
menu2 = get_menu_detail(
    "몬스터와퍼", "R/L", "3000/5000",
)
menu3 = get_menu_detail(
    "통새우와퍼", "R/L", "5000/7000",
)
menu4 = get_menu_detail(
    "기네스콰트로치즈와퍼", "R/L", "3000/5000",
)

menu_detail = [menu1, menu2, menu3, menu4]

menu1 = get_menu_detail(
    "와퍼", "R/L", "5000/7000",
)
menu2 = get_menu_detail(
    "와퍼주니어", "R/L", "3000/5000",
)
menu3 = get_menu_detail(
    "불고기와퍼", "R/L", "5000/7000",
)
menu4 = get_menu_detail(
    "치즈와퍼", "R/L", "3000/5000",
)
menu_detail2 = [menu1, menu2, menu3, menu4]

menu1 = get_menu_detail(
    "콜라", "0.5/1.0l", "5000/7000",
)
menu2 = get_menu_detail(
    "사이다", "0.5/1.0l", "3000/5000",
)
menu3 = get_menu_detail(
    "아메리카노", "R/L", "5000/7000",
)
menu4 = get_menu_detail(
    "레몬에이드", "R/L", "3000/5000",
)
menu_detail3 = [menu1, menu2, menu3, menu4]

def get_menu_list(menus):
    tab_menus = menus
    tab1, tab2, tab3 = st.tabs(tab_menus)
    with tab1:
        cols = st.columns(3)
        cols[0].write("메뉴")
        cols[1].write("사이즈")
        cols[-1].write("가격")
        for idx, col in enumerate(menu_detail):
            cols = st.columns(3)
            cols[0].write(col['name'])
            cols[1].write(col['size'])
            cols[-1].write(col['price'])


    with tab2:
        cols = st.columns(3)
        cols[0].write("메뉴")
        cols[1].write("사이즈")
        cols[-1].write("가격")
        for idx, col in enumerate(menu_detail2):
            cols = st.columns(3)
            cols[0].write(col['name'])
            cols[1].write(col['size'])
            cols[-1].write(col['price'])

    with tab3:
        cols = st.columns(3)
        cols[0].write("메뉴")
        cols[1].write("사이즈")
        cols[-1].write("가격")
        for idx, col in enumerate(menu_detail3):
            cols = st.columns(3)
            cols[0].write(col['name'])
            cols[1].write(col['size'])
            cols[-1].write(col['price'])