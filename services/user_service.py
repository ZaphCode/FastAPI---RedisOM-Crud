from lib.error_handler import except_handler
from .main_service import MainService
from schemas.user_schema import UserSch
from schemas.bio_schema import BioSch
from database.user_model import Bio

class UserService(MainService):
    def __init__(self, model) -> None:
        def custom_formater(user):
            user_dict = user.dict()
            del user_dict["password"]
            return user_dict
        super().__init__(model, custom_formater)

    @except_handler
    def create_new(self, user: UserSch):
        user_with_that_credentials = self.Model.find( 
                (self.Model.username == user.username) | 
                (self.Model.email == user.email)
            ).all()
        if user_with_that_credentials:
            raise Exception("Credentials Taken")
        new_user = self.Model(
            username=user.username,
            email=user.email,
            password=user.password + "SOME-HASH",
            age=user.age
        )
        new_user.save()
        return (self.format_model(new_user), None)

    @except_handler
    def update_bio(self, pk: str, bio: BioSch):
        user = self.Model.get(pk)
        user.bio = Bio(
            hobies = bio.hobies,
            job = bio.job,
            single = bio.single,
            city = bio.city,
        )
        user.save()
        return (self.format_model(user), None)

    @except_handler
    def search(self, search: str, limit: int = 10):
        users = self.Model.find(
            (self.Model.username % f'{search}*') | 
            (self.Model.email % f'{search}*')
            ).all(batch_size=limit)
        return ([self.format_model(user) for user in users], None)