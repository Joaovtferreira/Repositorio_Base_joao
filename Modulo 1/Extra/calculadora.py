import streamlit as st 

st.sidebar.title('calculadora')
st.sidebar.write('seja bem vindo(a)')

calculo =  ['adicao', 'subtracao', 'multiplicacao', 'divisao']
conta = st.sidebar.selectbox('selecione o tipo de calculo', calculo)

numero1 = st.text_input('escolha o primeiro numero:')
numero2 = st.text_input('escolha o segundo numero:')

numero1 = float(numero1)
numero2 = float(numero2)

if conta == 'adicao':
    resultado = numero1 + numero2
    print()
elif conta == 'subtracao':
    resultado = numero1 - numero2
    print()
elif conta == 'multiplicacao':
    resultado = numero1 * numero2
    print()
elif conta == 'divisao':
    resultado = numero1 / numero2

st.title('calculadora-automatica')
st.write('seja bem vindo(a)')
st.write(f'escolha uma formula de calculo {calculo}')

numero1 = st.text_input('informe a quantidade de dias')
km = st.text_input('informe a quantidade de kilometrosrodados')

if  st.button('calcular'):
    dias = int(dias)
    km = float(km)

    valor_dias = dias * valor_do_dia
    valor_km = km*0.15
    total = valor_dias+valor_km

st.warning(f'voce rodou {km}km com o {carro} por {dias} dias. o valor do aluguel sera R${total}')