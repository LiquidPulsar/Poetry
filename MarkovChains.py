from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_etexts

def GetTexts(method = "Title",_key):
  if method == "Title":
    Stuff = get_etexts('title', _key))
    text = set(strip_headers(load_etext(index)).strip() for index in Stuff)
    return text
    
