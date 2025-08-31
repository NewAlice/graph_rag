## graph_rag

## project structure
```
project
├── app/    
│   ├── common/--------------------common module
│   │   └──config.py--------------configration variables
│   │── controller/---------controller defination
│   │── service/------------service defination
│   └── main.py
├── tests/-------------------------unit tests
├── .env.example-------------------environment values example    
├── .gitignore
└── pyproject.toml-----------------python dependency
```

## install poetry
By default, the dependencies are managed with [Poetry](https://python-poetry.org/), go there and install it.

 - `pip install poetry`
 - run `poetry config virtualenvs.in-project true`, poetry will create .venv under project folder
 - run `poetry config virtualenvs.create true` poetry will create virtualenv if virtualenv not exits
 - run `poetry shell` virtualenv will be used

## install dependencies
run `poetry install` to install the project's dependencies

## local run
1. create .env based on .env.example, update values accordingly
2. `poetry run uvicorn app.main:app`
3. `graphrag init --root ./docs`
4. `graphrag index --root .`
5. `graphrag query --method local -q "文章出现了几次背影?"`


## more example 
`https://github.com/microsoft/graphrag/tree/main/docs/examples_notebooks`
`https://github.com/microsoft/graphrag/tree/main/examples_notebooks/community_contrib`

## local run unit test
1. create .env based on .env.example, update values accordingly
2. `poetry run pytest`

## graphrag import neo4j cypher
1. `docker run -e NEO4J_AUTH=neo4j/password -p 7687:7687 -p 7474:7474 neo4j`
2. 

