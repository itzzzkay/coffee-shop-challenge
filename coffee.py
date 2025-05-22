from order import Order

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

    def coffee_orders(self):
        return[order for order in Order.all_orders if order.coffee == self]
    
    def coffee_customers(self):
        return list(set(order.customer for order in self.coffee_orders()))
    
    def num_orders(self):
        return len(self.coffee_orders())
    
    
