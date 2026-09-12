# 1. Song Class
class Song:
    def __init__(self, song_id, title, artist, duration):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.duration = duration

    def display(self):
        print("Song ID  :", self.song_id)
        print("Title    :", self.title)
        print("Artist   :", self.artist)
        print("Duration :", self.duration)


# 2. Node Class
class Node:
    def __init__(self, song):
        self.data = song
        self.next = None


# 3. Singly Linked List
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size_value = 0

    # 4. Add at Beginning
    def insert_first(self, song):
        new_node = Node(song)
        new_node.next = self.head
        self.head = new_node
        self.size_value += 1

    # 5. Add at End
    def insert_last(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.size_value += 1

    # 6. Insert at Position
    def insert_at(self, song, position):
        if position < 1 or position > self.size_value + 1:
            return False

        if position == 1:
            self.insert_first(song)
            return True

        new_node = Node(song)
        current = self.head

        for i in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.size_value += 1
        return True

    # 7. Search
    def search(self, song_id):
        current = self.head

        while current is not None:
            if current.data.song_id.lower() == song_id.lower():
                return current.data

            current = current.next

        return None

    # 8. Delete
    def delete(self, song_id):
        if self.head is None:
            return False

        if self.head.data.song_id.lower() == song_id.lower():
            self.head = self.head.next
            self.size_value -= 1
            return True

        current = self.head

        while current.next is not None:
            if current.next.data.song_id.lower() == song_id.lower():
                current.next = current.next.next
                self.size_value -= 1
                return True

            current = current.next

        return False

    # 9. Display Playlist
    def display(self):
        if self.head is None:
            print("Playlist is empty.")
            return

        current = self.head
        count = 1

        print("\n===== MUSIC PLAYLIST =====")

        while current is not None:
            print("\nSong #", count)
            current.data.display()

            current = current.next
            count += 1

        print("\nTotal songs:", self.size_value)

    # 10. Size
    def size(self):
        return self.size_value

    def is_empty(self):
        return self.head is None


# 11. Input Validation
def read_text(message):
    while True:
        value = input(message).strip()

        if value != "":
            return value

        print("Input cannot be empty.")


def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a valid number.")


# 12. Duration Validation
def read_duration():
    while True:
        duration = read_text("Enter Duration (MM:SS): ")
        parts = duration.split(":")

        if len(parts) == 2:
            try:
                minutes = int(parts[0])
                seconds = int(parts[1])

                if minutes >= 0 and 0 <= seconds <= 59:
                    return duration
            except ValueError:
                pass

        print("Invalid duration. Example: 4:23")


# 13. Create Song
def create_song(playlist):
    song_id = read_text("Enter Song ID: ")

    if playlist.search(song_id) is not None:
        print("Song ID already exists.")
        return None

    title = read_text("Enter Song Title: ")
    artist = read_text("Enter Artist: ")
    duration = read_duration()

    return Song(song_id, title, artist, duration)


# 14. Add Beginning
def add_beginning(playlist):
    song = create_song(playlist)

    if song is not None:
        playlist.insert_first(song)
        print("Song added at beginning.")


# 15. Add End
def add_end(playlist):
    song = create_song(playlist)

    if song is not None:
        playlist.insert_last(song)
        print("Song added at end.")


# 16. Insert Position
def insert_position(playlist):
    position = read_int(
        "Enter position (1-" + str(playlist.size() + 1) + "): "
    )

    if position < 1 or position > playlist.size() + 1:
        print("Invalid position.")
        return

    song = create_song(playlist)

    if song is not None:
        playlist.insert_at(song, position)
        print("Song inserted successfully.")


# 17. Search Song
def search_song(playlist):
    song_id = read_text("Enter Song ID: ")
    song = playlist.search(song_id)

    if song is None:
        print("Song not found.")
    else:
        print("\nSong found:")
        song.display()


# 18. Remove Song
def remove_song(playlist):
    song_id = read_text("Enter Song ID: ")

    if playlist.delete(song_id):
        print("Song removed successfully.")
    else:
        print("Song not found.")


# 19. Main Menu
def main():
    playlist = SinglyLinkedList()

    while True:
        print("\n================================")
        print("     MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = read_int("Enter your choice: ")

        if choice == 1:
            add_beginning(playlist)

        elif choice == 2:
            add_end(playlist)

        elif choice == 3:
            insert_position(playlist)

        elif choice == 4:
            playlist.display()

        elif choice == 5:
            search_song(playlist)

        elif choice == 6:
            remove_song(playlist)

        elif choice == 7:
            print("Total songs:", playlist.size())

        elif choice == 8:
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


# 20. Start Program
if __name__ == "__main__":
    main()
