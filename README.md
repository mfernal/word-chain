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
uvicorn main:app --reload
```

Second start streamlit
```bash
streamlit run app/frontend/interface.py
```

### Things that are not done
- Tests
- Score function
- Authorization method to check the user identity
- Possiblity of finishing the game and timeout
- Validate if it is an existing word
- Validate if it is only one word
- Comments
- Button to return the history

### Things to improve
- The way I get the words. It's really rudimentary and can take a while.

### Calirications

I would have performed the tests using pytest. I would have made fixtures for the creation of users and games. I would have tested the limit cases such as, for example, that only one word is sent per item, that the word validator is correct, that the user who makes the call is the correct one, etc.

For the score function a method that would count the vowels and consonants in a linear way, something similar to:

```python
vowels = [a,e,i,o,u]
score = 0
scores_vowels = [2 for letter in list(word) if letter in vowels]
scores_consonants = [1 for letter in list(word) if letter not in vowels]
score = sum(scores_vowels) + sum(scores_consonants)
```

For authorization I would have done the following: 
- The user inputs a username and password into your app’s UI
- The app sends that username and password to a specific auth endpoint in our API (called /token)
- If the password and username check out, the API send back a token (along with an expiry date) back to the app
- The app stores that token in the app state
For every subsequent API call, the app sends Authorization with a value of Bearer and the token, as well as the request to make the API call



