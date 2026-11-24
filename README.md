<p align="center">
  <img src="./.github/readme/hero.svg" width="100%" alt="FSBO Leads Bot: animated banner with a for-sale-by-owner house, a daily clock and rows landing in a sheet">
</p>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&amp;weight=600&amp;size=18&amp;duration=2600&amp;pause=700&amp;color=F4C65A&amp;center=true&amp;vCenter=true&amp;width=850&amp;height=42&amp;lines=Scheduled+on+GitHub+Actions+at+00%3A00+UTC.;Authenticates+to+Google+Sheets+with+a+service+account.;Appends+lead+rows+to+the+%22FSBO+Leads%22+sheet.;Early+stage%3A+scraping+sources+are+not+wired+in+yet." alt="Typing summary of FSBO Leads Bot">
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/kamikaze1120/FSBO-leads-bot?style=for-the-badge&amp;labelColor=15103A&amp;color=F4C65A" alt="Last commit">
  <img src="https://img.shields.io/github/languages/top/kamikaze1120/FSBO-leads-bot?style=for-the-badge&amp;labelColor=15103A&amp;color=BD3CFF" alt="Top language">
  <img src="https://img.shields.io/badge/Schedule-Daily_00%3A00_UTC-F4C65A?style=for-the-badge&amp;labelColor=15103A&amp;logo=githubactions&amp;logoColor=white" alt="Schedule: daily at 00:00 UTC">
  <img src="https://img.shields.io/badge/Output-Google_Sheets-3ddc97?style=for-the-badge&amp;labelColor=15103A&amp;logo=googlesheets&amp;logoColor=white" alt="Output: Google Sheets">
</p>

**FSBO Leads Bot** is the skeleton of a for-sale-by-owner (FSBO) lead pipeline. A GitHub Actions workflow runs a Python script once a day. The script signs in to Google Sheets with a service account and appends rows to a spreadsheet called **FSBO Leads**. The sheet plumbing and the schedule work today. The script only writes a single hard-coded test row, because no listing source is scraped yet.

<p align="center"><sub><code>FSBO</code> ✦ <code>LEAD PIPELINE</code> ✦ <code>GITHUB ACTIONS</code> ✦ <code>GOOGLE SHEETS</code> ✦ <code>EARLY STAGE</code></sub></p>

<h2 align="center">✦ HOW IT RUNS ✦</h2>
<p align="center"><sub>ONE WORKFLOW, ONE SCRIPT, ONE SHEET</sub></p>

```mermaid
flowchart LR
  T(["Cron 0 0 * * *<br/>or manual dispatch"]) --> W["GitHub Actions<br/>ubuntu-latest · Python 3.8"]
  S[/"Secret<br/>GOOGLE_CREDENTIALS_JSON"/] --> W
  W -->|writes credentials.json| P["fsbo_scraper.py"]
  P -->|gspread + oauth2client| G[("Google Sheet<br/>FSBO Leads · sheet1")]

  classDef gold fill:#1d1732,stroke:#F4C65A,color:#ffe293;
  classDef violet fill:#160f38,stroke:#BD3CFF,color:#f0d7ff;
  classDef green fill:#071331,stroke:#3ddc97,color:#c9ffe6;
  class T,W gold;
  class S,P violet;
  class G green;
```

<table>
  <tr>
    <td width="33%" valign="top">⏰ <b>Daily schedule</b><br><sub><code>cron: '0 0 * * *'</code> runs at midnight UTC. <code>workflow_dispatch</code> lets you run it by hand.</sub></td>
    <td width="33%" valign="top">🔐 <b>Secret-based auth</b><br><sub>The service-account key lives in a repository secret and is written to <code>credentials.json</code> at run time. It is never committed.</sub></td>
    <td width="33%" valign="top">📊 <b>Sheet output</b><br><sub>Rows go to the first worksheet of the spreadsheet titled <code>FSBO Leads</code> (street, city, state, phone, email).</sub></td>
  </tr>
</table>

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,githubactions,gcp&amp;theme=dark" alt="Python, GitHub Actions, Google Cloud">
</p>

<h2 align="center">◈ SETUP ◈</h2>
<p align="center"><sub>GOOGLE SHEETS + GITHUB SECRET</sub></p>

1. In Google Cloud, create a service account with the Google Sheets and Drive APIs enabled, then download its JSON key.
2. Create a Google Sheet named exactly **FSBO Leads** and share it with the service account's email as an editor.
3. Add the full JSON key as a repository secret named `GOOGLE_CREDENTIALS_JSON`.
4. Run **Automate FSBO Scraper** from the Actions tab, or wait for the nightly run.

| Name | Where | Purpose |
|---|---|---|
| `GOOGLE_CREDENTIALS_JSON` | GitHub Actions secret | Service-account key, written to `credentials.json` during the run |
| `credentials.json` | Local file (do not commit) | Key file read by `fsbo_scraper.py` |

<details>
<summary><b>Run it locally</b></summary>

<br>

```bash
git clone https://github.com/kamikaze1120/FSBO-leads-bot.git
cd FSBO-leads-bot
pip install gspread oauth2client pandas
# put your service-account key next to the script as credentials.json
python fsbo_scraper.py
```

</details>

<h2 align="center">◆ STATUS ◆</h2>
<p align="center"><sub>WHERE THE PROJECT STANDS</sub></p>

- **Working:** the scheduled workflow, the service-account login, and appending a row to the sheet.
- **Not implemented:** fetching real listings. The workflow installs `requests` and `beautifulsoup4` for this, but the current script doesn't use them. An earlier notebook prototype, since removed from the repo, sketched Zillow FSBO and Craigslist real-estate pages with de-duplication by listing URL.
- **Heads-up:** GitHub turns off scheduled workflows in repos with no recent activity. If the nightly run has stopped, re-enable it from the Actions tab.

<h2 align="center">✦ RESPONSIBLE USE ✦</h2>
<p align="center"><sub>BEFORE YOU POINT THIS AT A REAL SITE</sub></p>

> [!IMPORTANT]
> - Read and follow each site's **terms of service** and **`robots.txt`**. Many listing sites forbid automated scraping.
> - Keep request rates low, identify your client honestly, and back off on errors.
> - Seller contact details are personal data. Store them privately (never in a public repo or a public sheet) and delete what you don't need.
> - Follow the laws on contacting leads where you and they live, such as do-not-call registries, telemarketing and anti-spam rules, and real-estate licensing rules.

<br>

<p align="center">
  <sub><code>◉ FSBO LEADS BOT // GILDED ORBIT</code></sub><br>
  <sub>Made by <a href="https://github.com/kamikaze1120">kamikaze1120</a></sub>
</p>
