from Helpers.structure.enums import ChoiceEnum

# Create your enums here.


class NotificationMethod(ChoiceEnum):
    EMAIL = 'email'
    PUSH = 'push'