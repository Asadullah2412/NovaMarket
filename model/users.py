class Users:
    def __init__(self,name="",user_id=""):
        self.name = name
        self.user_id = self.user_id
        self.users_list = []

    def add_user(self,name,id):

        user = {name:id}

        self.users_list.append(user)
        return f'{name} is added 200'

    def remove_user(self,name,id):

        self.users_list.remove({name:id})

        return f'{name} is removed 200'

        

    def show_users(self):
        return self.users_list
            


    
# testing⚠️⚠️⚠️⚠️

user_01 = Users()

add_user = user_01.add_user(name='LALA',id=1)
print(add_user)

add_user = user_01.add_user(name='BALA',id=2)
print(add_user)

add_user = user_01.add_user(name='KALA',id=3)
print(add_user)


delete_user = user_01.remove_user(name='LALA',id=1)
print(delete_user)

users_list = user_01.show_users()
print(users_list)

