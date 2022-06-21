# pro-agg
Pro-Agg is a minimalist web application that aggregates news from several progressive publications using python web-scraping, flask to serve the api, and javascript on the front-end.

# Quick Start

1. Clone repository using git
    ```shell
    git clone https://github.com/a-w-m/pro-agg.git
    ```

2. Install Python 3
    - [Python 3](https://www.python.org/downloads/)

3. create virtual environment in root folder
```shell 
# Windows
py -3 -m venv venv
venv\scripts\activate
```

4. install python requirements
```shell
pip install -r requirements.txt
```

5. define environment variables in .env file located in root folder
```
# .env file
FLASK_APP=pro-agg.py
FLASK_ENV=development
```

6. install javascript packages in client folder
```shell
cd client
npm i 
```

7. bundle javascript files with webpack in client folder
```shell
cd client
npm run build
```
8. launch flask application from root directory
```shell
cd..
flask run
```
