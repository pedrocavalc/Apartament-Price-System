import streamlit as st
import base64
import json
import requests

API_URL = "http://127.0.0.1:8000/predict"

@st.cache_data
def get_img_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

side_img = get_img_as_base64('assets/side-bar.jpeg')
home_img = get_img_as_base64('assets/homepage.jpg')

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image : url("data:image/png;base64,{home_img}");
background-size: cover;
}}

[data-testid="stSidebar"] > div:first-child {{
background-image : url("data:image/png;base64,{side_img}");
}}

[data-testid="stHeader"] {{
background-color: rgba(0, 0, 0, 0);
}}


div[data-testid="stSidebarUserContent"] .stMarkdown {{
    color: white;
}}

</style>
"""


def send_info_to_API(currency,city, fee, bathrooms,  bedrooms, square_feet, pets, category, price_type, state) -> requests.Response:
    """
    Sends image to the API endpoint for prediction.
    """
    body_json = {
        "currency": currency, 
        "fee": fee,
        "pets_allowed": pets, 
        "category": category, 
        "cityname": city, 
        "price_type":price_type, 
        "state":state, 
        "bathrooms":bathrooms, 
        "bedrooms":bedrooms, 
        "square_feet":square_feet
    }
    response = requests.post(API_URL, json=body_json)
    response_dict = json.loads(response.text)
    return response_dict['prediction']

def container_page():
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
        font-weight: bold;
    }
    .button-font {
        font-size: 20px !important;
        font-weight: bold;
        color: black;
    }
    .form-box {
        background-color: #f0f0f0;  
        padding: 10px;
        border-radius: 10px;
        margin: 5px 0;
        font-size: 20px !important;
        font-weight: bold;
        color: black;
    }
    .est-box {
    border: 2px solid #4CAF50; /* Verde claro */
    background-color: #f1f1f1; /* Cinza muito claro */
    border-radius: 10px; /* Cantos arredondados */
    padding: 10px; /* Espaço interno */
    font-size: 60px; /* Tamanho da fonte aumentado */
    font-weight: bold; /* Deixa o texto em negrito */
    color: red; /* Cor da fonte vermelha */
    text-align: center; /* Centraliza o texto */
    margin: 10px 0; /* Margem acima e abaixo */
}
    </style>
    """, unsafe_allow_html=True)



    st.markdown('<p class="big-font">Currency?</p>', unsafe_allow_html=True)
    currency = st.selectbox(
    'Currency?',
    ('USD', 'not_specified'))

    st.markdown('<p class="big-font">Enter the city where you will buy the apartment</p>', unsafe_allow_html=True)
    city = st.text_area('', 'New York')

    st.markdown('<p class="big-font">Have fee?</p>', unsafe_allow_html=True)
    fee = st.selectbox('', ('Yes', 'No','not_specified'))

    st.markdown('<p class="big-font">Number of bathrooms</p>', unsafe_allow_html=True)
    bathrooms = int(st.selectbox('', ('1', '2', '3', '4', '5', 'not_specified',)))

    st.markdown('<p class="big-font">Number of bedrooms</p>', unsafe_allow_html=True)
    bedrooms = int(st.selectbox('', ('1', '2', '3', '4', '5', 'not_specified'),key = 'bed'))

    st.markdown('<p class="big-font">Square Feet</p>', unsafe_allow_html=True)
    square_feet = st.number_input('', min_value = 10, max_value = 800, placeholder='Type the square feet of the apartment')
    
    st.markdown('<p class="big-font">Allow Pets?</p>', unsafe_allow_html=True)
    pets = st.selectbox('', ('Cats', 'Cats,Dogs', 'Dogs', 'Cats,Dogs,None','not_specified',))
    
    st.markdown('<p class="big-font">Category?</p>', unsafe_allow_html=True)
    category = st.selectbox('', ('housing/rent/apartment', 'housing/rent/home', 'housing/rent/short_term', 'not_specified', 'housing/rent', 'housing/rent/condo', 'housing/rent/other', 'housing/rent/commercial/retail', 'not_specified',))
    
    st.markdown('<p class="big-font">Price Type?</p>', unsafe_allow_html=True)
    price_type = st.selectbox('', ('Monthly', 'Weekly', 'Monthly|Weekly', 'not_specified',))
    
    st.markdown('<p class="big-font">State?</p>', unsafe_allow_html=True)
    state = st.text_area('', placeholder='Type the UF of the city')
    
    
    predict_button = st.button('Predict')
    
    if predict_button:  
        prediction = send_info_to_API(currency, city, fee, bathrooms, bedrooms, square_feet, pets, category, price_type, state)
        st.markdown(f'<div class= "form-box" <p class="button-font"> The predicted price is: {round(prediction,2)} USD</p> </div>', unsafe_allow_html=True)
        


def main():
    st.markdown(page_bg_img,unsafe_allow_html=True)
    st.title("Welcome to apartment predictor price!",)
    st.divider()
    container_page()


    # Definindo as informações com o estilo personalizado
    info1 = "<div style='background-color:rgba(128, 0, 32, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px; font-size: 16px;'>Developed by Pedro Cavalcante. <a href='https://github.com/pedrocavalc' target='_blank'>GitHub</a></div>"
    info2 = "<div style='background-color:rgba(128, 0, 32, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px; font-size: 16px;'>Trained on dataset from <a href='https://archive.ics.uci.edu/dataset/555/apartment+for+rent+classified' target='_blank'>UCI Machine Learning Repository</a>.</div>"
    info3 = "<div style='background-color:rgba(128, 0, 32, 0.8); padding: 10px; border-radius: 5px; margin-bottom: 10px; font-size: 16px;'>Goal: Learn MLOps techniques for production and deploy in Real Time Data.</div>"
    info4 = "<div style='background-color:rgba(128, 0, 32, 0.8); padding: 10px; border-radius: 5px; font-size: 16px;'>For more details, check the <a href='https://github.com/pedrocavalc/Apartament-Price-System' target='_blank'>repository</a>.</div>"

    st.sidebar.title("Informations about the project:")

    # Usando Markdown para exibir as informações com estilo personalizado
    st.sidebar.markdown(info1, unsafe_allow_html=True)
    st.sidebar.markdown(info2, unsafe_allow_html=True)
    st.sidebar.markdown(info3, unsafe_allow_html=True)
    st.sidebar.markdown(info4, unsafe_allow_html=True)

if __name__ == "__main__":
    main()