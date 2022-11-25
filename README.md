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

### MongoDB
Install mongoDB
```
brew install mongodb-community
```

```
brew services start mongodb/brew/mongodb-community
```

Create the **wordchain** database and the collections **games** and **users** (I recommend using mongo compass for this step)


## Execute

First you need to start the server
```bash
uvicorn main:app --reload
```

Second start streamlit
```bash
streamlit run app/frontend/interface.py
```

## Things that are not done
- Tests
- Score function
- Authorization method to check the user identity
- Possiblity of finishing the game and timeout
- Validate if it is an existing word
- Validate if it is only one word
- Comments
- Button to return the history

## Things to improve
- The way I get the words. It's really rudimentary and can take a while.

## Calirications

I would have performed the tests using pytest. I would have made fixtures for the creation of users and games. I would have tested the limit cases such as, for example, that only one word is sent per item, that the word validator is correct, that the user who makes the call is the correct one, etc.

For the score function a method that would count the vowels and consonants in a linear way, something similar to:

```python
vowels = [a,e,i,o,u]
score = 0
score_vowels = [2 for letter in list(word) if letter in vowels]
score_consonants = [1 for letter in list(word) if letter not in vowels]
score = sum(scores_vowels) + sum(scores_consonants)
```
And to count the time and see if it had taken less than 15s I had the updated_time field, which I could compare with the current time and apply the multiplier


For authorization I would have done the following: 
- The user inputs a username and password into your app’s UI
- The app sends that username and password to a specific auth endpoint in our API (called /token)
- If the password and username check out, the API send back a token (along with an expiry date) back to the app
- The app stores that token in the app state
For every subsequent API call, the app sends Authorization with a value of Bearer and the token, as well as the request to make the API call

For the ability to terminate I had a status within the line item data model which was "terminated".

And for the timeout my idea was to use some python library that follows the cron style and set a timer that would fire a method after two minutes and every time the endpoint /play was called it would restart again.

To validate if it is an existing word, I could have used the ntlk library where there is a dictionary of words that could tell me if it is a valid word or not.

Finally, for the history button, I had the field inside the schema of the game collection where I was saving the different words.