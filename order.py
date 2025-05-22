class Order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        self._customer = customer
        self._coffee = coffee
        self._price = price

        Order.all_orders.append(self)

        if not (1.0 <= price <= 10.0):
            raise TypeError("Price must be within the correct range!!")

        if not isinstance(price, float):
            raise TypeError("The price must be a float!!")

    @property
    def customer(self):
        return self._customer

    @property 
    def price(self):
        return self._price
    
    @property 
    def coffee(self):
        return self._coffee