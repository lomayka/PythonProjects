class Message:
    def __init__(self, sender='', reciever='', text='', status='created'):
        self.sender = sender
        self.reciever = reciever
        self.text = text
        self.status = status

    def __str__(self):
        return f'Status:{self.status}\nFrom "{self.sender}" to "{self.reciever}": {self.text}'
