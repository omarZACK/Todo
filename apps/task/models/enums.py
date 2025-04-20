from Helpers.structure.enums import ChoiceEnum

# Create your enums here.

class Priority(ChoiceEnum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class Status(ChoiceEnum):
    TODO =  'todo'
    IN_PROGRESS = 'in progress'
    DONE = 'done'
