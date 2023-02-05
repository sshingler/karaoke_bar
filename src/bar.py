class Bar:
    def __init__(self, name, till):
        self.name = name 
        self.till = till
        self.total_room_list = []
        self.total_song_list = []
        self.total_guest_list = []

    def add_room_to_total_room_list(self, room):
        self.total_room_list.append(room)

    def length_of_total_room_list (self):
        return len(self.total_room_list)

    def add_song_to_total_song_list (self, song):
        self.total_song_list.append(song)

    def length_of_total_song_list (self):
        return len(self.total_song_list)

    def add_guest_to_total_guest_list(self, guest):
        self.total_guest_list.append(guest)

    def length_of_total_guest_list (self):
        return len(self.total_guest_list)

    # def get_till_total (self, till):
    #     till_total = self.till
    #     return till_total 

    # def add_cash_to_till (self, cash):
    #     cash_in = (self.till + cash)
    #     till_total = cash_in
    #     return till_total 


    # def increase_till_total (self, entry_fee):
    #     return 


    


    

