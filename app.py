import streamlit as st

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity



st.title('My first ')
#TF Idf talk about it

#my_dataframe =pd.read_csv(r'C:\Users\frank\Desktop\project\eda\all_data.csv')
#st.dataframe(my_dataframe)
#st.file_uploader('File uploader')

def load_data(data):
    df=pd.read_csv(r'C:\Users\frank\Desktop\project\eda\ecommerce.csv')
    return df

#vectorize text and get cosine similarity
def vectorizer():
    count_vect = CountVectorizer()
    cv_mat = count_vect.fit_transform(data)
    cosine_sim_mat = cosine_similarity(cv_mat)
    return cosine_sim_mat


def get_recommendation(title,cosine_sim_mat,df,numberofrecommendations)
    #index
    product_index = pd.Series(df.index,index=df['product_name']).drop_duplicates
    idx  = product_index[title]

    

def main():
    st.title("Product recommation")

    menu = ["Home", "Recommend"]
    choice = st.sidebar.selectbox("Menu",menu)

    df= load_data(r'C:\Users\frank\Desktop\project\eda\ecommerce.csv')

    if choice =="Home":
        st.subheader("Home")
        st.dataframe(df.head(10))
    
    elif choice == "Recommend":
        st.subheader("Recommend Product")
        search_term = st.text_input("Enter a product name")
        numberofrecommendations = st.sidebar.number_input("Number",4,30,7)

    else:
        st.subheader("About")
        st.text("lalala")

if __name__=='__main__':
    main()