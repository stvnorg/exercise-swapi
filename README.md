### Introduction
This repo is the answer of the OneLogin code-challenge for https://swapi.dev API
It is written in Python (compatible with v2.7 and v3.x). And it is only need `swapi` pip module to be installed.


### Installation
- Git clone this repo https://github.com/stvnorg/exercise-swapi.git
- It is recommended that you use virtualenv
- If you choose to run the script under the virtualenv please follow below instruction
  ###### `$ virtualenv .venv`
  ###### `$ source .venv/bin/activate`

- Install the required pip module 
###### `$ pip install -r requirements.txt`

### Important Step!
FYI the current `swapi` module is still using http://swapi.co/api as it's BASE_URL, based on the last activity in the swapi github page https://github.com/phalt/swapi-python/pull/10, there was a PR to fix this, but somehow the latest changes hasn't been merged yet.

So, it is very necessary for you to replace the http://swapi.co with http://swapi.dev as the BASE_URL in your `swapi` pip module path, example (if you use virtualenv as above), the BASE_URL located in `.venv/lib/python{version}/site-packages/swapi/settings.py`

Anyhow even if you missed this step, the script will send you a warning.

### Running the script
###### `./exercise.py 1` 
(Find all ships that appeared in Return of the Jedi)

###### `./exercise.py 2` 
(Find all ships that have a hyperdrive rating >= 1.0)

###### `./exercise.py 3` 
(Find all ships that have crews between 3 and 100)
