# Automated Competitor Intelligence & AI Sentiment Dashboard

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.14-%23704214?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-Web_Scraping-%23A88B7D?style=for-the-badge&logo=selenium&logoColor=white" alt="Selenium">
  <img src="https://img.shields.io/badge/Google_Gemini-Generative_AI-%23704214?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-%23F5F1E6?style=for-the-badge&logo=streamlit&logoColor=black" alt="Streamlit">
</div>

---

## The Business Problem

Monitoring competitor pricing and extracting actionable insights from thousands of customer reviews manually is impossible to scale. For businesses operating in niche markets—such as **conscious fashion, minimalist apparel, and sustainable retail**—understanding real-time consumer sentiment (what they praise and what they complain about) is the key to maintaining a competitive edge.

## The Solution

This project is an automated **Data Engineering and Artificial Intelligence pipeline**. It acts as a stealthy market researcher that:

1. Scrapes dynamic e-commerce platforms to extract product data and customer reviews.
2. Feeds unstructured text into a Large Language Model (LLM).
3. Outputs a clean, executive dashboard with automated strategic insights.

---

## Architecture & Tech Stack

- **Extraction Engine (`extrator_avaliacoes.py`):** Uses **Selenium WebDriver** in headless mode and **BeautifulSoup** to bypass dynamic JavaScript rendering and extract raw consumer feedback.
- **Data Transformation:** Leverages **Pandas** and Regex to clean, structure, and normalize the scraped data into a relational format (`avaliacoes_brutas.csv`).
- **AI Brain (`analisador_ia.py`):** Integrates the **Google Gemini 2.5 Flash API** to perform advanced semantic sentiment analysis. It acts as a Senior Product Analyst, identifying the _Top 3 Praises_, _Top 3 Pain Points_, and generating a _Strategic Business Insight_.
- **Executive Interface (`dashboard.py`):** A frontend application built with **Streamlit**, featuring a bespoke UI/UX design (Sepia & Warm Beige palette) for clear data visualization and one-click AI report generation.

---

## How to Run Locally

**1. Clone the repository:**

```bash
git clone [https://github.com/your-username/fashiontech-competitor-intelligence.git](https://github.com/Camilalarissa/fashiontech-competitor-intelligence.git)
cd fashiontech-competitor-intelligence
```
