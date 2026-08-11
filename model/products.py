class Products:
    def __init__(self,name='',product_id=''):
        self.name = name
        self.product_id =product_id
        self.products = []

    def add_product(self,name,product_id):

        product = {"product_name" :name,
                   "product_id": product_id
        }

        self.users_list.append(product)
        return f'{name} is added 200'

    def remove_product(self,name,product_id):

        self.products.remove({"product_name" :name,
                   "product_id": product_id})

        return f'{name} is removed 200'

    def show_products(self):
        return self.products




            


    
        