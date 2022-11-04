from redis_om import JsonModel
from lib.error_handler import except_handler

class MainService:
    def __init__(self, model: JsonModel, formater = None) -> None:
        self.Model = model
        if not formater:
            self.format_model = lambda model: model.dict() 
        else:
            self.format_model = formater 

    @except_handler
    def get_all(self, limit: int):
        models_found = [self.format_model(self.Model.get(pk)) for pk in self.Model.all_pks()]
        return (models_found[:limit], None)
    
    @except_handler
    def get_by_pk(self, pk: str):
        return (self.format_model(self.Model.get(pk)), None)

    @except_handler
    def delete_by_pk(self, pk: str):
        model = self.Model.get(pk)
        self.Model.delete(pk)
        return (self.format_model(model), None)