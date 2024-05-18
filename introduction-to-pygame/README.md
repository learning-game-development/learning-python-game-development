# :mortar_board: :snake: Pygame Quick start

:link: [pygame.org/docs](https://www.pygame.org/docs/)

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
