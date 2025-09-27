import streamlit as st

st.set_page_config(page_title="Gerador de Currículo", layout="centered")
# Lê a "página" atual pela URL (padrão: "formulario")

if 'dados_curriculo' not in st.session_state:
    st.session_state["dados_curriculo"] = {
        "nome": 'nome',
        "idade": 0,
        "profissao": 'profissao',
        "sobre": 'sobre',
        "experiencias": 'experiencias',
        "formacoes": 'formacoes',
        "habilidades": 'habilidades',
        "idiomas": 'idiomas',
        "telefone": 'telefone',
        "email": 'email',
        "redes": 'redes',
        "cor_sidebar": 'cor_sidebar',
        "cor_texto": 'cor_texto',
        "fonte": 'fonte',
        "imagem": 'imagem'
    }

if 'data' not in st.session_state:
    st.session_state.data = {'nome': 'Milton Keynes Say', 'idade': 30,
                             'profissao': 'Estudante de Economia', 'sobre': """Olá! Sou Milton Keynes Say, tenho 23 anos e sou estudante do quarto ano de Economia.  
Procuro oportunidades de actuação onde eu possa aprender e crescer como profissional.""",
                             'experiencias': """Ajuda e pão — Voluntariado na Comunidade Alegre  \n2018–2022
Auxiliei em atividades como distribuição de alimentos, aulas de reforço escolar e atividades recreativas para as crianças.

Coca e Cola — Gestor de Recursos Humanos  \n2017–2018
Gestão de equipes e implementação de estratégias de recrutamento, seleção e treinamento de pessoal.  
Gestão de conflitos e resolução de problemas.

GHT e Parceiros — Auxiliar Administrativo  \n2015–2017
Desenvolvi habilidades em organização, atendimento ao cliente e gestão de documentos.  
Atuei de forma proativa nos trabalhos em equipe.""",
                             'formacao': """Economia
2019–2023 
Universidade Saber
Administração
2012–2017
Instituto S.A.""",
                             'habilidade': """Empatia
Boa comunicação
Organização exemplar
Atividades em grupo
Proatividade""",
                             'idioma': """Inglês: Fluente
Espanhol: Intermediário
""",
                             'cor_sidebar': '#F0F0F0',
                             'cor_texto': '#000000',
                             'contacto':'+285',
                             'email': '@gmail.com',
                             'redes': '@meunome_redesocial',
                             'imagem':''
                        }

formu = st.session_state.data

if 'lis' not in st.session_state:
    st.session_state.lis = [0]

op = st.selectbox('', ['Formulário', 'Curriculum', 'Sobre'])
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True



