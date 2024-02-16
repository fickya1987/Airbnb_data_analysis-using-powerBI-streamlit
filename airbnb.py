# Importing Libraries
import pandas as pd
import pymongo
import pymysql
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
from pymongo import MongoClient



import pymysql
from sqlalchemy import create_engine
# import sql
connection_params = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Nahid123',
}
connection = pymysql.connect(**connection_params)
cursor = connection.cursor()
database_name = 'airbnb'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
connection = pymysql.connect(host= 'localhost',user = 'root',password = 'Nahid123',database = 'AIRBNB')
cursor = connection.cursor()

engine = create_engine('mysql+pymysql://root:Nahid123@localhost/AIRBNB', echo=False)


def country_list():
    cursor.execute(f"""select distinct Country
                        from airbnb;""")
    data = cursor.fetchall()
    original_country= [i[0] for i in data]
    return original_country   

def property_type():
    cursor.execute(f"""select distinct Property_type
                        from airbnb;""")
    data =cursor.fetchall()
    property_type = [i[0] for i in data]
    return property_type  


def Room_type():
    cursor.execute(f"""select distinct Room_type
                        from airbnb;""")
    data = cursor.fetchall()
    Room_type = [i[0] for i in data]
    return Room_type





icon = Image.open("ICN.png")
# icon = Image.open("ICN.png")
st.set_page_config(page_title= "Airbnb Data Visualization | By Nahid Banu",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Nahid Banu*!
                                        Data has been gathered from mongodb atlas"""}
                  )


# setting background image 
def setting_bg(background_image_url):
    st.markdown(f""" 
    <style>
        .stApp {{
            background: url('{background_image_url}') no-repeat center center fixed;
            background-size: cover;
            transition: background 0.5s ease;
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: #f3f3f3;
            font-family: 'Roboto', sans-serif;
        }}
        .stButton>button {{
            color: #4e4376;
            background-color: #f3f3f3;
            transition: all 0.3s ease-in-out;
        }}
        .stButton>button:hover {{
            color: #f3f3f3;
            background-color: #2b5876;
        }}
        .stTextInput>div>div>input {{
            color: #4e4376;
            background-color: #f3f3f3;
        }}
    </style>
    """, unsafe_allow_html=True)

# # Background image
background_image_url = "https://media.cntraveller.com/photos/63bd91b73c7bca633cbfe0fb/16:9/w_1920%2Cc_limit/airbnb.jpg"
setting_bg(background_image_url)


box_style = """
    <style>
        .box {
            border: 2px solid #3F1209;
            padding: 20px;
            border-radius: 10px;
            background-color: #F7E4DE;
        }
    </style>
"""

# Apply the CSS style and the text within a box
st.markdown(box_style, unsafe_allow_html=True)
st.markdown("<div class='box'><h1 style='text-align: center; color:red; font-size:50px;'>Airbnb Data Visualization</h1></div>", unsafe_allow_html=True)


with st.sidebar:
    selected = option_menu("Menu", ["Home","Data Overview","Data Visualization", "Data Analysis"], 
                           icons=["house","graph-up-arrow","bar-chart-line","bar-chart-line"],
                           menu_icon= "menu-button-wide",
                           default_index=0,
                            styles={"nav-link": {"font-size": "20px", "text-align": "left", "margin": "-2px", "--hover-color": "#FF5A5F"},
                                    "nav-link-selected": {"background-color": "#FF5A5F"}}
                          )



client =pymongo.MongoClient("mongodb+srv://nahidkaramala:1234@cluster0.6indntk.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_airbnb
col = db.listingsAndReviews

# READING THE DATAFRAME
df = pd.read_csv('Airbnb_data.csv')

if selected == "Home":

    st.markdown("## <span style='color:red'>Domain</span> : <span style='color:blue'>Travel Industry, Property Management and Tourism</span>", unsafe_allow_html=True)
    st.markdown("## <span style='color:red'>Technologies used </span>: <span style='color:blue'>Python, Pandas, Plotly, Streamlit, MongoDB</span>", unsafe_allow_html=True)
    st.markdown("## <span style='color:red'>Overview </span>: <span style='color:blue'>To analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.</span>", unsafe_allow_html=True)


if selected == "Data Overview":
    select = st.selectbox("Select data view", ["View Raw Data", "View Curated Data"])
        
    if select=="View Raw Data":
        st.write(col.find_one())
    
    if select=="View Curated Data":
        st.write(df)
    



if selected=="Data Visualization": 
    country = st.sidebar.multiselect('Select a Country',country_list())
    prop = st.sidebar.multiselect('Select Property_type',property_type())
    room = st.sidebar.multiselect('Select Room_type',Room_type())
    price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))
    
    # CONVERTING THE USER INPUT INTO QUERY
    query = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'
    
    # CREATING COLUMNS
    col1,col2 = st.columns(2,gap='medium')
    
    with col1:
        
        # TOP 10 PROPERTY TYPES BAR CHART
        df1 = df.query(query).groupby(["Property_type"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
        fig = px.bar(df1,
                        title='Top 10 Property Types',
                        x='Listings',
                        y='Property_type',
                        orientation='h',
                        color='Property_type',
                        color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True) 
    
        # TOP 10 HOSTS BAR CHART
        df2 = df.query(query).groupby(["Host_name"]).size().reset_index(name="Listings").sort_values(by='Listings',ascending=False)[:10]
        fig = px.bar(df2,
                        title='Top 10 Hosts with Highest number of Listings',
                        x='Listings',
                        y='Host_name',
                        orientation='h',
                        color='Host_name',
                        color_continuous_scale=px.colors.sequential.Agsunset)
        fig.update_layout(showlegend=False)
        st.plotly_chart(fig,use_container_width=True)
    
    with col2:
        
        # TOTAL LISTINGS IN EACH ROOM TYPES PIE CHART
        df1 = df.query(query).groupby(["Room_type"]).size().reset_index(name="counts")
        fig = px.pie(df1,
                        title='Total Listings in each Room_types',
                        names='Room_type',
                        values='counts',
                        color_discrete_sequence=px.colors.sequential.Rainbow
                    )
        fig.update_traces(textposition='outside', textinfo='value+label')
        st.plotly_chart(fig,use_container_width=True)
        
        # TOTAL LISTINGS BY COUNTRY CHOROPLETH MAP
        country_df = df.query(query).groupby(['Country'],as_index=False)['Name'].count().rename(columns={'Name' : 'Total_Listings'})
        fig = px.choropleth(country_df,
                            title='Total Listings in each Country',
                            locations='Country',
                            locationmode='country names',
                            color='Total_Listings',
                            color_continuous_scale=px.colors.sequential.Plasma
                            )
        st.plotly_chart(fig,use_container_width=True)



if selected=="Data Analysis":
    st.markdown("## Analysis of Airbnb data")
    
    # GETTING USER INPUTS
    country = st.sidebar.multiselect('Select a Country',country_list())
    prop = st.sidebar.multiselect('Select Property_type',property_type())
    room = st.sidebar.multiselect('Select Room_type',Room_type())
    price = st.slider('Select Price',df.Price.min(),df.Price.max(),(df.Price.min(),df.Price.max()))

    # CONVERTING THE USER INPUT INTO QUERY
    query = f'Country in {country} & Room_type in {room} & Property_type in {prop} & Price >= {price[0]} & Price <= {price[1]}'
    
    # HEADING 1
    st.markdown("## $ Price Analysis")
    
    # CREATING COLUMNS
    col1,col2 = st.columns(2,gap='medium')
    
    with col1:
        
        # AVG PRICE BY ROOM TYPE BARCHART
        pr_df = df.query(query).groupby('Room_type',as_index=False)['Price'].mean().sort_values(by='Price')
        fig = px.bar(data_frame=pr_df,
                     x='Room_type',
                     y='Price',
                     color='Price',
                     title='Avg Price in each Room type'
                    )
        st.plotly_chart(fig,use_container_width=True)
        
        # HEADING 2
        st.markdown("## 🏠 Availability Analysis")
        
        # AVAILABILITY BY ROOM TYPE BOX PLOT
        fig = px.box(data_frame=df.query(query),
                     x='Room_type',
                     y='Availability_365',
                     color='Room_type',
                     title='Availability by Room_type'
                    )
        st.plotly_chart(fig,use_container_width=True)
        
    with col2:
        
        # AVG PRICE IN COUNTRIES SCATTERGEO
        country_df = df.query(query).groupby('Country',as_index=False)['Price'].mean()
        fig = px.scatter_geo(data_frame=country_df,
                                       locations='Country',
                                       color= 'Price', 
                                       hover_data=['Price'],
                                       locationmode='country names',
                                       size='Price',
                                       title= 'Avg Price in each Country',
                                       color_continuous_scale='agsunset'
                            )
        col2.plotly_chart(fig,use_container_width=True)
        
        # BLANK SPACE
        st.markdown("#   ")
        st.markdown("#   ")
        
        # AVG AVAILABILITY IN COUNTRIES SCATTERGEO
        country_df = df.query(query).groupby('Country',as_index=False)['Availability_365'].mean()
        country_df.Availability_365 = country_df.Availability_365.astype(int)
        fig = px.scatter_geo(data_frame=country_df,
                                       locations='Country',
                                       color= 'Availability_365', 
                                       hover_data=['Availability_365'],
                                       locationmode='country names',
                                       size='Availability_365',
                                       title= 'Avg Availability in each Country',
                                       color_continuous_scale='agsunset'
                            )
        st.plotly_chart(fig,use_container_width=True)


    
    
