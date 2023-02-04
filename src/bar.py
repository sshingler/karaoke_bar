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

    
    

