class Steuer:
    def __init__(self, anteil):
        self.anteil = anteil

    def __call__(self, betrag):
        return self.anteil * betrag


mehrwertsteuer = Steuer(0.19)
print(mehrwertsteuer(1000))
        
