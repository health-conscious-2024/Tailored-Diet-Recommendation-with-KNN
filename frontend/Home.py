import streamlit as st

st.set_page_config(page_title="Home", page_icon="🥗", layout="wide")

link = "https://github.com/Rohithkumar77/Tailored-Diet-Recommendation-System/raw/main/assets/Tlogo.png"
markdown_content = f"""
    <div style='display: flex; align-items: center;'>
        <span style='color: black; font-size: 42px; font-weight: bold; margin-top: -5px;'>Welcome to Tailored Diet Recommendation System</span>
    </div>
    <style>
        @media only screen and (max-width: 600px) {{
            span {{
                font-size: 24px !important;
            }}
        }}
    </style>
"""
st.markdown(markdown_content, unsafe_allow_html=True)

def main():
    st.sidebar.markdown(f"""<span style='color: black;font-size: 36px;font-weight: bold;'>
                                <img src='{link}' style='width: 40px; height: 40px; border-radius: 50px;'/> 
                                Diet Recommendation</span>""", unsafe_allow_html=True)
    st.sidebar.info("Welcome to our project diet recommendation. Here you can analyze the nutritional value of food")
    st.sidebar.subheader("Check out our [Github Repository](https://github.com/health-conscious-2024/Tailored-Diet-Recommendation-with-KNN)")

    st.subheader("Your personalized diet and nutrition assistant.")

    # About section
    with st.container():
        st.write("Our diet recommendation system is designed to help you make healthier food choices and achieve your nutrition goals. With our system, you can:")
        st.write("- Generate personalized meal plans based on your dietary preferences and nutritional needs")
        st.write("- Get detailed nutrition information of foods")

    # Features section
    with st.container():
        st.write("Our system offers the following features:")
        col1, col2 = st.columns(2)
        with col1:
            st.image("./assets/diet.jpeg", width=350) 
            st.write("🍽️ Generalized Recommendation")

        with col2:
            st.image("./assets/custom.jpeg", width=350)
            st.write("🧑‍🍳 Tailored Recommendation")

    # How It Works section
    with st.container():
        st.markdown(f""" 
        <h4> Simple step-by-step process for Generalized Recommendation: </h4>
        """, unsafe_allow_html=True)
        steps = [
            "1. Enter age,height, weight, gender and activity level.",
            "2. Select your weight loss goal which includes Maintain weight, lose weight and gain weight and select how many meals per day.",
            "3. Click on generate button and The system generates a personalized meal plan and detail recipe instructions.",
            "4. Access detailed nutritional information for each recommended recipe."
            ]
        for step in steps:
            st.write(step)
        st.markdown(f""" 
        <h4> Simple step-by-step process for Tailored Recommendation: </h4>
        """, unsafe_allow_html=True)   
        steps = [
            "1. Enter calories, fat content,saturated fat content, cholesterol content, sodium content,carbohydrate content, fiber content, sugar content, and protein content.",
            "2. select how many recommendations  and Click in generate button.",
            "3. The system generates Detailed recipe instructions .",
            "4. Access detailed nutritional information for each recommended recipe."
            ]
        for step in steps:
            st.write(step)

    # Benefits section
    with st.container():
        st.header("Benefits")
        st.write("By using our diet recommendation system, you can enjoy several benefits:")
        benefits = [
            "- Personalized meal plans tailored to your needs and preferences.",
            "- Access to a wide range of recipes that meet your nutritional goals.",
            "- Detailed nutritional information for each recipe to help you make informed dietary choices.",
            ]
        for benefit in benefits:
            st.write(benefit)

if __name__ == "__main__":
    main()
