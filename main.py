import requests
import streamlit as st

st.header('Savory Secrets')
input_name = st.text_input("Enter Dish:")
clickbutton = st.button("Check")

if clickbutton:

	url = "https://recipe-by-api-ninjas.p.rapidapi.com/v1/recipe"

	querystring = {"query": input_name}

	headers = {
		"X-RapidAPI-Key": "3219a68b92msh29b6e8a5f3ac678p1f555fjsnd1399975bbb0",
		"X-RapidAPI-Host": "recipe-by-api-ninjas.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	print(response.json())
	output = response.json()
	var1 = output[0]["title"]
	var2 = output[1]["ingredients"]
	var3 = output[3]["instructions"]
	print(var1)
	print(var2)
	print(var3)
	st.caption('recipe')
	st.info(var1)
	st.caption('Ingredients')
	st.info(var2)
	st.caption('Instructions')
	st.info(var3)