## 💻 Project :Publier avec LangServe et créer une API REST 


## 🛠️ Requirements : Installation & Setup

### Python 3.10.0

`brew install pyenv`
`pyenv install 3.10.0`

switch to python 3.10.0

`pyenv local 3.10.0`

### packages

- **LangChain** :[LangChain](https://www.langchain.com/) framework pour développer des applications alimentées par des modèles de langage
- **OpenAI** : [OpenAI](https://python.langchain.com/docs/integrations/platforms/openai)  bibliothèque Python qui fournit une interface simple vers l'API OpenAI. Elle propose également une interface en ligne de commande (CLI) pour interagir avec l'API.
- **python-dotenv** : [python-dotenv](https://pypi.org/project/python-dotenv/) bibliothèque Python qui charge les variables d'environnement à partir d'un fichier .env. Elle est utilisée pour charger la clé API OpenAI à partir du fichier .env.
- **uvicorn** : [Documentation](https://www.uvicorn.org/) implémentation de serveur web ASGI pour Python.


## 🌐 Créer un environnement virtuel :

**MacOS/Linux**:

```
python3 -m venv env
source env/bin/activate

```

**Windows**:

```
python -m venv env
source env/bin/activate
```

## 🏗️ Installation:

### Install Python 3.6 or higher

use pip3 on a Mac or Linux and pip on Windows

```
pip install -r requirements.txt
pip install --upgrade langchain
pip install "langserve[all]"
```

## [Get an API key](https://platform.openai.com/account/api-keys)

### Ajouter une clé API:

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

.env file:

```
OPENAI_API_KEY=sk-brHeh...A39v5iXsM2
```

### Installer serveur [uvicorn ASGI server](https://www.uvicorn.org/)
`pip install "uvicorn[standard]"`
`pip install pydantic==1.10.13` pour accéder à la docs

## Démarrer le serveur :
`uvicorn main:app --reload`
`python main.py`

## openai.error.APIConnectionError:[Error communicating with OpenAI](https://stackoverflow.com/questions/75920597/openai-error-apiconnectionerror-error-communicating-with-openai)

`bash /Applications/Python*/Install\ Certificates.command`

## Déployer to [Render](https://docs.render.com/deploy-fastapi)