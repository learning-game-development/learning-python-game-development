# :mortar_board: :snake: Introduction to Pygame Zero

:link: [tutorial](https://pygame-zero.readthedocs.io/en/stable/introduction.html)

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
pipenv install pgzero
pgzrun introduction/intro.py
```

### Step 3: Install and Run Mu Editor

```shell
pipenv install mu-editor --dev
mu-editor
```

### Step 4: Finalizing the Project Dependencies

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
