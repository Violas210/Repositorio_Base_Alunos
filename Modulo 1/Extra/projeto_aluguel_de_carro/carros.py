import streamlit as st 



# -------------------------------------------------------------- Sidebar
st.sidebar.image('logo.png')
st.sidebar.title('Doki')
st.sidebar.title('Aluguel de Carros')

carros = ['eclipse','mt09','Honda_civic','Fusca']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)





# -------------------------------------------------------------- Principal
st.title('Titans - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos km você rodou com o {opcao}?')

if opcao == 'eclipse':
    diaria = 1000

elif opcao == 'mt09':
    diaria = 650

elif opcao == 'Honda_civic':
    diaria = 700 

elif opcao == 'Fusca':
    diaria = 450


if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias*diaria
    total_km = km*0.15
    aluguel = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} dias e rodou por {km}km, então o total a pagar é de {aluguel}R$.')              