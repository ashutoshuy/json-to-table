import streamlit as st
import pandas as pd
import json

# Load JSON data
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Convert data to DataFrame and transpose
def data_to_df(data):
    return pd.DataFrame([data]).transpose()

# Streamlit app
def streamlit_app(data):
    st.title('Health and Nutrition Data Overview')

    # Member Details
    st.header('Member Details')
    member_df = data_to_df(data['data']['getPreliminaryPlan']['member'])
    st.table(member_df)

    # Products Details including nested products
    st.header('Products')
    for product in data['data']['getPreliminaryPlan']['products']:
        st.subheader(f"Product: {product['name']}")
        product_df = data_to_df({key: product[key] for key in product if key not in ['products', 'assessments']})
        st.table(product_df)

        # Specific Products
        if 'products' in product and product['products']:
            st.subheader('Specific Products')
            for specific_product in product['products']:
                specific_product_df = data_to_df(specific_product)
                st.table(specific_product_df)

        # Assessments
        if 'assessments' in product and product['assessments']:
            st.subheader('Assessments')
            assessments_df = pd.DataFrame(product['assessments'])
            st.table(assessments_df)

    # Final Ingredients
    st.header('Final Ingredients')
    ingredients_df = pd.DataFrame(data['data']['getPreliminaryPlan']['ingredients'])
    st.table(ingredients_df)

# Load the data
data = load_data('data.json')

# Run the app
streamlit_app(data)
