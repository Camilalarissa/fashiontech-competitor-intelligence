import streamlit as st
import pandas as pd
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. Configuração da Página e Paleta Minimalista
st.set_page_config(page_title="Radar de Inteligência", layout="wide")

st.markdown("""
    <style>
    .stApp {
        background-color: #F5F1E6;
        color: #704214;
    }
    h1, h2, h3 {
        color: #704214 !important;
    }
    .stButton>button {
        background-color: #704214;
        color: #F5F1E6;
        border-radius: 5px;
        border: none;
    }
    .stDataFrame {
        border: 1px solid #A88B7D;
    }
    .box-insight {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #704214;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    /* Nova regra para corrigir as cores das caixas de aviso do Streamlit */
    div[data-testid="stAlert"] {
        background-color: #D9C5B2; /* Bege mais escuro para contraste */
        color: #704214 !important;
        border: 1px solid #704214;
    }
    div[data-testid="stAlert"] * {
        color: #704214 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Radar de Inteligência Competitiva")
st.markdown("Monitoramento de mercado e análise de sentimento de consumidores focada em e-commerce.")

st.markdown("---")

# 2. Carregamento dos Dados
@st.cache_data
def carregar_dados():
    try:
        return pd.read_csv("avaliacoes_brutas.csv")
    except:
        return pd.DataFrame()

df = carregar_dados()

if df.empty:
    st.warning("Nenhum dado encontrado. Rode o extrator primeiro.")
else:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 Matéria-Prima Coletada")
        st.dataframe(df, height=400)
        st.caption(f"Total de avaliações extraídas: {len(df)}")

    with col2:
        st.subheader("🧠 Cérebro Analítico (IA)")
        
        if st.button("Gerar Relatório Executivo com Gemini"):
            with st.spinner("Analisando centenas de avaliações..."):
                load_dotenv()
                CHAVE_API = os.getenv("GEMINI_API_KEY")
                
                if not CHAVE_API:
                    st.error("Chave de API não encontrada no arquivo .env")
                else:
                    genai.configure(api_key=CHAVE_API)
                    modelo = genai.GenerativeModel("gemini-2.5-flash")
                    
                    comentarios = df['Comentário Original'].dropna().tolist()[:50]
                    texto_completo = "\n- ".join(comentarios)
                    
                    prompt = f"""
                    Atue como um Analista de Negócios e Produto Sênior. 
                    Analise os comentários e gere um Resumo Executivo em tópicos com:
                    1. Principais Qualidades.
                    2. Pontos de Atrito.
                    3. Insight Estratégico.
                    
                    Comentários: {texto_completo}
                    """
                    
                    try:
                        resposta = modelo.generate_content(prompt)
                        st.markdown('<div class="box-insight">', unsafe_allow_html=True)
                        st.markdown(resposta.text)
                        st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Erro na comunicação com a IA: {e}")