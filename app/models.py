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


    def get_by_id(self, id):
        for order in orders:
            if order.id == id:
                return order
                
    def get_all(self):
        return orders

    def serialize(self):
        return dict (
            id = self.id,
            name = self.name,
            description = self.description,
            price=self.price,
            status=self.status
        )