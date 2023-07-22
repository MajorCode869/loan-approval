import streamlit as st
import pickle as pkl
import numpy as np
import os

def __init__():
    return

def load_model():
    
    model_path=os.path.join("notebook","out","best_model.pkl")
    # return model_path
    with open(model_path,'rb') as of:
        data=pkl.load(of)
    return data        

def show_pedict_page():
    st.title("Loan Prediction Approval")
    # st.write("Input values to predict the Loan Approval")
# if __name__=="__main__":
#     path=load_model()
#     print(path)    