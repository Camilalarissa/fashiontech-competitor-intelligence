import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv

print("🧠 Iniciando o motor de Inteligência Artificial...")

# 1. Carregamento seguro da chave de API
load_dotenv()
CHAVE_API = os.getenv("GEMINI_API_KEY")

if not CHAVE_API:
    print("❌ Erro: Chave de API não encontrada. Verifique o arquivo .env.")
    exit()

genai.configure(api_key=CHAVE_API)

def analisar_sentimento(caminho_csv):
    # 2. Leitura dos dados extraídos no Passo 1
    try:
        df = pd.read_csv(caminho_csv)
    except FileNotFoundError:
        print("❌ Erro: Arquivo 'avaliacoes_brutas.csv' não encontrado.")
        return

    # 3. Preparação do texto (Limitamos aos 50 primeiros para análise rápida)
    comentarios = df['Comentário Original'].dropna().tolist()[:50]
    
    if not comentarios:
        print("⚠️ A tabela não possui comentários válidos para analisar.")
        return
        
    texto_completo = "\n- ".join(comentarios)
    print(f"✅ {len(comentarios)} comentários processados. Solicitando análise ao Gemini...")

    # 4. Engenharia de Prompt (O diferencial do seu projeto)
    prompt = f"""
    Atue como um Analista de Negócios e Produto Sênior. 
    Abaixo está uma lista de comentários brutos de clientes extraídos de um e-commerce.
    
    Por favor, analise esses textos e gere um Resumo Executivo formatado e direto ao ponto, contendo:
    1. Principais Qualidades: As 3 características mais elogiadas.
    2. Pontos de Atrito: As 3 maiores reclamações ou defeitos mencionados.
    3. Insight de Negócio: Uma recomendação estratégica de 2 linhas baseada nas reclamações.
    
    Comentários dos clientes:
    {texto_completo}
    """

    # 5. Conexão e Geração de Resposta
    modelo = genai.GenerativeModel("gemini-2.5-flash")
    resposta = modelo.generate_content(prompt)

    # 6. Exibição do Resultado
    print("\n" + "="*60)
    print("📊 RELATÓRIO DE SENTIMENTO E INTELIGÊNCIA COMPETITIVA")
    print("="*60)
    print(resposta.text)
    print("="*60)

# Executa a função
analisar_sentimento("avaliacoes_brutas.csv")