# Airbnb_data_analysis-using-powerBI-streamlit
Airbnb data analysis project using Python, fetching data from Mongo Atlas, data cleaning, preprocessing, Data reading using EDA, Data Visualization using matplotlib.plotly and Data Analysis by PowerBI

## Domain : 
Travel Industry, Property management and Tourism
## Problem Statement :
This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.

## Airbnb Dashboard Link : [![Click view Dashboard](https://img.shields.io/badge/Your_Text-Your_Color?style=flat-square&logo=Your_Logo)](http://example.com](https://github.com/Nahidkaramala/Airbnb_data_analysis-using-powerBI-streamlit/blob/main/airbnb.pbix)https://github.com/Nahidkaramala/Airbnb_data_analysis-using-powerBI-streamlit/blob/main/airbnb.pbix)

## Libraries/Modules needed for the project!
Plotly, Seaborn - (To plot and visualize the data)
Pandas - (To Clean and maipulate the data)
Pymongo - (To store and retrieve the data by connecting with MongoDB Atlas)
Streamlit - (To Create Graphical user Interface)
## Workflow :
### Step 1 :
Establish a connection to the MongoDB Atlas database and retrieve the Airbnb dataset.

#### Example AIRBNB data structure:
	{"_id": "unique_listing_id",
 	 "name": "listing_title",
 	 "description": "listing_description",
  	"host_id": "unique_host_id",
 	 "host_name": "host_name",
 	 "neighbourhood": "neighbourhood_name",
 	 "location": {
"type": "Point",
   			 "coordinates": [longitude, latitude]
 			 },
  	"price": "listing_price",
 	 "availability": {
   			 "start_date": "YYYY-MM-DD",
   			 "end_date": "YYYY-MM-DD"
  },
  	"amenities": ["amenity_1", "amenity_2", ...],
  	"rating": "average_rating",
 	 "reviews": [
    			{
     			 "reviewer_id": "unique_reviewer_id",
      			"reviewer_name": "reviewer_name",
      			"comment": "review_comment",
     			 "rating": "review_rating"
   			 }, ...
 			 ], ...
}



### Step 2 :
Clean the Airbnb dataset by handling missing values, removing duplicates, and transforming data types as necessary. Prepare the dataset for EDA and visualization tasks, ensuring data integrity and consistency.

### Step 3 :
Develop a streamlit web application that utilizes the geospatial data from the Airbnb dataset to create interactive maps.

### Step 4 :
Use the cleaned data to analyze and visualize how prices vary across different locations, property types, and seasons. Create dynamic plots and charts that enable users to explore price trends, outliers, and correlations with other variables.

### Step 5 :
Power BI to create a comprehensive dashboard that presents key insights from your analysis. Combine different visualizations, such as maps, charts, and tables, to provide a holistic view of the Airbnb dataset and its patterns.

