class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if len(name) < 3:
            raise TypeError("Coffee name must be at least 3 characters!!")
        
        if not isinstance(name, str):
            raise TypeError("Coffee name must be a string!!")
        
        if hasattr(self, "_name"):
            raise AttributeError("The coffee name has already been set and cannot be changed!!")
        
        self._name = name

    
    