from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

def raspar_avaliacoes(url):
    print(f"🕵️‍♀️ Iniciando radar de espionagem na URL: {url}")
    
    # Configuração do navegador invisível para evitar bloqueios
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
    
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        driver.get(url)
        # Espera estratégica para o site carregar os comentários dinâmicos
        time.sleep(5) 
        
        sopa = BeautifulSoup(driver.page_source, 'html.parser')
        avaliacoes_extraidas = []
        
        # NOTA: Estas tags (div, p, span) são genéricas para simulação. 
        # Em um cenário real, inspecionamos a página do cliente para pegar a classe exata.
        # Aqui, vamos buscar blocos de texto que se pareçam com parágrafos longos de reviews
        comentarios = sopa.find_all('p') 
        
        for comentario in comentarios:
            texto = comentario.get_text(strip=True)
            # Filtro simples: assumimos que comentários reais têm mais de 30 caracteres
            if len(texto) > 30 and "cookies" not in texto.lower():
                avaliacoes_extraidas.append({
                    "Comentário Original": texto
                })
                
    except Exception as e:
        print(f"❌ Erro durante a extração: {e}")
    finally:
        driver.quit()
        
    df_reviews = pd.DataFrame(avaliacoes_extraidas)
    print(f"✅ Sucesso! {len(df_reviews)} avaliações coletadas.")
    return df_reviews

# Testando com um link (pode ser substituído por qualquer produto da Renner, C&A, etc.)
url_alvo = "https://www.lojasrenner.com.br/c/feminino/moda-responsavel" # Link de exemplo
df_resultado = raspar_avaliacoes(url_alvo)

# Salvando a matéria-prima para a IA usar no próximo passo
if not df_resultado.empty:
    df_resultado.to_csv("avaliacoes_brutas.csv", index=False, encoding='utf-8-sig')
    print("💾 Dados salvos em 'avaliacoes_brutas.csv'")