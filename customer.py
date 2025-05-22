class Customer:

    all_customers = []

    def __init__(self, name):
        self.name = name
        Customer.all_customers.append(self)

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name (self, name):
        if len(name) > 15:
            raise TypeError("Maximum charcters for the name is 15!")
        
        if not isinstance(name, str):
            raise TypeError("The name typed must be a string!")
        
        else:
            return self._name