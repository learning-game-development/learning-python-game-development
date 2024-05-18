# :mortar_board: :snake: Python Platformer Game Tutorial for Beginners

:link: [YouTube tutorial](https://youtu.be/6gLeplbqtqg?si=KgKjJJ5aPVwMKMIH) from freeCodeCamp.org  
:link: [Assets and Completed Code](https://github.com/techwithtim/Python-Platformer/tree/main/assets)

## :bookmark_tabs: Running the Code

### Step 1: Managing the Virtual Environment

The packaging tool is `pipenv` and should be installed globally:

```shell
pip install --user pipenv
```

Create/open and close the virtual environment:

```shell
pipenv shell
exit
```

### Step 2: Intstall and Run PyGame

```shell
pipenv install pygame
python introduction/intro.py
```

### Step 3: Finalizing the Project Dependencies

```shell
pipenv lock
```

Install dependencies in production:

```shell
pipenv install --ignore-pipfile
```

Other developers collaborating on the code:

```shell
pipenv install --dev
```
