import streamlit as st

#-----------------------------------------sidebar
st.sidebar.image('movida_logo.png')
st.sidebar.title('movida - aluguel de carros')
st.sidebar.write('seja bem vindo(a)')

carros = ['BMW', 'MUSTANG', 'HB20', 'FUSCA', 'CIVIC']
carro = st.sidebar.selectbox('selecione o carro alugado', carros)
valor_do_dia = 0 
    
if carro == 'BMW':
    valor_do_dia = 500

elif carro == 'MUSTANG':
    valor_do_dia = 2000     
    
elif carro == 'HB20':
    valor_do_dia = 130

elif carro == 'FUSCA':
    valor_do_dia = 250

elif carro == 'CIVIC':
    valor_do_dia = 180





#-----------------------------------------principal
st.title('movida - aluguel de carros')
st.write('seja bem vindo(a)')
st.write(f'voce alugou {carro}')
st.image(f'{carro}.png')

dias = st.text_input('informe a quantidade de dias')
km = st.text_input('informe a quantidade de kilometrosrodados')

if  st.button('calcular'):
    dias = int(dias)
    km = float(km)

    valor_dias = dias * valor_do_dia
    valor_km = km*0.15
    total = valor_dias+valor_km

st.warning(f'voce rodou {km}km com o {carro} por {dias} dias. o valor do aluguel sera R${total}')