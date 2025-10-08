import streamlit as st

# 🔐 Құпиясөз
correct_password = "Мари"

# 👉 Құпиясөз сұрау
password = st.text_input("Құпиясөзді енгізіңіз:", type="password")

if password == correct_password:
    st.success("Қош келдіңіз!")

    st.title("📘 Әсемнің Бухгалтерия курсына қош келдіңіз! 😊")
    name = st.text_input("Атыңыз:")
    year = st.text_input("Туған жылыңыз (мысалы, 2001):")
    city = st.text_input("Қалаңыз:")

    if st.button("Жіберу"):
        if name and year and city:
            st.success("✅ Мәлімет Excel-ге сақталды!")
        else:
            st.warning("⚠️ Барлық жолдарды толтырыңыз!")

    st.markdown("---")
    st.header("📚 Курс бөлімдері")

    # 🔗 Бөлімдерге сілтемелер
    st.page_link("pages/1_Kirispe.py", label="1-бөлім: Кіріспе", icon="🔰")
    st.page_link("pages/2_ashu.py", label="2-бөлім: ИП ашу", icon="🏢")
    st.page_link("pages/3_tapsyrma.py", label="3-бөлім: Тапсырма", icon="📝")
    st.page_link("pages/4_sabaq.py", label="4-бөлім: Сабақ", icon="📖")
    st.page_link("pages/5_barlygy.py", label="5-бөлім: Құжаттар", icon="📁")
    st.page_link("pages/6_esepter.py", label="6-бөлім: Есептер", icon="📊")
    st.page_link("pages/7_korytyndy.py", label="7-бөлім: Қорытынды", icon="✅")

else:
    if password:
        st.error("❌ Құпиясөз қате!")
    else:
        st.info("🔐 Құпиясөз енгізіңіз")

















































