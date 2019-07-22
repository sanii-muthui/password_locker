#credential class
class Credential:
    """
    a class that generates new credential for users
    """
    pass
    credential_array = [] #empty array

    def __init__(self, password, email):
        self.email = email
        self.password = password

    def save_credential(self):
        """
        save_contact method saves credentials objects into credential_array
        """
        Credential.credential_array.append(self)

    @classmethod
    def display_credential(cls):
        """
        method that returns the credential array
        """
        return cls.credential_array
