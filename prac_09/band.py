class Band:
    def __init__(self, band_name="", musicians=""):
        self.band_name = band_name
        self.musicians = musicians

    def add(self, musician):
        self.musicians.append(musician)
    def play(self):
        print(f"{self.band_name} (Band)")

