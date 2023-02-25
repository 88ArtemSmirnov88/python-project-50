
[![Actions Status](https://github.com/88ArtemSmirnov88/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/88ArtemSmirnov88/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/690c101b622ca0a1fdd0/maintainability)](https://codeclimate.com/github/88ArtemSmirnov88/python-project-50/maintainability)

# Gendiff - compare two json and/or yaml files
### About
___
You can get a comparison of two json/yaml files - different formats can be compared too!

The output type depends on the selected format:
* stylish - is selected by default
* plain
* json
### Install
___
```
git clone https://github.com/88ArtemSmirnov88/python-project-50
cd python-project-50
make install
```
### Help
___
```commandline
gendiff -h

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
### comparison of flat files (JSON)
___
[![asciicast](https://asciinema.org/a/m7bQARwsbavWlqeQ6XENMaxzn.png)](https://asciinema.org/a/m7bQARwsbavWlqeQ6XENMaxzn)
