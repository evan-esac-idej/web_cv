import streamlit as st

# --- Configuração da página ---
st.set_page_config(page_title="Curriculum Vitae - Ginélio Tchavana", layout="wide")

# --- Cabeçalho ---
st.title("Curriculum Vitae")
st.subheader("Economist and Developer | gineliohermilio@gmail.com")
st.markdown("---")

# --- Estrutura em colunas ---
col1, col2 = st.columns([1, 2])

# --- Coluna 1 (Perfil + Educação + Contato) ---
with col1:
    st.header("Resumo")
    st.write("""
    Estudante finalista de Economia, com sólida base em Python, análise de dados e modelagem econômica.
    Experiência em aplicações web, automação de processos e dashboards interativos. 
    Também escritor premiado, integrando capacidades analíticas e criativas.
    """)

    st.header("Educação")
    st.write("**Eduardo Mondlane University | Maputo**")
    st.write("Bacharel em Economia (Conclusão esperada: 202X)")
    st.write("Cursos: Econometria, Microeconomia, Macroeconomia, Finanças, Análise de Dados")
    st.markdown("---")
    st.write("**Noroeste 1 Secondary School | Maputo (2018)**")
    st.write("Prêmio 'Young Literature – Conto'")

    st.header("Contacto")
    st.write("Email: gineliohermilio@gmail.com")
    st.write("Localização: Maputo, Moçambique")
    st.write("Telefone: +258 84 693 5922")
    st.markdown("---")

# --- Coluna 2 (Habilidades + Formações + Projetos + Certificados) ---
with col2:
    st.header("Habilidades")
    st.write("""
    **Técnicas:** Python (Data Analysis, Modeling), R, Stata  
    **Ferramentas:** Microsoft Office, Power BI, Photoshop, SQL, Visual Studio  
    **Quantitativas:** Econometria, Forecasting, Séries Temporais, Indicadores Econômicos  
    **Analíticas:** Resolução de Problemas, Pensamento Crítico, Pesquisa  
    **Comunicação e criativas:** Escrita, Apresentação, Storytelling, Design Gráfico, Desenho
    """)

    st.header("Formações Complementares")
    st.write("- Impact Evaluation (World Bank - DIME)")
    st.write("- Introdução à Inteligência Artificial Clássica")
    st.write("- Curso de Visualização de Dados com Python e Power BI")
    st.markdown("---")

    st.header("Projetos Relevantes")
    st.write("- **Dashboard Econômico**: Criação de dashboards interativos em Streamlit para indicadores macroeconômicos de Moçambique")
    st.write("- **Automação de Relatórios**: Scripts em Python para análise e resumo de dados econômicos")
    st.write("- **Projeto de Pesquisa**: Análise econométrica sobre impacto de políticas públicas na economia local")
    st.markdown("---")

    st.header("Certificados")
    st.write("- Data Analysis with Python (Coursera / IBM)")
    st.write("- Econometrics and Time Series (EDX / MIT)")
    st.write("- Power BI Essentials (Microsoft)")
