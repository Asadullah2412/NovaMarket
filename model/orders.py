class Users:
    def __init__(self,name='',order_id='',products =[]):
        self.user_name = name
        self.products = products
        self.order_id =order_id
        self.orders = []

    def add_order(self,user_name,order_id,products):

        order = {'Order_id' : order_id,
            'User_name':user_name,
                'Products' : products,
                }

        self.users_list.append(order)
        return f'{order_id} is added [200]'

    def remove_product(self,name,user_name,order_id,products):

        self.orders.remove({'Order_id' : order_id,
            'User_name':user_name,
                'Products' : products,
                })

        return f'{order_id} is removed [200]'

    def show_products(self):
        return self.orders
            


    
        