if op == 'Formulário':
    st.title("🧾 Formulário do Currículo")
    with st.form("formulario_curriculo"):
        nome = st.text_input("Nome completo", value=formu['nome'], )
        st.session_state.data['nome'] = nome
        idade = st.number_input("Idade (opcional)", min_value=0, max_value=120, value=formu['idade'])
        st.session_state.data['idade'] = idade
        profissao = st.text_input("Profissão ou área", placeholder="Estudante de Economia",
                                  value=formu['profissao'])
        st.session_state.data['profissao'] = profissao
        sobre = st.text_area("Sobre você", value=formu['sobre'], height=250)
        st.session_state.data['sobre'] = sobre
        st.markdown("### 💼 Experiência Profissional")
        experiencias = st.text_area("Experiências (separe cada experiência com uma linha em branco)", value=formu['experiencias']
        , height=400)
        st.session_state.data['experiencias'] = experiencias

        st.markdown("### 🎓 Formação")
        formacoes = st.text_area("Formações (uma por linha)", value=formu['formacao'], height=250)
        st.session_state.data['formacao'] = formacoes

        st.markdown("### 💡 Habilidades")
        habilidades = st.text_area("Habilidades (uma por linha)", value=formu['habilidade']
        , height=250)
        st.session_state.data['habilidade'] = habilidades

        st.markdown("### 🌍 Idiomas")
        idiomas = st.text_area("Habilidades (uma por linha)", value=formu['idioma']
        , height=200)
        st.session_state.data['idioma'] = idiomas

        st.sidebar.markdown("### 🖼️ Foto de Perfil")
        imagem = st.sidebar.file_uploader("Foto de perfil", type=["jpg", "jpeg", "png"])
        if imagem:
            st.session_state.data['imagem'] = imagem
        else:
            imagem = st.session_state.data['imagem']
            st.sidebar.image("imagem, use_column_width=True)
        st.sidebar.markdown("### 📞 Contacto")
        telefone = st.sidebar.text_input("Telefone", placeholder="+258 __ ___ ____", value=formu['contacto'])
        st.session_state.data['contacto'] = telefone
        email = st.sidebar.text_input("E-mail", placeholder="email@profissional.co.mz", value=formu['email'])
        st.session_state.data['email'] = email
        redes = st.sidebar.text_input("Rede social", placeholder="@nome_redesocial", value=formu['redes'])
        st.session_state.data['redes'] = redes

        st.sidebar.markdown("### 🎨 Personalização")
        cor_sidebar = st.sidebar.color_picker("Cor da barra lateral", f"{formu['cor_sidebar']}")
        st.session_state.data['cor_sidebar'] = cor_sidebar
        cor_texto = st.sidebar.color_picker("Cor do texto", f"{formu['cor_texto']}")
        st.session_state.data['cor_texto'] = cor_texto
        fontes = [
            # --- Fontes padrão do sistema ---
            "Sans-serif", "Serif", "Monospace", "Arial", "Georgia", "Verdana", "Tahoma", "Courier New",
            "Times New Roman",

            # --- Google Fonts (precisam ser importadas) ---
            "Poppins", "Roboto", "Lato", "Open Sans", "Montserrat", "Raleway", "Merriweather",
            "Oswald", "Playfair Display", "Nunito", "Inter", "Quicksand", "Ubuntu", "Fira Sans",
            "Inconsolata", "Cabin", "Source Sans Pro"
        ]
        fonte = st.sidebar.selectbox("Fonte", sorted(fontes), index=st.session_state.lis[::-1][0])
        if sorted(fontes).index(fonte) != st.session_state.lis[::-1][0]:
            st.session_state.lis.append(sorted(fontes).index(fonte))
            st.rerun()

        st.markdown(f"""
            <link href="https://fonts.googleapis.com/css2?family={fonte.replace(" ", "+")}:wght@300;400;600&display=swap" rel="stylesheet">
        """, unsafe_allow_html=True)

        # --- Aplica o CSS personalizado ---
        st.markdown(f"""
            <style>
                /* Sidebar */
                section[data-testid="stSidebar"] > div {{
                    background-color: {cor_sidebar} !important;
                    padding-left: 25px;
                    padding-right: 20px;
                    font-family: '{fonte}', sans-serif !important;
                }}

                /* Texto principal */
                html, body, [class*="css"], .main-text * {{
                    color: {cor_texto} !important;
                    font-family: '{fonte}', sans-serif !important;
                }}

                /* Títulos */
                h1, h2, h3, h4, h5, h6 {{
                    font-family: '{fonte}', sans-serif !important;
                    font-weight: 600 !important;
                }}
                
                  html, body, [class*="css"], .main-text * {{
                    color: {cor_texto} !important;
                }}
                h1, h2, h3, h4, h5, h6 {{
                    color: {cor_texto} !important;
                }}
                p, span, div, label {{
                    color: {cor_texto} !important;
                }}

                /* Parágrafos */
                p, span, div {{
                    font-family: '{fonte}', sans-serif !important;
                    font-weight: 400 !important;
                }}
            </style>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <style>
                section[data-testid="stSidebar"] * {{
                    color: {cor_texto} !important;
                }}
            </style>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <style>
                /* Botões */
                button, .stButton > button {{
                    color: {cor_texto} !important;
                }}

                /* Inputs de texto */
                input, textarea, select {{
                    color: {cor_texto} !important;
                }}
            </style>
        """, unsafe_allow_html=True)

        submit = st.form_submit_button("🚀 Gerar Currículo")

        if submit:
            st.session_state["dados_curriculo"] = {
                "nome": nome,
                "idade": idade,
                "profissao": profissao,
                "sobre": sobre,
                "experiencias": experiencias,
                "formacoes": formacoes,
                "habilidades": habilidades,
                "idiomas": idiomas,
                "telefone": telefone,
                "email": email,
                "redes": redes,
                "cor_sidebar": cor_sidebar,
                "cor_texto": cor_texto,
                "fonte": fonte,
                "imagem": imagem
            }

            st.info('As informações do seu curriculum já estão disponíveis.')


try:
    if op == 'Curriculum':
        dados = st.session_state.get("dados_curriculo", None)
        # --- Aplica o CSS personalizado ---
        st.markdown(f"""
                    <style>
                        /* Sidebar */
                        section[data-testid="stSidebar"] > div {{
                            background-color: {dados['cor_sidebar']} !important;
                            padding-left: 25px;
                            padding-right: 20px;
                            font-family: '{dados['fonte']}', sans-serif !important;
                        }}
    
                        /* Texto principal */
                        html, body, [class*="css"], .main-text * {{
                            color: {dados['cor_texto']} !important;
                            font-family: '{dados['fonte']}', sans-serif !important;
                        }}
    
                        /* Títulos */
                        h1, h2, h3, h4, h5, h6 {{
                            font-family: '{dados['fonte']}', sans-serif !important;
                            font-weight: 600 !important;
                        }}
                        
                        html, body, [class*="css"], .main-text * {{
                        color: {dados['cor_texto']} !important;
                        }}
                        h1, h2, h3, h4, h5, h6 {{
                            color: {dados['cor_texto']} !important;
                        }}
                        p, span, div, label {{
                            color: {dados['cor_texto']} !important;
                        }}
                        
                        
    
                        /* Parágrafos */
                        p, span, div {{
                            font-family: '{dados['fonte']}', sans-serif !important;
                            font-weight: 400 !important;
                        }}
                    </style>
                """, unsafe_allow_html=True)
        st.markdown(f"""
                   <style>
                       section[data-testid="stSidebar"] * {{
                           color: {dados['cor_texto']} !important;
                       }}
                   </style>
               """, unsafe_allow_html=True)
        st.markdown(f"""
                   <style>
                       /* Botões */
                       button, .stButton > button {{
                           color: {dados['cor_texto']} !important;
                       }}
    
                       /* Inputs de texto */
                       input, textarea, select {{
                           color: {dados['cor_texto']} !important;
                       }}
                   </style>
               """, unsafe_allow_html=True)

        if not dados:
            st.warning("Nenhum dado encontrado. Volte e preencha o formulário.")
            st.stop()

        with st.sidebar:
            if dados['imagem']:
                st.image(dados['imagem'], width=200, caption=dados['nome'])
               
            st.header(" **Contacto**".upper())
            st.markdown(f"""
            - {dados['telefone']}
            - {dados['email']} 
            - {dados['redes']} 
            """)

            # st.subheader()
            st.markdown("## **Formação Profissional**".upper())
            for bloco in dados['formacoes'].split("\n\n"):
                partes = bloco.strip().split("\n")
                if len(partes) >= 1:
                    st.markdown(f"### {partes[0]}")
                    if len(partes) > 1:
                        st.markdown("<br>".join(partes[1:]), unsafe_allow_html=True)

                st.markdown("## **habilidades**".upper())
                for bloco in dados['habilidades'].split("\n\n"):
                    partes = bloco.strip().split("\n")
                    if len(partes) >= 1:
                        st.markdown(f"### {partes[0]}")
                        if len(partes) > 1:
                            st.markdown("<br>".join(partes[1:]), unsafe_allow_html=True)

                st.markdown("## **Idiomas**".upper())
                for bloco in dados['idiomas'].split("\n\n"):
                    partes = bloco.strip().split("\n")
                    if len(partes) >= 1:
                        st.markdown(f" {partes[0]}")
                        if len(partes) > 1:
                            st.markdown("<br>".join(partes[1:]), unsafe_allow_html=True)
                st.markdown(f"## Profissão".upper())
                st.markdown(f"{dados['profissao']}")

        # CURRÍCULO
        st.markdown("<div class='main-text'>", unsafe_allow_html=True)
        try:
            nome_lis = dados['nome'].split()
            st.markdown(f"""# {nome_lis[0]} \n # {nome_lis[::-1][0]}
        """)
        except:
            st.empty()

        st.markdown('---')
        st.markdown("##### Sobre Mim".upper())
        st.text(f"{dados['sobre']}")
        st.markdown('---')
        st.markdown("##### Experiência Profissional".upper())
        for bloco in dados['experiencias'].split("\n\n"):
            partes = bloco.strip().split("\n")
            if len(partes) >= 1:
                st.markdown(f"##### {partes[0]}")
                if len(partes) > 1:
                    st.markdown("<br>".join(partes[1:]), unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown('---')

        #st.info("🚀 **Mais de 200 profissionais já conquistaram o currículo dos sonhos!**")
        #st.info("💼 **Aumente suas chances de sucesso:** solicite seu currículo profissional por apenas **500 MZN**.")
        #st.info("✨ **Destaque-se no mercado** com um currículo que abre portas para novas oportunidades.")

        import smtplib
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.base import MIMEBase
        from email import encoders
        import os


        def enviar_email(remetente, senha, destinatario, assunto='', corpo='', arquivo=None):
            """
            Envia e-mail pelo Gmail com ou sem anexo.

            - remetente: e-mail de envio
            - senha: senha ou App Password do Gmail
            - destinatario: e-mail de destino
            - assunto: assunto do e-mail
            - corpo: corpo da mensagem (aceita texto simples e HTML)
            - arquivo: pode ser:
                1. UploadedFile (do st.file_uploader)
                2. Caminho de arquivo no disco
            """
            msg = MIMEMultipart("alternative")
            msg["From"] = remetente
            msg["To"] = destinatario
            msg["Subject"] = assunto

            # Corpo do email
            msg.attach(MIMEText(corpo, "plain"))
            msg.attach(MIMEText(corpo, "html"))

            # Anexo (se houver)
            if arquivo:
                try:
                    if hasattr(arquivo, "getbuffer"):
                        # Caso seja UploadedFile (Streamlit)
                        nome_arquivo = arquivo.name
                        file_data = arquivo.getbuffer()
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(file_data)
                    else:
                        # Caso seja caminho do arquivo
                        nome_arquivo = os.path.basename(arquivo)
                        with open(arquivo, "rb") as f:
                            file_data = f.read()
                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload(file_data)

                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename="{nome_arquivo}"'
                    )
                    msg.attach(part)

                except Exception as e:
                    st.error(f"❌ Erro ao anexar arquivo: {e}")
                    return False

            # Envio do e-mail
            try:
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(remetente, senha)
                    server.send_message(msg)
                return True
            except Exception as e:
                st.error(f"❌ Erro ao enviar e-mail: {e}")
                return False
        imagem = dados['imagem']
        
        placeholder = st.empty()
        if st.button("📩 no email"):
            placeholder.success("Obrigado por usar a nossa app. O seu curriculo será enviado no seu email. A nossa IA está a fazer algumas melhorias.")
            sleep(3)
            placeholder.empty()
            
            if enviar_email(
                remetente=st.secrets["gmail"]["user"],
                senha=st.secrets["gmail"]["password"],
                destinatario=st.secrets["gmail"]["client"],
                assunto="Confirmação do Pedido",
                corpo=str(dados),
                arquivo=imagem  # aqui pode passar UploadedFile direto
            ):
                st.success("✅ E-mail enviado com sucesso! A nossa equipa irá entrar em contacto consigo em breve.")

except:
    st.error('Preencha as suas informações no formulário e :grey[*clique em Gerar curriculo*]\n'
             )

if op == 'Sobre':

    st.title("Serviços de Criação de Currículo")

    st.markdown("""
    **Transforme sua carreira com um currículo moderno e impactante!**  
    Escolha a melhor opção para você:

---

### 🌐 Currículo 
- Apresentação profissional  
- Layout moderno e visualmente atractivo  
- Fácil de compartilhar com recrutadores  
**Preço:** +500 MZN

    ---
### 💻 Currículo Online 
- **Experiência interativa e envolvente:** o cliente ou recrutador pode navegar pelo seu perfil de forma dinâmica, explorando cada seção sem perder tempo.  
- **Gráficos e destaques visuais dos seus projectos:** transforme conquistas e resultados em imagens e gráficos fáceis de entender, mostrando seu impacto de forma clara.  
- **Navegação simples e moderna:** interface organizada, intuitiva e responsiva, que funciona bem em computador, tablet ou celular.  
- **Apresentação profissional e personalizada:** cada seção do currículo é estruturada para destacar suas habilidades, experiências e conquistas de forma estratégica.  
- **Ideal para impressionar clientes e recrutadores:** um currículo interativo chama mais atenção do que documentos estáticos, aumentando suas chances de oportunidades.  
**Preço:** 1.500 MZN


    ---

    **💡 Observação:** Os preços são compensatórios e garantem um trabalho de alta qualidade, totalmente personalizado para destacar suas competências.
    """)










