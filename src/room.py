class Room:
    def __init__(self, name):
        self.name = name
        self.song_list = []
        self.guest_list = []


    def add_song_to_song_list(self, song):
        self.song_list.append(song)

    def length_of_song_list(self):
        return len(self.song_list)

    def add_guest_to_guest_list(self, guest):
        self.guest_list.append(guest)

    def length_of_guest_list(self):
        return len(self.guest_list)

    def remove_guest_from_guest_list(self, guest):
        self.guest_list.remove(guest)
    
    


    

    
    

