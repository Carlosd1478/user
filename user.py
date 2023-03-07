class User:
    
    def __init__( self, first_name, last_name, email, age ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info( self ):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self

    def spend_points(self, amount):
        self.gold_card_points -= amount
        
user1 = User("carlos","delgado", "dfd@gmail.com", 25)
user2 = User("mike", "waski", "mnsterinc@gmail.com", 12)

# user1.display_info()
# user1.enroll()
# print(user1.is_rewards_member)
# user1.spend_points(50)
# print(user1.gold_card_points)

# user2.display_info()
# user2.enroll()
# print(user2.is_rewards_member)
# user2.spend_points(80)
# print(user2.gold_card_points)
