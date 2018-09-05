class MixinsData(object):
    def __init__(
        self,
        user="rog",
        password="rog1",
        port="123",
        host="localhost",
        db="sqlite3"):

        self.user=user
        self.password=password
        self.port=port
        self.host=host
        self.db=db
    def get_username(self):
        return self.user

    def get_possword(self):
            return self.password
    def get_port(self):
            return self.port
    def get_host(self):
            return self.host
    def get_db(self):
            return self.db
    #Java y sus amigos
# MixinsData obj= new MixisData();


usuario = str(input("Nombre de Usuario? :___"))
password = str(input("Password? :___"))
# Python o Ruby
obj = MixinsData(password=password, user=usuario)

print(obj.user)
print(obj.password)

print(obj.get_username())

user = obj.get_username()

print (user * 10)
