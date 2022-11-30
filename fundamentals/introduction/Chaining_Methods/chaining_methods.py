class User:
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
#Have this method print all the users' details on separate lines.
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self
#Have this method change the user's member status to True and set their card points to 200.
    def enroll(self):
        if(self.is_rewards_member == False):
            self.is_rewards_member = True
        else:
            print("Already a member")
            
        self.gold_card_points = self.gold_card_points + 200
        print(self.is_rewards_member,self.gold_card_points)
        return self
#Have this method decrease the user's points by the amount spcified
    def spend_points(self,amount):
        if(self.gold_card_points - amount >= 0):
            self.gold_card_points = self.gold_card_points - amount
            print(self.gold_card_points)
        else:
            print("Not enough points.")
        return self



luke = User("Luke","Skywalker","jedi@email.com","70")
han = User("Han","Solo","falcon_pilot@email.com","75")
leia =User("Leia","Organa","RIP_Alteran@email.com","67")


luke.display_info().enroll().spend_points(50).display_info()






