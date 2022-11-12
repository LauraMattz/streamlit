import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
from tabulate import tabulate
import pandas as pd

st.title('Mapa de Redes')


xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

file = "teste.xlsx"
G = nx.Graph()

total_names = []
names= []

option = st.selectbox(
    'Qual tema você gostaria de verificar?',
    ('FORRÓ', 'YOUTUBE','FUTEBOL','ESTUDAR FORA','MÚSICA'))

st.write('Você escolheu:', option)


book = xlrd.open_workbook(file)
sheet = book.sheet_by_index(0)

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


plt.show()
st.table(names)

st.pyplot(plt)



import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.title("Auto Filter Dataframes in Streamlit")
st.write(
    """This app accomodates the blog [here](<https://blog.streamlit.io/auto-generate-a-dataframe-filtering-ui-in-streamlit-with-filter_dataframe/>)
    and walks you through one example of how the Streamlit
    Data Science Team builds add-on functions to Streamlit.
    """
)

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
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

data_url = "https://github.com/LauraMattz/streamlit/blob/main/teste.xlsx"

df = pd.read_csv(data_url)
st.dataframe(filter_dataframe(df))
