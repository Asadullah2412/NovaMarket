class User:
    def __init__(self,user_name,user_id):
        self.name = user_name
        self.user_id = user_id


class User_manager:
    def __init__(self):
        
        self.users_dict = {}

    def add_user(self,name,user_id):

        new_user = User(user_name=name,user_id=user_id)

        self.users_dict[user_id] = new_user # adding as object
        return f'{name} is added [200]'

    def remove_user(self,user_id):

        if user_id in self.users_dict:
            del self.users_dict[user_id]
            return f'User {user_id} is removed'
        return 'user not in list'

    def update_user(self,user_id:int,new_user_name:str):

        self.users_dict[user_id].user_name = new_user_name
        return f'username is updated to {new_user_name}'

    def get_user(self,user_id:int):
        return self.users_dict[user_id]

    def show_users(self):
        return list(self.users_dict.values())
            


    
# testing⚠️⚠️⚠️⚠️


# um = User_manager()

# x = um.add_user(name='wala',id=3)
# x = um.add_user(name='rala',id=4)
# x = um.add_user(name='aala',id=5)
# x = um.add_user(name='sala',id=6)
# x = um.add_user(name='dala',id=7)
# # print(x)

# # y = um.show_users()
# # print(y)
# print)