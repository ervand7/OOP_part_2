class Track:
    def __init__(self, name="Незаполненное название", duration=0):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name} - {self.duration} min."

    def __lt__(self, other):
        return self.duration < other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __gt__(self, other):
        return self.duration > other.duration


class Album:
    def __init__(self, name=" ", group=" "):
        self.name = name
        self.group = group
        self.list_tracks_in_album = []

    def add_track_in_album(self, value_from_track_class):
        if not isinstance(value_from_track_class, Track):
            raise NotImplementedError('ERROR OF APPENDING!!!!')
        self.list_tracks_in_album.append(value_from_track_class)

    def get_tracks_for_task(self):
        return [i.__str__() for i in self.list_tracks_in_album]

    def __str__(self):
        print(f"Name of group '{self.group}' \nName of album '{self.name}'")
        for s in enumerate(self.get_tracks_for_task(), 1):
            print(f"     {s[0]}. {s[1]}")
        print(f"Общая длительность альбома: {self.get_duration_of_album()} минут.\n")

    def get_duration_of_album(self):
        return sum([i.duration for i in self.list_tracks_in_album])


if __name__ == '__main__':
    album1 = Album("Первый альбом", "Первый исполнитель")
    album1.add_track_in_album(Track("Частушка", 1))
    album1.add_track_in_album(Track("Лирика", 4))
    album1.add_track_in_album(Track("Романс", 3))

    album2 = Album("Другой альбом", "Другой исполнитель")
    album2.add_track_in_album(Track("Баллада", 2))
    album2.add_track_in_album(Track("Менуэт", 5))
    album2.add_track_in_album(Track("Серенада", 5))

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
