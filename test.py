import pandas as pd
from pandasql import sqldf

doar= pd.read_excel("teste.xlsx", sheet_name="DOAR")
receber= pd.read_excel("teste.xlsx", sheet_name="RECEBER")
pessoas= pd.read_excel("teste.xlsx", sheet_name="PESSOAS")

q="""
select nome, doar,receber from doar
left join pessoas on doar.ID_QUEM = pessoas.ID
left join receber on receber.ID_QUEM = pessoas.ID
where doar = 'FUTEBOL'
"""

print(sqldf(q))
