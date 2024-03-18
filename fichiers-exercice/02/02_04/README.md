## 💻  Project : Démarrer avec LangChain

## 🏗️ Installation:Prérequis : Installation Python

### [Python 3.6+](https://www.python.org/downloads/)

-[Mac](https://kinsta.com/knowledgebase/install-python/#mac)
-[Windows](https://kinsta.com/knowledgebase/install-python/#windows)

### 🛠️ Bibliothèques

- **LangChain** :[LangChain](https://www.langchain.com/) framework pour développer des applications alimentées par des modèles de langage
- **OpenAI** : [OpenAI](https://python.langchain.com/docs/integrations/platforms/openai)  bibliothèque Python qui fournit une interface simple vers l'API OpenAI. Elle propose également une interface en ligne de commande (CLI) pour interagir avec l'API.
- **python-dotenv** : [python-dotenv](https://pypi.org/project/python-dotenv/) bibliothèque Python qui charge les variables d'environnement à partir d'un fichier .env. Elle est utilisée pour charger la clé API OpenAI à partir du fichier .env.
- **colorama** : pour ajouter de la couleur au terminal 


## 🌐 Créer un environnement virtuel :

**MacOS/Linux**:

```
python -m venv env
python3 -m venv env (Mac)
source env/bin/activate

```

```
pip install -r requirements.txt
pip install --upgrade langchain
pip3 install -r requirements.txt(Mac)
pip3 install --upgrade langchain (Mac)
```

## [OpenAI API key](https://platform.openai.com/account/api-keys)

### Variable Environement:

`export OPENAI_API_KEY='sk-brHeh...A39v5iXsM2'`

.env file:

```
OPENAI_API_KEY=sk-brHeh...A39v5iXsM2
```

## ▶️ Démarrer l'application:

`python main.py`
`python3 main.py` (Mac)

