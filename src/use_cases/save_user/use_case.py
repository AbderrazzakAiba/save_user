class SaveUserUseCase:
    def __init__(self, repository, presenter):
        self.presenter = presenter

    def execute(self, command):
        self.presenter.present(None)
