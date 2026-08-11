class Product:
    def __init__(self,product_name,product_id):
        self.name = product_name
        self.product_id =product_id

class Products_Manager:
    def __init__(self,name='',product_id=''):
        
        self.products = {}

    def add_product(self,product_name,product_id):

        product = Product(product_name=product_name,product_id=product_id)

        self.products[product_id] = product 
        return f'{product_name} is added 200'

    def remove_product(self,product_id):

        if product_id in self.products:
                       del self.products[product_id]
                       return f'User {product_id} is removed'
        return 'product not in list'

    def show_products(self):
        return list(self.products.values())




            


    
        