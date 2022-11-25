# WORD CHAIN

Game to play word chain using a server

## Requirements.txt

### first install

```bash
pip install -r requirements.txt
```

### Add packages

Packages should be added to the [`requirements.in`](requirements.in) or to the [`dev-requirements.in`](dev-requirements.in).

After this, use `pip-compile` to translate these to [`requirements.txt`](requirements.txt) and [`dev-requirements.txt`](dev-requirements.txt).

```bash
pip-compile requirements.in
pip-compile dev-requirements.in
```

### Install and Uninstall packages

Packages can be installed with

```bash
pip-sync requirements.txt dev-requirements.txt
```

This will install all the packages specified in the requirement files and will uninstall the ones that are not.


### Execute

First you need to start the server
```bash
python main:app --reload
```

Second start streamlit
```bash
streamlit run app/frontend/interface.py
```

### Things that are not done
- Tests
- Score function
- Authorization method to check the user identity
- Timeout
- Possiblity of finishing the game

### How would you have done it?
- 

