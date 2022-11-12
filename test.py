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

option = st.selectbox(
    'Qual tema você gostaria de verificar?',
    ('FORRÓ', 'YOUTUBE','FUTEBOL','ESTUDAR FORA','MÚSICA'))

st.write('Você escolheu:', option)


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
      modify = st.checkbox("Add filters")

if not modify:
return excel_data_df

df = excel_data_df.copy()


plt.show()
st.table(names)
st.table(excel_data_df)

st.pyplot(plt)
