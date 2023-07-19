import streamlit as st
from joblib import load
import numpy as np


# import model
pipe = load("pipe.pkl")
# df = pickle.load(open('df.pkl','rb'))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox('Brand',['HP','Dell','Lenovo','Asus','Acer','MSI','Toshiba'])

# type of laptop
type = st.selectbox('Type',['Notebook', 'Gaming', 'Ultrabook', '2 in 1 Convertible', 'Workstation', 'Netbook'])

# inches
inches =  st.number_input('In inches')

# cpu
cpu = st.selectbox('CPU',['Intel', 'AMD'])

# ram
ram = st.selectbox('RAM',[4,8, 16, 6, 12, 2, 32, 24])

# memory
memory = st.selectbox("Storage memory in GB, '1' for TB ",[256, 1, 128, 500, 512, 32])

# gpu
gpu = st.selectbox('GPU',['Intel', 'Nvidia', 'AMD'])

# OpSys
OpSys = st.selectbox('Operating System',['Windows ', 'Linux', 'No OS'])

# weight
weight  = st.number_input("Weight of The Laptop")

screen_width = st.selectbox('Screen Width',[1600,1366,1920, 2560,3200, 3840])
screen_height = st.selectbox('Screen Height',[768,900,1080,1440, 1800, 2160])

if st.button('Predict Price'):

    query = np.array([company,type,inches,cpu,ram,memory,gpu,OpSys,weight,
                      screen_width,
                      screen_height])
    query = query.reshape(1,11)
    st.title("The predicted price of the Laptop is Rs. " + str(int(np.exp(pipe.predict(query)))))

