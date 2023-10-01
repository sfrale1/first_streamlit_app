import pandas; 
import streamlit; 
streamlit.title ('My Mom\'s New Healthy Diner');

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt");


streamlit.header ('Breakfast Favorites ');

streamlit.text ('🥣 Omega3 & Blueberry Oatmeal ');
streamlit.text ('🥗 Kale, Spinach & Rocket Smoothie ');
streamlit.text ('🐔 Hard-Boiled Free-Range Egg ');
streamlit.text ('🥑🍞 Avocado Toast' );

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇');
# Let's put a pick list here so they can pick the fruit they want to include 

my_fruit_list = my_fruit_list.set_index('Fruit'); 

fruits_selectd = streamlit.multiselect("Pick some fruits:", list (my_fruit_list.index),  ['Lime','Orange']);
fss = my_fruit_list.loc(fruits_selected);
streamlit.write(fruits_selectd); 

#streamlit.dataframe(fruits_selected);

streamlit.dataframe(my_fruit_list);

#fruits_to_show = my_fruit_list.loc[fruits_selectd];
#streamlit.dataframe(fruits_to_show);

