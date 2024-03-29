# RSS Parser

---
This is an   over-engineered script for retrieving RSS news feeds.  
For example [NY Times RSS-feed](https://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml) in category "Perasonal Tech".

### Usage

First install dependencies with [poetry](https://python-poetry.org/docs/basic-usage/):

```shell
poetry install 
```

Then activate virutal environment:

```shell
poetry shell
```
or
```shell
source .venv/bin/activate
```

### Configuration

You need to specify the environment variables in `.env`-file.  
Example:

```dotenv
RSS_URL=
TIME_SLEEP=
LOG_FILE=
JSON_FILE=
SHOW_STATISTICS=
```

Also check the `env.example` for changes.

Now you can run parser with following command:

```shell
poetry run python start_parser.py
```
or
```shell
python start_parser.py
```
