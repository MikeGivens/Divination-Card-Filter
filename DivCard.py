class DivCard(object):
    name = "none"
    chaosValue = "0"

    # The class "constructor" - It's actually an initializer 
    def __init__(self, name, chaosValue):
        self.name = name
        self.chaosValue = chaosValue
        
def make_divcard(name, chaosValue):
    divcard = DivCard(name, chaosValue)
    return divcard