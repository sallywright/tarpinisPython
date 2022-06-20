# Sukurkite klasę "Movie", kuri gebės sukurti objektus 3 savybėm ir 1 metodu. 
# Naudojant šią klasę sukurkite bent du skirtingus objektus.

# Savybės:
# title: string
# director: string
# budget: number

# Metodas: 
# was_expensive() - jeigu filmo "budget" yra daugiau nei 100 000 000 mln USD, tada grąžins True, kitu atveju False.

class Movie:
    def __init__(self, title:str, director:str, budget:int) -> None:
        self.title = title
        self.director = director
        self.budget = budget

    def was_expensive(self):
        expensive = False

        if self.budget > 100000000:
            expensive = True
        
        return expensive


first_movie = Movie("Split", "Some Director", 1000000000000)
second_movie = Movie("Split 2", "Some Other Director", 2000000)
third_movie = Movie("Split 3", "Different Director", 400000)

print(first_movie.was_expensive())
print(second_movie.was_expensive())
print(third_movie.was_expensive())