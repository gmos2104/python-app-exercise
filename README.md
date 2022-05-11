# Python App Exercise

## Exercise
- Use the ApiService to fetch TODOs from an API and save them into the _storage_ folder
    - TODOs can be accessed from this URL: https://jsonplaceholder.typicode.com/todos/
    - Each TODO should be saved on a single file in CSV format
    - The filename must contain the TODO "id" prefixed with the current date.
        - Example: 2021_04_28_123.csv


## Extra points
- Use _requests_ library from [PyPI](https://pypi.org/project/requests/)


## Run the script
- Install required dependencies `pip install -r requirements.txt`
- Run the main script `python main.py`

- Some environment variables that affect the execution of the program:
    - `API_ENDPOINT`: Endpoint where the data will be retrieved from. Default: `https://jsonplaceholder.typicode.com/todos/`
    - `ID_FIELD`: Field in the data that will be used as ID in the saved filename. Default: `id`


## Running tests

- Install dev dependencies `pip install -r requirements-dev.txt`
- Run pytest `pytest`
