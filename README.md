<p align="center">
  <a href="https://pro-agg.herokuapp.com/">
    <img alt="Pro-Agg" src="assets\screenshot.png" width="200" />
  </a>
</p>

# Description
[Pro-Agg](https://pro-agg.herokuapp.com/) is a minimalist web application that aggregates news from several progressive publications using Python web-scraping, Flask to serve the api, and JavaScript on the front-end.

# Quick Start

1. Clone repository using git

> Run the following command on the command line

    ```shell
    git clone https://github.com/a-w-m/pro-agg.git
    ```

2. Install Python 3
    - [Python 3](https://www.python.org/downloads/)

3. Create virtual environment in root folder

```shell 
# Windows
py -3 -m venv venv
venv\scripts\activate
```

4. Install python requirements

> From the root directory, run the following command to install the backend requirements

```shell
pip install -r requirements.txt
```

5. Define local environment

> In the root directory, create a file called .env with the following variable declarations 

```
# .env file
FLASK_APP=pro-agg.py
FLASK_ENV=development
```

6. Install javascript packages in client folder

> Navigate to the client folder and then run the following command to install node packages

```shell
cd client
npm i 
```

7. Bundle javascript files with webpack in client folder

> From the client folder, run the build script to bundle the frontend files

```shell
cd client
npm run build
```

8. Launch Flask application from root directory

> Navigate to the root directory, run the following command to initiate our Flask application which serves the html file and the api data to the client.

```shell
cd..
flask run
```

> In your broweser, visit localhost:5000 to view the application