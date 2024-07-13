import streamlit as st

import pandas as pd
import numpy as np

import pickle

data =pd.read_csv("finaldata.csv")
# data1 =pd.read_csv('encodeddata.csv')

#streamlit part
st.set_page_config(layout="wide")

with open(r'style1.css') as f:
  st.markdown(f"""<style>{f.read()}</style>""", unsafe_allow_html=True)

with st.sidebar:
  st.title(" :violet[WELCOME TO MY PROJECT]")
  st.header("skill Take Away" ,divider='rainbow')
  st.caption(":black_circle: :blue[_python Scripting_]")
  st.caption(":black_circle: :blue[_Data Exploration_]")
  st.caption(":black_circle: :blue[_Data Preprocessing_]")
  st.caption(":black_circle: :blue[_Data Visualization_]")
  st.caption(":black_circle: :blue[_Feature Selection_]")
  st.caption(":black_circle: :blue[_Feature Scaling_]")
  st.caption(":black_circle: :blue[_Model Selection_]")
  st.caption(":black_circle: :blue[_Model Train_]")
  st.caption(":black_circle: :blue[_Hyperparameter Tuning_]")
  st.caption(":black_circle: :blue[_Prediction_]")
  st.caption(":black_circle: :blue[_Building Streamlit_]")   

tab1,tab2 = st.tabs([":black[🏛️ Home]",":black[📜 Form]"])
with tab1: 

    st.title(":black[Welcome TO Singapore Real Estates]") #🌍

    st.image("https://upload.wikimedia.org/wikipedia/commons/a/ac/Singapore_skyline_at_sunset_viewed_from_Gardens_by_the_Bay_East_-_20120426.jpg", caption=None, 
              width=None, use_column_width=None, clamp=False,
              channels="RGB", output_format="auto") 
with tab2:
    st.markdown("""
            <h2 style =" text-align : center;  color:purple;">
            Resale-Flat Price Prediction Model 🕵️‍♀️🏛️ 
            </h2>
        """, unsafe_allow_html=True)  
    
    with open('label_encoder.pkl', 'rb') as file:
        loaded_label_encoder = pickle.load(file) 
    with open('Label_Encoder2.pkl', 'rb') as file:
       loaded_Label_Encoder2 = pickle.load(file)
    with open('Label_Encoder3.pkl', 'rb') as file:
        loaded_Label_Encoder3 = pickle.load(file)
    with open('Label_Encoder4.pkl', 'rb') as file:
        loaded_Label_Encoder4 = pickle.load(file)  
    with open('scaled.pkl', 'rb') as file:
        loaded_scaled = pickle.load(file)     
    with open('LR1.pkl', 'rb') as file:
        loaded_LR1 = pickle.load(file)
    

    def main():
      # Form content
        col1,col2,col3 = st.columns([1,2,1])
        with col2: 
            with st.form(key='my_form'):
                st.subheader(':orange[Please enter information:]')

                css = """
                        <style>
                        label {
                            color: purple !important;
                        }
                        </style>
                        """
            # Display the custom CSS
                st.markdown(css, unsafe_allow_html=True)

            
                town = st.selectbox('Town_Name',('ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                                                'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
                                                'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                                                'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
                                                'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
                                                'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
                                                'PUNGGOL'))
                # col1,col2 = st.columns(2)
                # with col1:
                flat_type =st.radio("Select the Flat_type:",['1 ROOM', '2 ROOM', '3 ROOM','4 ROOM', '5 ROOM', 'EXECUTIVE','MULTI GENERATION'])
                # with col2:
                #   flat_type =st.radio(['4 ROOM', '5 ROOM', 'EXECUTIVE','MULTI GENERATION'],index=None)    
              
                street_name = st.selectbox('Street_Name',(data["street_name"].unique()))
                floor_area_sqm = st.number_input('Required Floor Area',value=None, placeholder="Type a number...")
                
                flat_model = st.selectbox('Select the Flat_Model', ['IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED',
                                                'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE',
                                                '2-ROOM', 'IMPROVED-MAISONETTE', 'MULTI GENERATION',
                                                'PREMIUM APARTMENT', 'Improved', 'New Generation', 'Model A',
                                                'Standard', 'Apartment', 'Simplified', 'Model A-Maisonette',
                                                'Maisonette', 'Multi Generation', 'Adjoined flat',
                                                'Premium Apartment', 'Terrace', 'Improved-Maisonette',
                                                'Premium Maisonette', '2-room', 'Model A2', 'DBSS', 'Type S1',
                                                'Type S2', 'Premium Apartment Loft', '3Gen'])
            
                lease_commence_date =st.slider("Select the Lease_Commence_Date:",1966,2020,1966)#data['lease_commence_date'].min(),data['lease_commence_date'].max(),data['lease_commence_date'].min()) 
                years =st.slider("Select the Flat_year:",1990,2024,1990) 
                month =st.slider("Select the Flat_Month:",1,12,1)
                storey_start =st.slider("Select the storey_start_range:",1,49,1)
                storey_end =st.slider("Select the storey_end_range:",3,51,3)#data1['storey_range_end'].min(),data1['storey_range_end'].max(),data1['storey_range_end'].min())
                st.checkbox(':violet[I agree to the terms and conditions]')
   
                submitted = st.form_submit_button(":violet[Submit]")
                    
                if submitted:
                            
                    user= {'town' :town,'flat_type':flat_type,
                            'street_name':street_name,'floor_area_sqm':floor_area_sqm,
                            'flat_model':flat_model,'lease_commence_date':lease_commence_date,
                            'year':years,'Month':month ,'storey_range_start':storey_start,
                            'storey_range_end':storey_end }
                    user = pd.DataFrame(user,index=[0])
                    

                    user['town'] =loaded_label_encoder.transform(np.array([user['town']])),  
                    user['flat_type'] = loaded_Label_Encoder2.transform(np.array([user['flat_type']])), 
                    user['street_name'] =loaded_Label_Encoder3.transform(np.array([user['street_name']])),
                    user['flat_model'] =loaded_Label_Encoder4.transform(np.array([user['flat_model']]))

                    list_scaled = loaded_scaled.transform(user)
                    
                    Price =loaded_LR1.predict (list_scaled)   #model  #loaded_rfr.predict([[4,2,6,600,3,2000,2012,12,5,10]])[0]
                       
                    st.subheader(":violet[Price Predicted for the selected House model]:house:")  
                    st.subheader('$'+str(np.round(Price[0],2)))

    if __name__ == '__main__':
        main()
 #town	flat_type	street_name	street_name	flat_model	lease_commence_date	resale_price
 # 	year	Month	storey_range_start	storey_range_end
