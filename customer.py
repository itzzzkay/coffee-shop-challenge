from order import Order

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

    def cust_orders(self):
        return[order for order in Order.all_orders if order.customer == self]

    def cust_coffee(self):
        return list(set(order.coffee for order in self.cust_orders()))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def most_aficionado(cls, coffee):
        spending_dic = {}

        for order in coffee.orders():
            customer = order._customer
            price = order._customer

            if customer not in spending_dic:
                spending_dic[customer] = 0
            spending_dic[customer] += price
        
        if not spending_dic:
            return None
        
        return max(spending_dic, key=spending_dic.get)
