
import streamlit as st
generos = {

    'Hip Hop' : {

        'Hungria' : 'https://www.youtube.com/watch?v=ySCAq0EabOs&list=RDySCAq0EabOs&start_radio=1',
        'Tribo da periferia' : 'https://www.youtube.com/watch?v=sEkvmF1bGmw&list=RDsEkvmF1bGmw&start_radio=1',
        'Projota' : 'https://www.youtube.com/watch?v=SBs_pd1QQu8&list=RDSBs_pd1QQu8&start_radio=1',
        'SNJ' : 'https://www.youtube.com/watch?v=5lI-b9yRPTk&list=RD5lI-b9yRPTk&start_radio=1'
    },

    'Funk' : {

        'Mc Daleste' : 'https://www.youtube.com/watch?v=tfWA7sJKtqU&list=RDtfWA7sJKtqU&start_radio=1',
        'Mc Tití' : 'https://www.youtube.com/watch?v=51cIQrgw_HM&list=RD51cIQrgw_HM&start_radio=1',
        'Kaue Mc' : 'https://www.youtube.com/watch?v=Cu8-r-MGSHk&list=RDCu8-r-MGSHk&start_radio=1',
        'Mc Neguinho do Kaxeta' : 'https://www.youtube.com/watch?v=blLNQiCblHc&list=RDblLNQiCblHc&start_radio=1'

    },

    'Sertanejo' : {

        		'léo e raphael' : 'https://www.youtube.com/watch?v=9bibdQXOqyM&list=RD9bibdQXOqyM&start_radio=1',
	            'bruno e barreto' : 'https://www.youtube.com/watch?v=wF_Rn3US6hs&list=RDwF_Rn3US6hs&start_radio=1',
                'mano walter' : 'https://www.youtube.com/watch?v=htrlDVrF4vw&list=RDhtrlDVrF4vw&start_radio=1',
                'antony e gabriel' : 'https://www.youtube.com/watch?v=grTp4mbWNW4&list=RDgrTp4mbWNW4&start_radio=1'

     },

     'Pop' : {
         
         	'melim' : 'https://www.youtube.com/watch?v=gUpGTRR4Tt4&list=RDgUpGTRR4Tt4&start_radio=1',
            'melim 2' : 'https://www.youtube.com/watch?v=vaXCSYva2FM&list=RDvaXCSYva2FM&start_radio=1',
	        'anavitoria' : 'https://www.youtube.com/watch?v=-QdZ2VtOkhc&list=RD-QdZ2VtOkhc&start_radio=1',
	        'vitor kley' : 'https://www.youtube.com/watch?v=9Sk7RQtSl5g&list=RD9Sk7RQtSl5g&start_radio=1',
    	    'charlie brown jr' : 'https://www.youtube.com/watch?v=jp288zfsNTI&list=RDjp288zfsNTI&start_radio=1'

     },

     'Acústico' : {
         
         '1 Kilo' : 'https://www.youtube.com/watch?v=TQ5DUv_ZwRg&list=RDTQ5DUv_ZwRg&start_radio=1',
         'Delacruz' : 'https://www.youtube.com/watch?v=VQ2NPHdTb-0&list=RDVQ2NPHdTb-0&start_radio=1',
         'lourena' : 'https://www.youtube.com/watch?v=lxhqCcrnTv4&list=RDlxhqCcrnTv4&start_radio=1',
         'Sant' : 'https://www.youtube.com/watch?v=XGNb0oBSTtg&list=RDXGNb0oBSTtg&start_radio=1'



     }






}

#------------------------------------------------------------------sidebar

st.sidebar.title('Violas list')
st.sidebar.image('logo.png')

genero = st.sidebar.selectbox('Escolha um genero musical', generos.keys())
artista = st.sidebar.selectbox('Escolha um artista', generos[genero])








#------------------------------------------------------------------body

