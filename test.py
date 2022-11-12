import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import xlrd
from tabulate import tabulate


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

import streamlit as st
import pandas as pd

#define data
d = {'id': ['a', 'b', 'c'], 'data': [3, 4,6]}
df = pd.DataFrame(data=d)


#create sidebar input
with st.sidebar.form("my_form"):
    a = st.slider('sidebar for testing', 5, 10, 9)
    calculate = st.form_submit_button('Calculate')

# Initialization
if 'button_pressed' not in st.session_state:
    st.session_state['button_pressed'] = False

# Changes if calculated button is pressed  
if calculate:
    st.session_state['button_pressed'] = True

# Conditional on session_state instead
if st.session_state['button_pressed']:
    df['result'] = df['data'] + a
    st.write(df)
    #no issues up to this point. When I move the slider in 10 the output in 16 stays on the web page

    ########debug############
    # I am trying to select an 'id' from the dropdown and use that to filter df, but when I select a value from the dropdown,
    # the script runs again and the output disappears
    filter = st.selectbox('filter data', df['id'].unique())
    st.write(df[df['id'] == filter])
