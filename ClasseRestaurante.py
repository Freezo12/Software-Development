class RestauranteOriginal:
    def __init__(self, name, tipocozinha, pratodochef, rendamensal):
        self.name = name
        self.tipocozinha = tipocozinha
        self.__pratodochef = pratodochef
        self.__rendamensal = rendamensal

    def my_restaurante_print(self):
        print(f"O nome do meu restaurante: {self.name}")
        print(f"O tipo do restaurante: {self.tipocozinha}")
        print(f"O prato do chef: {self.__pratodochef}")
        print(f"A renda mensal do restaurante: R${self.__rendamensal:}")

    def get_pratodochef(self):
        return self.__pratodochef

    def get_rendamensal(self):
        return self.__rendamensal

    def set_pratodochef(self, dia):
        if dia == "domingo":  
            self.__pratodochef = "Tagliatelle al Ragù"
        else:
            print("Para o especial do chef venha aos domingos")

    def set_rendamensal(self, valor):
        if valor >= 0:
            self.__rendamensal = valor
        else:
            print("Receita do restaurante não pode ser negativa.")


rest1 = RestauranteOriginal("MamaMia", "Italiana", "Lasanha à Bolonhesa", 72000)


rest1.my_restaurante_print()


rest1.set_pratodochef("domingo")
print("após mudar o prato do chef no domingo:")
rest1.my_restaurante_print()