st.title(artista)
st.markdown('---')
video, sobre = st.tabs(['Vídeo', 'Sobre o Artista'])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista == 'Hungria':
        st.markdown(""" 
Gustavo da Hungria Neves (Ceilândia, 26 de maio de 1991)[1] é um rapper, cantor, compositor e empresário brasileiro.[3]

Hungria ficou conhecido nacionalmente pelo seu primeiro single, "Bens Materiais", mas só alcançou sucesso fora do território nacional com as músicas "Dubai", "Lembranças", "Coração de Aço", "Beijo Com Trap", "Temporal”, "Chovendo Inimigo", "O Playboy Rodou", "Não Troco", "Quebra-Cabeça", "Um Pedido", "Insônia" e "Amor e Fé", com cada uma delas ultrapassando a marca de 100 milhões de acessos na Internet. Atualmente, um dos seus maiores hits "Lembranças", possui mais de 300 milhões de acessos no YouTube e tornou-se trilha sonora de Malhação: Viva a Diferença. Hungria lançou três álbuns de estúdio, três EPs, possui um certificado de disco de ouro em Meu Carona,[4] um certificado de single de platina em "Insônia 2",[5] um certificado de ouro em “Amor e Fé”, um certificado de platina 2x em “Outro Patamar” e “Temporal”, um certificado de diamante em “Cruzeiro da Revoada”, um certificado de ouro em “Cama de Casal”, “Quem é o Boss?”, e “Atmosfera”, um certificado de platina em “Coração de Carro Forte”,[5] e um certificado de single de platina triplo em "Eu Vou Te Buscar (Cha La La La La)", com Gusttavo Lima.[6]

""")
        
    elif artista == 'Tribo da periferia':
        st.markdown("""
Tribo da Periferia é uma dupla de rap formada em Brasília, Distrito Federal, atualmente integrada por Look e DuckJay.[1][2] Tribo da Periferia é conhecida nacionalmente pelos singles "Insônia" e "Insônia 2" com Hungria Hip Hop, "Imprevisível", "Nosso Plano", e "Conspiração" com Marília Mendonça.[3][4] Com oito álbuns lançados, dois discos de platina,[5] e uma vitória em premiação musical,[1] a dupla, por década é considerada uma das maiores bandas de rap do Brasil[6], sendo também considerados pioneiros do subgênero trap

""")

    elif artista == 'Projota':
        st.markdown("""
José Tiago Sabino Pereira (São Paulo, 11 de abril de 1986), mais conhecido pelo nome artístico Projota, é um rapper, compositor e ator brasileiro.

Em 2014, lançou seu álbum de estreia, Foco, Força e Fé.[2] Em 2016, foi lançado seu primeiro DVD, 3Fs ao Vivo, que recebeu certificação de disco de ouro pelas 40 mil cópias vendidas.[3] Seu segundo álbum de estúdio foi lançado em 2017 e recebeu certificado de disco de ouro pelas 40 mil cópias vendidas.[4] Em 2019, lançou o álbum Tributo dos Sonhadores, que recebeu certificado de disco de ouro pelas 40 mil cópias vendidas

""")

    elif artista == 'SNJ':
        st.markdown("""
Ao longo de sua trajetória, o SNJ passou por diversas mudanças em sua formação. A primeira selas, em 1996, contava com DJ Alex, Boca, Pelé, WF e Sombra. No entanto, esta formação não se consolidou por questões pessoais e familiares.[3] No ano seguinte, o grupo se reestruturou com Sombra, DJ Alex e Cabeça. Embora tenha alcançado maior repercussão que a anterior, a formação ainda buscava estabilidade no cenário do rap brasileiro. Com a saída de DJ Alex, o grupo contou com a colaboração dos DJs Kill e Favela em suas apresentações.[3]

""")

    elif artista == 'Mc Daleste':
        st.markdown("""
Daniel nasceu no bairro Penha, localizado na Zona Leste de São Paulo, e foi criado por uma família de baixa renda, sendo o mais novo de três irmãos. Teve uma infância sofrida e conturbada pelo falecimento precoce de sua mãe, que ocorreu devido à complicação de um derrame. Ela sempre o incentivou a seguir uma carreira artística, com o intuito de ajudar financeiramente a sua família.[4] Na sua música "Minha História", o cantor revelou que até completar treze anos de idade, residia em uma casa de madeira que não possuía banheiro e que em diversas ocasiões passou fome por não ter condições de se alimentar.[5] Daniel só frequentou o colégio até a oitava série e era um aluno indisciplinado, momento em que conheceu a sua esposa Érica Teixeira, com a qual foi casado por cinco anos, até a data de seu falecimento.[6]
                    
                    """)

    elif artista == 'Mc Tití':
        st.markdown("""
DJ Tití Oficial é um artista brasileiro de São João de Meriti (RJ), conhecido no funk carioca por suas batidas animadas e letras ousadas. Suas músicas, como No Pique BBB, Tu Já Sabe o Macete e Toma La Dentro, têm forte presença em plataformas digitais e são marcadas por parcerias com MCs e DJs da cena. Com estilo voltado para o baile e influências latinas, ele aposta em sons dançantes que conquistam o público das festas e mantém presença ativa em redes sociais e no YouTube.

""")

    elif artista == 'Kaue Mc':
        st.markdown("""

MC Kaue é um cantor brasileiro de funk, com músicas recentes como “Pra Subir na KTM 2” em parceria com Oliverjdlz. Ele aposta em batidas diretas e letras voltadas para o cotidiano das ruas e do baile. Suas produções têm presença em plataformas digitais como YouTube, Spotify e Apple Music, onde conquista espaço com singles de curta duração e estilo dançante

""")

    elif artista == 'Mc Neguinho do Kaxeta':
        st.markdown("""
MC Neguinho do Kaxeta, nome artístico de Júlio César Ferreira, é um dos artistas mais emblemáticos do funk paulista. Natural de São Vicente, no litoral de São Paulo, ele iniciou sua carreira no final dos anos 1990, destacando-se como um dos pioneiros do funk na Baixada Santista. Seu nome artístico é uma homenagem à favela Kaxeta, onde cresceu.

""")

    elif artista == 'léo e raphael':
        st.markdown("""


Leo & Raphael são uma dupla brasileira de sertanejo, conhecida por músicas românticas e de sofrência, típicas do gênero. Eles se destacam pelo estilo que mistura moda de viola com arranjos modernos, conquistando público em shows e redes sociais. Suas canções falam de amor, relacionamentos e histórias do cotidiano, mantendo presença em plataformas como Spotify, YouTube e Instagram

""")

    elif artista == 'bruno e barreto':
        st.markdown("""

Bruno & Barreto são uma dupla brasileira de sertanejo, com repertório focado em músicas românticas e de festa. Eles combinam moda de viola tradicional com arranjos modernos, atingindo público tanto em shows ao vivo quanto em plataformas digitais como YouTube, Spotify e Instagram. Suas letras geralmente abordam amor, relacionamentos e temas do cotidiano sertanejo.

""")

    elif artista == 'mano walter':
        st.markdown("""
Mano Walter é um cantor brasileiro de sertanejo, natural de Fortaleza (CE), conhecido por seu estilo de sofrência e músicas românticas. Ficou famoso com hits como Coração de Papel e Meu Coração Deu PT, conquistando grande presença em radios, YouTube, Spotify e shows pelo Brasil. Ele combina moda de viola com arranjos modernos, sendo referência no sertanejo contemporâneo e na música para festas e baladas sertanejas.

""")

    elif artista == 'antony e gabriel':
        st.markdown("""



Antony & Gabriel são uma dupla brasileira de sertanejo, conhecida por músicas românticas e de sofrência. Com repertório que mistura moda de viola e arranjos modernos, eles conquistam público em shows, YouTube e plataformas como Spotify, abordando temas de amor, relacionamentos e cotidiano sertanejo

""")

    elif artista == 'melim':
        st.markdown("""
Melim foi um trio musical brasileiro formado pelos irmãos Rodrigo de Paula Pontes Melim, Gabriela de Paula Pontes Melim e Diogo de Paula Pontes Melim.[2] Interessados por música desde a infância, os irmãos tinham projetos separados antes de se juntarem para formar a banda. Em 2016, participaram da terceira temporada do reality show musical Superstar, da TV Globo, e terminaram a competição como semifinalistas. No ano seguinte, eles assinaram um contrato com a Universal Music e lançaram o extended play (EP) Melim, que inclui o single "Meu Abrigo". Em 2018, o trio lançou seu álbum de estreia homônimo. Em 2019 a banda participou da oitava edição do Rock in Rio, no palco sunset e em maio de 2020 lançaram a primeira parte de seu segundo álbum de estúdio intitulado Eu Feat. Você.
""")

    elif artista == 'anavitoria': 
        st.markdown("""
Anavitória é uma dupla de música folk-pop brasileira formado em 2014 em Araguaína, Tocantins pelas cantoras Ana Caetano e Vitória Falcão.[3]

Alcançaram o sucesso na música popular brasileira com o lançamento de seu primeiro álbum de estúdio homônimo, Anavitória em 2016, aclamado pela critica e que recebeu a certificação de disco de diamante, vendendo mais de 300 mil cópias. Além disso, o álbum recebeu duas indicações ao Grammy Latino, vencendo em Melhor Canção em Língua Portuguesa por "Trevo (Tu)".[5][6] Lançaram o longa-metragem de ficção autobiográfico Ana e Vitória (2018) e o segundo álbum de estúdio O Tempo É Agora (2018), vencedor do Grammy Latino de Melhor Álbum Pop Contemporâneo em Língua Portuguesa.[7][8][9] Lançaram em 2019 um álbum composto por regravações de canções do cantor Nando Reis e foi produzido por Tó Brandileone e Ana Caetano, N .[10] O duo lançou em 2021, o terceiro álbum de estúdio, Cor, novamente vencedor do Grammy Latino de Melhor Álbum Pop Contemporâneo em Língua Portuguesa.
""")

    elif artista == 'vitor kley':
        st.markdown("""
Vitor Barbiero Kley (Porto Alegre, 18 de agosto de 1994) é um cantor, musicista e compositor brasileiro.[3] Em 2009, lançou seu álbum de estreia, Eclipse Solar. Seu segundo álbum, Luz a Brilhar, foi lançado em 2012 e teve a produção do cantor Armandinho. Em 2015, assinou com a gravadora Midas Music, lançando seu primeiro EP, o homônimo Vitor Kley, em 2016. Ganhou notoriedade nacional após o lançamento da canção "O Sol", que lhe rendeu uma certificação de disco de diamante duplo no Brasil e disco de platina em Portugal, se tornando uma das canções mais ouvidas do país.
""")

    elif artista == 'charlie brown jr':
        st.markdown("""
Charlie Brown Jr. foi uma banda de rock brasileira formada em Santos, em 1992, tendo em sua formação original o vocalista Chorão, o baixista Champignon, os guitarristas Marcão Britto e Thiago Castanho, além do baterista Renato Pelado.[5] Sua discografia contabiliza dez álbuns de estúdio lançados, três álbuns ao vivo e sete DVDs. [6] Excetuando Chorão, todos os membros da banda são naturais de Santos, uma vez que o vocalista é natural de São Paulo.[7]

A banda encerrou suas atividades em 2013, quando na madrugada do dia 6 de março daquele ano, Chorão foi encontrado morto em seu apartamento em São Paulo, devido a uma overdose de cocaína. Posteriormente a isso os demais membros do Charlie Brown Jr. se reuniram em projetos distintos para preservar a memória de Chorão e manter o seu legado vivo. Em 2013, logo após à morte de Chorão, os membros remanescentes chegaram a mudar o nome da banda para A Banca, com Champignon assumindo os vocais.[8][9] Porém o grupo encerrou as atividades em setembro do mesmo ano, após Champignon cometer suicídio em sua casa, também em São Paulo, na madrugada do dia 9 daquele mês.[10]
""")
    
    elif artista == '1 Kilo': 
        st.markdown("""
1Kilo é uma gravadora de rap e selo de música independente formada no Rio de Janeiro em 2016.[1] Soma mais de 2 Bilhões de acessos nas principais plataformas digitais. É formada por DoisP, Junior Lord, Mozart Mz, Pelé Milflows, RastaBeats (Produtor musical, Instrumental), Dj Grego (Produtor musical, Beatmaker)
""")
         
    elif artista == 'Delacruz': 
        st.markdown("""
Delacruz é um artista do Rio de Janeiro que ganhou destaque misturando rap, samba, MPB e R&B, criando uma identidade única na cena musical brasileira. Ele ficou conhecido principalmente após participar do projeto Poesia Acústica, onde sua voz marcante e suas letras sensíveis chamaram atenção. Suas músicas falam de amor, relacionamentos, vivências de rua e reflexões sobre a vida, sempre com uma pegada poética. Além disso, ele é reconhecido pelo timbre suave, que combina bem tanto em faixas mais românticas quanto nas de crítica social.
""")

    elif artista == 'lourena': 
        st.markdown("""
Lourena é uma cantora e compositora que vem se destacando na cena do rap e do R&B brasileiro. Com voz suave e letras marcantes, ela mistura romantismo, vivências pessoais e poesia em suas músicas. Ganhou mais visibilidade participando do projeto Poesia Acústica, onde sua presença e estilo conquistaram o público. Seu trabalho tem como marca a delicadeza, o sentimento e a originalidade, colocando Lourena como uma das vozes femininas mais promissoras da nova geração.
""")

    elif artista == 'Sant': 
        st.markdown("""
Sant é um rapper carioca conhecido pelas rimas afiadas e pela versatilidade. Ele ganhou destaque no projeto Poesia Acústica e se firmou na cena com letras que falam de amor, vivência urbana e superação. Sua voz marcante e o estilo autêntico fazem dele um dos nomes mais promissores do rap nacional.
""")



    