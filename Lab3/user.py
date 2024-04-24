#init - construktor
#str - do wyświetlania construktora

class User():

    def _init_(self,id,username,password):

        self.id = id
        self.username = username
        self.password = password

    def _str_(self):
        return f"User ID: {self.id}"