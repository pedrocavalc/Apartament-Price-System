import streamlit as st
import base64

@st.cache_data
def get_img_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64('assets/side-bar.jpeg')


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image : url("https://rentpath-res.cloudinary.com/$img_current/t_3x2_webp_xl/t_unpaid/869c0cbe1b3e7ec5168fa8fd456f171f");
background-size: cover;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image : url("data:image/png;base64,{img}");
}}

[data-testid="stHeader"] {{
background-color: rgba(0, 0, 0, 0);
}}

</style>
"""

container = """
    <style>
    .info-container {
        background-color: #f0f2f6;
        border: 1px solid #e1e4e8;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    </style>
    <div class="info-container">
        <p><strong>Developed by Pedro Cavalcante.</strong> <a href="https://github.com/pedrocavalc" target="_blank">GitHub</a></p>
        <p>Trained on dataset from <a href="https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified" target="_blank">UCI Machine Learning Repository</a>.</p>
        <p>Goal: Learn MLOps techniques for production and deploy in Real Time Data.</p>
        <p>For more details, check the <a href="https://github.com/pedrocavalc/Apartament-Price-System" target="_blank">repository</a>.</p>
    </div>
    """


def container_page():
    currency = st.selectbox(
    'Currency?',
    ('USD', 'not_specified'))
    fee = st.selectbox('Have Fee?', ('Yes', 'No','not_specified'))
    pets = st.selectbox('Allow Pets?', ('Cats', 'Cats,Dogs', 'Dogs', 'Cats,Dogs,None'))


def main():
    st.markdown(page_bg_img,unsafe_allow_html=True)
    st.title("Welcome to apartment predictor price!")
    st.divider()
    st.sidebar.title("Informations about the project:")
    st.sidebar.info("Developed by Pedro Cavalcante. [GitHub](https://github.com/pedrocavalc)")
    st.sidebar.info("Trained on dataset from [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified).")
    st.sidebar.info("Goal: Learn MLOps techniques for production and deploy in Real Time Data.")
    st.sidebar.info("For more details, check the [repository](https://github.com/pedrocavalc/Apartament-Price-System).")
    container_page()



if __name__ == "__main__":
    main()