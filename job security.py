import streamlit as st
import time
def clear_text():
    st.session_state["url_input"]=""
#קוד להפוך את האלגוריתם לממשק בעברית
st.markdown("""
            <style>
            .stApp {direction: rtl !important;
            text-align: right !important;
            }
            input{direction: rtl !important;
            text-align: right !important;}
            h1{
            text-align: center !important;
            width:100% !important;}
            </style>
            """,
            unsafe_allow_html=True)
st.title("ברוכים הבאים לסורק האבטחה")
url=st.text_input("הזן כתובת לבדיקה", key="url_input").lower()
if st.button("התחל סריקה"):
    if url:
        #משתנה לצורך מחיקת הכיתוב סורק... לאחר הזמן
        status = st.empty()
        status.write("סורק...")
        time.sleep(1)
        status.empty()
        #st.write("סורק...") זה שורת טעות ניתן למחוק  
        if url.startswith("https"):
            st.success(".האתר משתמש בפרוטוקול מאובטח")
        elif url.startswith("http"):
            st.warning("זהירות! האתר משתמש בפרוטוקול לא מאובטח")
        else:
            st.write(".כתובת לא תקינה או חסרת פרוטוקול")
    else:
        st.write("לא הוזנה כתובת לבדיקה")
st.button("בדוק מחדש",on_click=clear_text)

    
