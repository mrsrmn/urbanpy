# urbanpython

urbanpython is an API wrapper for the Urban Dictionary JSON API

## Installation

To install urbanpy, do:

``pip install urbanpython``

or

``python -m pip install urbanpython``

## Documentation

This README file is the documentation

## Examples

To get your API key, go to https://rapidapi.com/community/api/urban-dictionary/endpoints and get your API key

![This is your API key](https://i.imgur.com/5WojesI.png)

```python
import urbanpython

urban = urbanpython.Urban("-your api key-")
result = urban.search("the thing you are gonna search")

print(result.definition)     #Definition of the post
print(result.permalink)      #The link to the post
print(result.thumbs_up)      #Number of thumbs ups
print(result.thumbs_down)    #Number of thumbs downs
print(result.sounds_url)     #A list of the sounds urls in the post
print(result.author)         #The author of the post
print(result.defid)          #The ID of the definition
print(result.written_on)     #The time the definition got written on
print(result.example)        #The example of the post

```
