from service.GeneticAlgorithmService import GeneticAlgorithmService


class PrincipalController:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, configuration):
        try:

            print(configuration)

            ag_service = GeneticAlgorithmService(configuration, self.view)
            ag_service.start()

            # save the model
            # self.model = configuration
            # self.model.save()

            # show a success message
            # self.view.show_success(f'The email {email} saved!')

        except ValueError as error:
            # show an error message
            # self.view.show_error(error)
            print(error)
