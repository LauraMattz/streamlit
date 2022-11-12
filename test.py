import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
from tabulate import tabulate
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)
import pandas as pd

st.title('Mapa de Redes')
  
xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

file = "teste.xlsx"
G = nx.Graph()

total_names = []
names= []

book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(0)
search_words = (option)

for row in range(sheet.nrows):
    data= sheet.row_slice(row)
    person1 = data[0].value
    person2 = data[1].value
    names.append((person1, person2))
    total_names.append(person1)
    total_names.append(person2)
    
node_sizes = [(total_names.count(node)*100) for node in G.nodes()]


G.add_edges_from(names)

pos = nx.circular_layout(G, scale=5)

nx.draw(G, with_labels=True)
options = {"node_size": 1200, "node_color": "r"}

excel_data_df = pd.read_excel('teste.xlsx', sheet_name='DOAR')
def filter_dataframe(excel_data_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Add filters")

    if not modify:
        return df
df = excel_data_df.copy()

# Try to convert datetimes into a standard format (datetime, no timezone)
for col in df.columns:
    if is_object_dtype(df[col]):
    	try:
    	    df[col] = pd.to_datetime(df[col])
    	except Exception:
    	    pass

    if is_datetime64_any_dtype(df[col]):
        df[col] = df[col].dt.tz_localize(None)
        
modification_container = st.container()
with modification_container:
    to_filter_columns = st.multiselect("Escokha a Categoria", df.columns)
    
for column in to_filter_columns:
    left, right = st.columns((1, 20))
    left.write("↳")
# Treat columns with < 10 unique values as categorical
if is_categorical_dtype(df[column]) or df[column].nunique() < 10:
    user_cat_input = right.multiselect(
        f"Relacionados a {column}",
        df[column].unique(),
        default=list(df[column].unique()),
    )
    df = df[df[column].isin(user_cat_input)]
st.write('Você escolheu:', filter_dataframe(df))
st.dataframe(filter_dataframe(df))


plt.show()
st.table(df)

st.pyplot(plt)
