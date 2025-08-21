import streamlit as st 
import streamlit as st 
import pandas as pd 
import seaborn as sns 
import plotly.express as px


st.title('explore the insights and visuals')


df=sns.load_dataset('titanic')



#filters
st.sidebar.subheader('filter option')

gender=st.sidebar.multiselect('Gender',
                              options=df['sex'].unique(),
                              default=df['sex'].unique())


pclass=st.sidebar.multiselect('passenger class',
                              options=df['pclass'].unique(),
                              default=df['pclass'].unique())

min_age,max_age=st.sidebar.slider('age',
                      min_value=int(df['age'].min()),
                      max_value=int(df['age'].max()),
                      value=(int(df['age'].min()),int(df['age'].max())))


#apply filters
filtered_df=df[
    (df['sex'].isin(gender))& #this line check if the gender is in the selected options
    (df['pclass'].isin(pclass))&
    (df['age']>=min_age)&
    (df['age']<=max_age)
]

st.dataframe(filtered_df)


fig=px.histogram(filtered_df,x='age',color='class',barmode='overlay',title='age distribution by class')
st.plotly_chart(fig)

fig2 = px.pie(filtered_df, names='sex', title='sex distribution' ,
              hole=0.2)
st.plotly_chart(fig2)

fig=px.bar(filtered_df,x='class',y='fare',color='sex',title='average fare by class and sex',barmode='group')
st.plotly_chart(fig)

fig=px.scatter(filtered_df,x='age',y='fare',color='class',size='survived',title='fare vs age by class')
st.plotly_chart(fig)