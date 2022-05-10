# Import libraries 
import pandas as pd 
import plotly.express as px 
import json 

# ------------------------------
#       DATA TREATMENT
# ------------------------------
# Open geojson file with doors layout 
  with open('pia2.geojson') as response:
    doors = json.load(response)

# Create Pandas Dataframe from Form

# Create Pandas Dataframe from Form


 df_doors = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQzLHhweuUH0meMW0QfQrNCbat0Rw73fEBpBgKU-LQOlSqOTVQ0xMHhquDh-gAo9SNj50xbP1bULh87/pub?gid=404140102&single=true&output=csv')

  # Create Map 
  doors_map = px.choropleth_mapbox(df_doors, 
        geojson=doors,locations='name',featureidkey='properties.name',color='occupancy',
                                    color_continuous_scale="Reds",                           
                                    mapbox_style="carto-positron",
                                    center=dict(lon=-8.674051848928324, lat=39.63074957184749),
                                    zoom=16,
                                    opacity=0.6,
                                    height=900
  )
  # Do some styling Color Axis should be turned to False for produciton. 
  doors_map.update_layout(margin={"r":15,"t":0,"l":15,"b":0},coloraxis_showscale=True)

  # Make the hoverlabel oh so pretty 
  doors_map.update_layout(
      autorange=False,
      hoverlabel=dict(
        bgcolor="#273B80",
        font_size=16,
        font_family="sans-serif"

        )
  )

  # Force Y Axis Range 
  doors_map.update_yaxes(range = [0,100])

  # Sad Face Because it doesn't seem to work 
doors_map.show()
