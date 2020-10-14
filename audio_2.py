class Track():
    def __init__(self, name="Незаполненное название", duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.duration} min."


# Эти 3 функции я нагуглил для сравнения длительностей. Важно их прописать в этом классе, а не в Album
    def __lt__(self, other):
        return self.duration < other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __gt__(self, other):
        return self.duration > other.duration



class Album():
    def __init__(self, name=" ", group=" "):
        self.name = name
        self.group = group
        self.tracks = []

    def __str__(self):
        print(f"Name group '{self.group} \nName album '{self.name}''.")
        for s in enumerate(self.get_tracks(), 1):
            print(f"     {s[0]}. {s[1]}")
        print(f"Общая длительность альбома: {self.get_duration()} минут.\n")




    def get_tracks(self):
        return [i.__str__() for i in self.tracks]

    def get_duration(self):
        return sum([i.duration for i in self.tracks])

    def add_track(self, value_from_track_class):
        if not isinstance(value_from_track_class, Track):
            raise NotImplementedError('ERROR OF APPENDING!!!!')
        self.tracks.append(value_from_track_class)


albums = []

album1 = Album("Первый альбом", "Первый исполнитель")
album1.add_track(Track("Частушка", 1))
album1.add_track(Track("Лирика", 4))
album1.add_track(Track("Романс", 3))
albums.append(album1)

album2 = Album("Другой альбом", "Другой исполнитель")
album2.add_track(Track("Баллада", 2))
album2.add_track(Track("Менуэт", 5))
album2.add_track(Track("Серенада", 5))
albums.append(album2)

# Проверяем код:
# Задание 1.1
track1 = Track('Bohemian rhapsody', 6)
print(track1)
print()
# Задание 1.2
album1.__str__()
print()
# Задание 2
track1 = Track('Bohemian rhapsody', 6)
track2 = Track('The show must go on', 4)
print(track1 > track2)



