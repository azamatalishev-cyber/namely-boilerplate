# BoilerPlate code to work with Namely API

This is a quick way to get started with the Namely API


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install required modules.

```bash
pip install -r requirements.txt
```
(Please note that if you have the `brew python` formula installed, you will use ```pip3`` instead)

## Usage
```python

def main():
    drive = Namely(
        'token_path')
    response = drive.send_api('GET', '/profiles')
    pprint(response.json())

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
