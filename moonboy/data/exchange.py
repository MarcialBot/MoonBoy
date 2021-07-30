import ccxt

class Exchange:

    def __init__(self, name) -> None:
        self.name  = name 
        self.api = getattr(ccxt, name) () 
        self.api.load_markets()
         
    def __str__(self):
        return self.name

    def return_api(self):
        return self.api 
    