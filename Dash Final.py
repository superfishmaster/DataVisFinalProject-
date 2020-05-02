#!/usr/bin/env python
# coding: utf-8

# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://superfishmaster.github.io/DataVisFinalProject-/External.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
# Use a csv dataset from a repository in your GitHub account. Use the Raw URL to expose the data to the Python dataframe
df = pd.read_csv('https://raw.githubusercontent.com/superfishmaster/DataVisFinalProject-/master/time_series_covid19_confirmed_US.csv')
df2= pd.read_csv('https://raw.githubusercontent.com/superfishmaster/DataVisFinalProject-/master/time_series_covid19_confirmed_global.csv')
df3= pd.read_csv('https://raw.githubusercontent.com/superfishmaster/DataVisFinalProject-/master/time_series_covid19_deaths_US.csv')
df4= pd.read_csv('https://raw.githubusercontent.com/superfishmaster/DataVisFinalProject-/master/time_series_covid19_deaths_global.csv')
#df_china_confirmed
df_china_confirmed=df2[df2['Country/Region']=="China"]
y1=df_china_confirmed.iloc[0:33,4:101].sum()
x1=df_china_confirmed.columns[4:101]
fig_confirmed=px.scatter(df2,x1,y1)
#df_china_death
df_china_death=df4[df4['Country/Region']=="China"]
y2=df_china_death.iloc[0:33,4:101].sum()
x2=df_china_death.columns[4:101]
fig_death=px.scatter(df4,x2,y2)


# In[3]:


# Custom function used to generate a data table from a dataframe
def generate_table(dataframe, max_rows=16):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


# In[11]:


app.layout=html.Div([
    # Add your HTML tags to the content - notice a comma is added between HTML elements
    html.H1('Data Visualization Story Telling'),
    html.Div([
        html.P('The Covid-19 in 2020 ...'),
    ]),
     # Begin of DIV surrounding both Tables
    html.Div([   
        # Begin of First Table
    html.Table(style={'width':'100%'},
              #Begin of Table children
              children=[
                  #######################################
                  #Begin of First Tr
                  html.Tr(
                  #Begin Tr Children
                  children=[
                      #Begin Th
                      html.Th(style={'width':'50%'},
                             #Begin Th Children
                          children=[
                             html.H3('China Confirmed over Time')
                      # End of Th children
                  ]
                  # End of Th - Notice a comma is placed here to separate the next Th
                  ),
                  #Begin of Th
                  html.Th(style={'width':'50%'},
                         #Begin of Th children
                         children=[
                             html.H3('China Death over Time')
                 #End of Th children            
                         ]
                         #End of Th
                         )
                  #End of Tr children
              ]
              # End of First Tr - Notice a comma is placed here to separate the next Tr
              ),
                  ##########################################################################
                  #Begin of Second Tr
                  html.Tr(
                  #Begin Tr Children
                  children=[
                      #Begin Td
                      html.Td(
                      # Begin Td Children
                          children=[
                              #Display bar grpah
                              dcc.Graph(
                           figure=fig_confirmed
                                  # End of Chart 1
                              )
                              # End of Td children  
                          ]
                          # End of Td - Notice a comma is placed here to separate the next Th
                      ),
                      #Being of Td
                      html.Td(
                      #Begin of Td children
                      children=[
                          #Display plot graph use data from dataframe df4
                          dcc.Graph(
                          figure=fig_death)
                          #End of Td Children
                      
                      ]
                      #End of Td
                      )
                      #End of Tr Children
                  ]
                     # End of Second Tr
                  )
                  #########################################################################    
                  #End of Table children
              ]
               #End of First Table -Notice a comma is placed here to separate the next Table 
              ),
      #########################################################################################  
          # Begin of Second Table
        html.Table(style={'width':'100%'},
                  children=[
                      ####################################################################
                      #Begin First Tr
                      html.Tr(
                      #Begin Tr children
                      children=[

                          #Begin of Th
                          html.Th(style={'width':'10%'},
                                 #Begin of Th children
                                  children=[
                                      #Nothing to display here, just a place holder in the column
                                      html.H2('')
                                      #End of Th children
                                  ]
                                  #End of Th- Notice a comma is placed here to separate the next Th
                                 ),
                          #Begin of Th
                          html.Th(style={'width':'50%'},
                                 #Begin of Th children
                                  children=[
                                      html.H3('Top 15 us states')
                                        #End fo Th children   
                                 ]
                                  #End of Th
                                 )
                          #End of Tr children
                      ]
                          #End of First Tr
                      ),
                      ##################################################
                      #Begin of Second Tr
                      html.Tr(
                      #Begin Tr children
                          children=[
                             
                           
                              #Begin of Td
                              html.Td(style={'border':'1px solid black'},
                                     #Begin of Td children
                                     children=[
                                         #Display a large and important measure
                                         html.H2('Domestic'),
                                         html.H2('Recover:'),
                                         html.H2('92%')
                                         #End of Td children
                                     ]
                                      #End of Td
                                     ),
                              #Begin of Td
                              html.Td(
                              #Begin of Td children
                              children= [
                              #Execute custom generate_table frunction and display data
                                  #Use data from dataframe df2
                                  generate_table(df2)
                                  #End of Td children
                              ]
                                  #End of Td
                              )
                              #End of Tr children
                          ]
                          #End of Second Tr
                      )
                      ####################################################
                      #End of Table Children
                  ]
                  ############################################################
                  #End of Second Table -Notice a comma is placed here to seprate the next Content
                  ),
        #End of DIV surrounding both Tables
    ]),
   #End of all content DIV  
])




# In[12]:


if __name__ == '__main__':
    # Set debug to False. Some configurations are not setup for Debug
    app.run_server(debug=False)


# In[ ]:




