
import streamlit as st
import pickle as pkl
import numpy as np
import os



def load_model():
    
    model_path=os.path.join("notebook","out","best_model.pkl")
    # return model_path
    with open(model_path,'rb') as of:
        data=pkl.load(of)
    return data        

def show_predict_page():
    # credit_history=('1.,  0.')
    
    st.title("Loan Prediction Approval")
    st.write("""### We need some information to predict the loan approval""")
    gender=("Male","Female")
    married=("Yes","No")
    education=("Graduate","Not Graduate")
    self_employed=("Yes","No")
    area=('Urban', 'Rural', 'Semiurban')
    dependents=('0', '1', '2', '3+')
    # creating panel to select for dtype object
    gender = st.selectbox("Gender", gender)
    married = st.selectbox("Marital Status", married)
    education = st.selectbox("Education Level", education)
    self_employed=st.selectbox("Self Employment Status", self_employed)
    area=st.selectbox("Area Type",area)
    dependents=st.selectbox("Number of Dependents",dependents)
    # creating panels for dtype int
    credit_history = st.slider("Credit History",0,1)
    term = st.number_input("Insert Term: 360., 120., 240., 180.,  60., 300., 480.,  36.,  84.,  12.")
    applicant_income = st.number_input('Insert Applicant Income')
    coapplicant_income = st.number_input('Insert Coapplicant_Income')
    loan_amount = st.number_input('Insert Loan_Amount')

    # # using the inputs to ready the model input
    # ['Applicant_Income', 'Coapplicant_Income', 'Loan_Amount', 'Term',
    #    'Credit_History', 'Gender', 'Married', 'Dependents_0', 'Dependents_1',
    #    'Dependents_2', 'Dependents_3+', 'Education', 'Self_Employed',
    #    'Area_Rural', 'Area_Semiurban', 'Area_Urban', ]

    # columns which dont need to be processed:'Applicant_Income', 'Coapplicant_Income', 'Loan_Amount', 'Term','Credit_History'
    # columns that need to be processed are  'Gender', 'Married', 'Dependents_0', 'Dependents_1',
    #    'Dependents_2', 'Dependents_3+', 'Education', 'Self_Employed',
    #    'Area_Rural', 'Area_Semiurban', 'Area_Urban',
    # print(type(credit_history))
    if gender=="Male":
        gender=True
    else :
        gender=False    

    if married=="Yes":
        married=True    
    else:
        married=False
            
    Dependents_0,Dependents_1,Dependents_2,Dependents_3=False,False,False,False
    if dependents=="0":
        Dependents_0=True
    elif dependents=="1":
        Dependents_1=True
    elif dependents=="2":
        Dependents_2=True       
    elif dependents=="3+":
        Dependents_3=True

    if education=="Graduate":
        education=True
    else:
        education=False

    if self_employed=="Yes":
        self_employed=True    
    else:
        self_employed=False            

    Area_Rural, Area_Semiurban, Area_Urban=False,False,False                   
    if area=="Urban":
        Area_Urban=True
    elif area=="Rural":
        Area_Rural=True
    else:
        Area_Semiurban=True                

#   the numeric value needs to be scaled too which has not been done yet.
    user_value=np.array([[applicant_income,coapplicant_income,loan_amount,term,credit_history,gender,married,Dependents_0,Dependents_1,Dependents_2,Dependents_3,education,self_employed,Area_Rural,Area_Semiurban,Area_Urban]])
    model=load_model()
    print(user_value)
    ok = st.button("Calculate Salary")
    if ok:
        assigned=model.predict(user_value)
        st.write("Model Output",assigned)



if __name__=="__main__":
    page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))
    
    if page == "Predict":
        show_predict_page()
        
    else:
        show_predict_page()
        


    