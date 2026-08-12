class Order:
    def __init__(self,name='',order_id='',products =[]):
        self.user_name = name
        self.products = products
        self.order_id =order_id

class Order_manager:
    def __init__(self):

        self.orders = {}

    def add_order(self,user_name,order_id,products):

        order = Order(name=user_name,order_id=order_id,products=products)

        self.orders[order_id] = order  
        return f'{order_id} is added [200]'

    def remove_order(self,order_id):

        if order_id in self.orders:
                del self.users_dict[order_id]
                return f'User {order_id} is removed'
        return 'user not in list'

    def update_order(self,order_id:int,new_products):
    
            # self.orders[order_id].name = new_user_name
            self.orders[order_id].products = new_products

            return f'new products are {new_products}'
        
    
    def get_order(self,user_id:int):
        return self.orders[user_id]

    def show_orders(self):
        return list(self.orders.values())
            


    
        