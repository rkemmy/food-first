orders = []

class Order:
    order_id = 1
    def __init__(self,name=None,description=None,price=None,status = "pending"):
        self.id = Order.order_id
        self.name =  name
        self.description =  description
        self.price = price
        self.status = status

        Order.order_id += 1