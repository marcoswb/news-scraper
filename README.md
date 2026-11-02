# News Scraper

[![Python](https://img.shields.io/badge/python-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Scrapes top stories from major English-language news sites and delivers them as clean HTML emails. Built for **English-practice reading**: real news, cleaner layout, less distraction from ads and page chrome.

## Features

- Scrapes up to **5 articles** each from [BBC](https://www.bbc.com), [The Guardian](https://www.theguardian.com) (international / world), and [CBC](https://www.cbc.ca/news)
- Extracts title, link, body paragraphs, and subheadings
- Keeps limited inline formatting (`b`, `strong`, `i`, `em`, `blockquote`) and italicizes quoted speech
- Strips unrelated markup (links, images, and other tags are not preserved in the email body)
- Sends one HTML email per source via **Gmail SMTP**
- Optional daily run through **GitHub Actions** (scheduled and manual)

## Technologies

| Area | Stack |
|------|--------|
| Language | Python |
| HTTP / HTML | `requests`, Beautiful Soup (`bs4`) |
| Config | `python-dotenv` |
| Email | `smtplib` + Gmail (`smtp.gmail.com:465`) |
| Automation | GitHub Actions |

## Project structure

```
.
├── main.py                          # Entry point: scrape each source and send emails
├── requirements.txt
├── .github/workflows/
│   └── daily-news-email.yml         # Scheduled + manual workflow
└── src/
    ├── controllers/
    │   ├── email_sender.py          # Builds HTML and sends via Gmail
    │   └── enviroments.py           # Loads env vars (including from .env)
    ├── models/
    │   └── Article.py               # Article model and text formatting
    └── scrapers/
        ├── base.py                  # Shared page loading / CSS selection
        ├── BBC.py
        ├── TheGuardian.py
        └── CBC.py
```

## Prerequisites

- Python 3 (current releases work; CI runs on 3.11)
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) for SMTP
- Network access to the news sites and `smtp.gmail.com`

## Installation

```bash
git clone https://github.com/marcoswb/news-scraper.git
cd news-scraper
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root (the file is gitignored):

```env
SENDER=<Gmail address that sends the digests>
PASSWORD=<Gmail App Password for that account>
RECEIVER=<email address that receives the digests>
```

| Variable | Description |
|----------|-------------|
| `SENDER` | SMTP login / From address |
| `PASSWORD` | Gmail App Password (not the normal account password) |
| `RECEIVER` | To address for the digests |

The same three values are required as GitHub Actions secrets (`SENDER`, `PASSWORD`, `RECEIVER`) if you use the workflow.

## How to run

From the project root:

```bash
python main.py
```

This scrapes BBC, The Guardian, and CBC in sequence and sends one email per source that returned articles. Subject line format: `{Portal} - Daily English News`.

### GitHub Actions

Workflow: [`.github/workflows/daily-news-email.yml`](.github/workflows/daily-news-email.yml)

- **Schedule:** `30 14 * * *` (14:30 UTC every day)
- **Manual:** `workflow_dispatch` (run from the Actions tab)
- Installs dependencies and runs `python main.py` with the secrets above

## Usage notes

- Each scraper deduplicates by article title within that run and stops after 5 articles.
- The Guardian scraper starts from the international edition and only keeps URLs under `/world/`.
- BBC uses the homepage; CBC uses `/news`.
- Empty scrape results skip sending for that source (no empty email).

### Email example

Emails use collapsible HTML (`<details>`) with the article title linking to the original page and cleaned body text underneath.

<img width="686" height="669" alt="Example news email" src="https://github.com/user-attachments/assets/01c18862-c5ec-461e-b55f-5d9266c7235e" />

## License

This project is licensed under the [MIT License](LICENSE).
