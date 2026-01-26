class Japan:

    def capital(self):

        print("Tokyo")

    def language(self):

        print("Japanese")

    def country_type(self):

        print("Developed Country")

class Brazil:

    def capital(self):

        print("Brasília")

    def language(self):

        print("Portuguese")

    def country_type(self):

        print("Developing Country")


jp = Japan()
br = Brazil()

for country in (jp,br):
    country.capital()
    country.language()
    country.country_type()