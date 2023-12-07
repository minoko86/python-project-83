### Hexlet tests and linter status:
[![Actions Status](https://github.com/minoko86/python-project-83/workflows/hexlet-check/badge.svg)](https://github.com/minoko86/python-project-83/actions)
[![Python CI](https://github.com/minoko86/python-project-83/actions/workflows/pyci.yml/badge.svg)](https://github.com/minoko86/python-project-83/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/3e83d09f9a5f02262901/maintainability)](https://codeclimate.com/github/minoko86/python-project-83/maintainability)

# Page Analyzer

Page Analyzer is a web application that analyzes URLs and provides information about them through various request methods. It retrieves parameters such as title, description, status code, and more. The application also keeps a history of user requests in an SQL database and provides a separate page to view all URLs and their analysis history.

## Features

- Analyze URLs using request method
- Retrieve parameters like title, description, status code, etc.
- Store and manage user request history in an SQL database
- View all URLs and their analysis history on a dedicated pages

## Usage

1. Enter a URL in the input field and click "Проверить" button
3. On the url page click "Запустить проверку" button to start check
4. See the result below
5. Navigate to the "Сайты" page to see a list of all analyzed URLs
6. Click on a URL to view its detailed analysis history

## Technologies Used

- Python
- Flask (Web framework)
- HTML/CSS
- SQL (Database)

## Contributions

Contributions to the Page Analyzer project are always welcome! If you encounter any issues or have suggestions for enhancements, please submit an issue or pull request. 

### Installation
**Setting up enviroment**
```bash
git clone https://github.com/minoko86/python-project-83/
cd page_analyzer
make build
```

Configure .env in the root folder
```
cp .env_example .env
```

**Dev**
```bash
make dev
```

**Prod**
```bash
make start
```

*Additional functions are available in Makefile*

### View site here:
[Analyzer](https://speed-page-analyzer.onrender.com/)