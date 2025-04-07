name: Trier les chansons automatiquement

on:
  push:
    branches:
      - main  

jobs:
  trier:
    runs-on: ubuntu-latest

    steps:
    - name: Vérifier le code du dépôt
      uses: actions/checkout@v2

    - name: Installer Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'  

    - name: Installer les dépendances
      run: |
        pip install -r requirements.txt  
    - name: Exécuter le script de tri des chansons
      run: |
        python trier_chansons.py 

    - name: Commiter les changements triés
      run: |
        git config --global user.name "github-actions"
        git config --global user.email "github-actions@users.noreply.github.com"
        git add .
        git commit -m "Trier les chansons automatiquement"
        git push

