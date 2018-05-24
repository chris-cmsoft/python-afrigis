# Afrigis Python Library

### Installation

```bash
$ pip install afrigis
```

### Services:

#### Geocode

Example on using the Geocode service
```python
from afrigis.services import geocode
result = geocode('AFRIGIS_KEY', 'AFRIGIS_SECRET', 'NADID | SEOID')
print(result)
# {'number_of_records': 4, ...}
```

### Running tests

```bash
$ py.test
```

### Building and pushing to pypi

> In order to di this please make sure you are authenticated against Pypi first :).  
> You ca do this with the following method: https://docs.python.org/2/distutils/packageindex.html#the-pypirc-file

```bash
$ python setup.py register sdist upload --sign
```