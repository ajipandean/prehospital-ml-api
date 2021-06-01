<p align="center" style="margin-top: 32px;margin-bottom: 16px;">
  <img src="https://trello-attachments.s3.amazonaws.com/6090d4246149261a17b24089/60911a77064d92878e158b34/4dfc89d87d9160a3b35e6fa2f36eb0b4/Logo.png" alt="G-One Logo" />
</p>

# G-One Prehospital
> Repository for G-One Prehospital Machine Learning API

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#api-endpoints">API Endpoints</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

## Getting Started
This project is built using Python and Flask as web framework.

### Prerequisites
Please make sure you have these programs installed on your computer/laptop.

* Python v3.8.5 or later
* Python virtualenv library installed

### Installation
Follow these steps to replicate this project to your local computer/laptop.

1. Clone this project
   ```bash
   # Using HTTPS
   git clone https://github.com/g-one-capstone/prehospital-ml-api.git

   # Using SSH
   git clone git@github.com:g-one-capstone/prehospital-ml-api.git
   ```
2. Install dependencies
   ```bash
   $ cd prehospital-ml-api

   # virtualenv
   $ sudo apt install python3-virtualenv -y
   $ virtualenv venv
   $ source venv/bin/activate

   $ pip install -r requirements.txt
   ```
3. Run locally
   ```bash
   # for development
   $ python3 app.py
   ```
8. Enjoy!

## API Endpoints
Visit file ```api-enpoints.http``` to see all available endpoints.

Please make sure you use VS Code and have installed REST Client extension to run that file or you can use that file as reference and use another REST Client testing application.

## References
1. Python download link [here](https://www.python.org/downloads/).
2. Flask documentation website [here](https://flask.palletsprojects.com/en/2.0.x/)
3. Python virtualenv download link [here](https://virtualenv.pypa.io/en/latest/installation.html)