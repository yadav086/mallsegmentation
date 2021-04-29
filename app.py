import streamlit as st
import pickle
import joblib


model_dc = pickle.load(open('seg_dc.pkl','rb'))
model_rf = pickle.load(open('seg_rf.pkl','rb'))
model_ct = pickle.load(open('seg_ct.pkl','rb'))
model_xg = joblib.load('seg_xg.pkl','rb')

def mall():

	st.title('Social Network Add predication')
	activities =['Decision Tree','Random Forest','Xgboost','Catboost']
	option = st.sidebar.selectbox('Which model do you want to select ?',activities)

	gender = st.selectbox('Select the Gender',('Male','Female'))
	if gender=='Male':
		gender=0
	else:
		gender=1

	age = st.slider('Select the age',0,100)
	salary = st.slider('Select the salary ',0,1000000)

	inputs= [[gender,age,salary]]

	if option== 'Decision Tree':
		model_dc.predict(inputs)
	elif option== 'Random Forest':
		model_rf.predict(inputs)	
	elif option== 'Xgboost':
		model_xg.predict(inputs)
	else:
		model_ct.predict(inputs)


	if st.button('Predict'):
		if model_dc.predict(inputs)[0]==0 or model_rf.predict(inputs)[0]==0 or model_xg.predict(inputs)[0]==0 or model_ct.predict(inputs)[0]==0:
		 	st.success('The user will click on the Advertisement.')
		else:
		 	st.success('he user will not click on the Advertisement.')


if __name__=='__main__':
	mall()
