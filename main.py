import os
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd

#set page configuration
st.set_page_config(page_title= "Data Visualiser",
                   layout="centered",
                   page_icon="📊")

#Title
st.title("📊 Data Visualiser - Web App")

#getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))


folder_path = f"{working_dir}/data"

#List the files present in data folder
files_list = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

#Dropdown for all the files
selected_file = st.selectbox("Select a file", files_list, index=None)

if selected_file:


    # get the complete path of the selected files
    file_path = os.path.join(folder_path, selected_file)

    # reading the csv file as a pandas dataframe
    df = pd.read_csv(file_path)

    col1, col2 = st.columns(2)

    columns = df.columns.tolist()

    with col1 :
        st.write ("")
        st.write (df.head())
    # user selection of df columns
    with col2 :

        x_axis = st.selectbox("Select the X-axis", options=columns + ["None"], index = None)
        y_axis = st.selectbox("Select the Y-axis", options=columns + ["None"], index=None)
        plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', "Distribution Plot","Count Plot"]
        selected_plot = st.selectbox("Select a plot", options=plot_list + ["None"], index=None)

        # st.write(x_axis)
        # st.write(y_axis)
        # st.write(selected_plot)


    #button to generate plots
    if st.button ("Generate Plot"):

        fig, ax = plt.subplots(figsize = (6,4))

        if selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y = df[y_axis], ax = ax)
        elif selected_plot == "Bar Chart":
            sns.barplot(x=df[x_axis], y = df[y_axis], ax = ax)
        elif selected_plot == "Scatter Plot":
            sns.scatterplot(x=df[x_axis], y = df[y_axis], ax = ax)
        elif selected_plot == "Line Plot":
            sns.lineplot(x=df[x_axis], y = df[y_axis], ax = ax)
        elif selected_plot == "Distribution Plot":
            sns.histplot(df[x_axis], kde = True, ax = ax)

        elif selected_plot == "Count Plot":
            sns.countplot(x=df[x_axis], ax = ax)

        # Adjust Label Sizes
        ax.tick_params (axis ='x', labelsize= 10)
        ax.tick_params (axis ='y', labelsize= 10)

        #title axes labels
        plt.title( f"{selected_plot} of {y_axis} vs {x_axis}", fontsize = 12 )
        plt.xlabel (x_axis, fontsize= 10)
        plt.xlabel (y_axis, fontsize= 10)

        st.pyplot (fig)




