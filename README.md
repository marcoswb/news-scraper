# *News Scraper* — Notícias frescas. Leitura limpa. Inglês melhor!

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)   
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)  


Um scraper de notícias em inglês que envia diariamente resumos de portais de qualidade diretamente para o seu e-mail. Ideal para praticar leitura, vocabulário e acompanhar atualidades sem distrações.

---

## 🔍 Visão Geral  

O News Scraper coleta as principais notícias de portais confiáveis (BBC, The Guardian e CBC) e envia resumos completos com título, subtítulos, parágrafos, negritos e falas em itálico diretamente para o seu e-mail.

O foco é:
- Facilitar a prática de inglês com textos reais
- Manter a leitura limpa e organizada
- Destacar palavras importantes e falas de pessoas

---

## ✅ Funcionalidades  

- 📥 **Scraping** de notícias dos portais [BBC](https://www.bbc.com), [The Guardian](https://www.theguardian.com) e [CBC](https://www.cbc.ca);
- 🧹 **Transformação e organização** de dados, capturando e destacando títulos, parágrafos, negritos/falas/etc...   
- 💾 **Limpeza** de links, imagens e formatações desnecessárias; 
- ⏰ Envio diário de **e-mails em HTML** com as notícias completas;

---

## 🛠 Como usar / Setup  

### 1. Clone o repositório  
```bash
git clone https://github.com/marcoswb/news-scraper.git
cd news-scraper
```

### 2. Configure variáveis de ambiente  
Crie um arquivo `.env` na raiz do projeto com as credenciais para envio de emails(para a variável `PASSWORD`(senha de aplicativo do Gmail) a geração da mesma deve ser feita seguindo [esse passo a passo de configuração no Gmail](https://support.google.com/accounts/answer/185833?hl=pt-BR)):  
```env
SENDER=<email que irá enviar as notícias>
PASSWORD=<senha(de aplicativo) do email que irá enviar as notícias>
RECEIVER=<email que irá receber as notícias>
```

### 3. Iniciar script com GitHub Actions


---

## 📊 Exemplos / Resultados  

### Notícia enviada para o email
<img width="419" height="702" alt="image" src="https://github.com/user-attachments/assets/e73e4c25-41ae-4889-bdb4-546fa3f01920" />


---

## 📝 Licença  

Este projeto está licenciado sob a [MIT License](LICENSE).  

---
