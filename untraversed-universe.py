import os

from app import create_app


env = os.environ.get("APP_STATE", "default")
application = create_app(config_name=env)


@application.context_processor
def utility_processor():
    def link_to(obj):
        try:
            return obj.link_to
        except Exception:
            raise NotImplementedError("This object link_to is probably not implemented")

    from app.models import models_dict

    return dict(link_to=link_to, **models_dict)


# @application.before_first_request
# def fill_database():
#     # from app.models.qualities import Quality
#     from app.models import Quality, Ship

#     # print("Doing this only one time! ")
# Quality.fill_database()
#     # Ship.fill_database()
