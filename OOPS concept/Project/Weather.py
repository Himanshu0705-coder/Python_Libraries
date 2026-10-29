class Weather:
    def __init__(self):

        user_input = input("""How would you like to proceed?
        1. Enter 1 to see the zip_code
        2. enter 2 to see city_name
        3. enter 3 to see country_code""")

        if user_input == "1":
            print("print zip code")

        elif user_input =="2":
            print("print city name")

        else:
            self.country_code()

    def country_code(self):
        input("Enter the zipcode ")
        self.fetch_data()

    

