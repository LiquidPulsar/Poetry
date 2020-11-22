





class Word(str):
    def __init__(self,name):
        self.name = name

    @property
    def rhymes(self):
        import requests
        from bs4 import BeautifulSoup
        page = requests.get("https://www.rhymezone.com/r/rhyme.cgi?typeofrhyme=perfect&loc=dmapi2&Word="+self.name)
        soup = BeautifulSoup(page.content, 'html.parser')
        return [word.get_text().replace("\xa0"," ") for word in soup.select("html body center table b a", class_ = "r")][1:] #first word always Spruce idk so we avoid that one, \xao used
    

def rhymes(word):
    import requests, cchardet
    from bs4 import BeautifulSoup
    page = requests.get("https://www.rhymezone.com/r/rhyme.cgi?typeofrhyme=perfect&loc=dmapi2&Word="+word)
    #page = requests.get("https://www.rhymezone.com/r/rhyme.cgi?Word="+word+"&typeofrhyme=adv&loc=advlink2")

    soup = BeautifulSoup(page.content, 'lxml')
    words = []
    for word in soup.select("html body center table b a"):
        if word == "†": # this symbol shows the start of the near rhymes, so we cut the rest off
            break
        words.append(word.get_text().replace("\xa0"," "))
    return words


def near(word):
    import requests
    from bs4 import BeautifulSoup
    page = requests.get("https://www.rhymezone.com/r/rhyme.cgi?Word="+word+"&typeofrhyme=rel&org1=syl&org2=l&org3=y")
    soup = BeautifulSoup(page.content, 'html.parser')
    #==========================WIP==========================

