class Gene:

    def __init__(self, percents):
        self.__percents = percents

    def get_percents(self):
        return self.__percents

    def set_percents(self, percents):
        self.__percents = percents

    def __str__(self):
        string = "Percents: ["

        for i in range(len(self.__percents)):
            string += str(self.__percents[i])
            if i < len(self.__percents) - 1:
                string += ", "

        string += "]"
        return string

    def copy(self):
        return Gene(self.__percents.copy())
