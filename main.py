import streamlit as st
import pandas as pd
import json

# Load JSON data
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Convert member details to dataframe
def member_details_to_df(member_data):
    return pd.DataFrame([member_data]).transpose()

# Convert products to dataframe
def products_to_df(products):
    products_list = []
    for product in products:
        product_info = {key: product[key] for key in product if key != 'ingredients'}
        products_list.append(product_info)
    return pd.DataFrame(products_list).transpose()

# Convert ingredients to dataframe
def ingredients_to_df(ingredients):
    ingredients_list = []
    for ingredient in ingredients:
        ingredients_list.append(ingredient)
    return pd.DataFrame(ingredients_list).transpose()

# Streamlit app
def streamlit_app(data):
    st.title('Health and Nutrition Data Overview')

    # Member Details
    st.header('Member Details')
    member_df = member_details_to_df(data['data']['getPreliminaryPlan']['member'])
    st.table(member_df)

    # Product Details
    st.header('Products')
    products_df = products_to_df(data['data']['getPreliminaryPlan']['products'])
    st.table(products_df)

    # Ingredients Details
    st.header('Final Ingredients')
    ingredients_df = ingredients_to_df(data['data']['getPreliminaryPlan']['ingredients'])
    st.table(ingredients_df)

# Load the data
data = load_data('data.json')

# Run the app
streamlit_app(data)
