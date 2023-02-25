
[![Actions Status](https://github.com/88ArtemSmirnov88/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/88ArtemSmirnov88/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/15935953afcdb706c4a2/maintainability)](https://codeclimate.com/github/88ArtemSmirnov88/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/15935953afcdb706c4a2/test_coverage)](https://codeclimate.com/github/88ArtemSmirnov88/python-project-50/test_coverage)

# Gendiff - compare two json and/or yaml files
## About

You can get a comparison of two json/yaml files - different formats can be compared too!

The output type depends on the selected format:
* stylish - is selected by default
* plain
* json
## Install

```
git clone https://github.com/88ArtemSmirnov88/python-project-50
cd python-project-50
make install
```
## Help

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
## comparison of flat files (JSON)
[![asciicast](https://asciinema.org/a/m7bQARwsbavWlqeQ6XENMaxzn.png)](https://asciinema.org/a/m7bQARwsbavWlqeQ6XENMaxzn)
