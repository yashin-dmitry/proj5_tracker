from rest_framework.exceptions import ValidationError

def validate_habit(data):
    if data.get('related_habit') and data.get('reward'):
        raise ValidationError("Cannot have both related habit and reward.")
    if data.get('execution_time') > 120:
        raise ValidationError("Execution time cannot exceed 120 seconds.")
    if data.get('related_habit') and not data['related_habit'].is_pleasant:
        raise ValidationError("Related habit must be a pleasant habit.")
    if data.get('is_pleasant') and (data.get('reward') or
                                    data.get('related_habit')):
        raise (ValidationError
               ("Pleasant habit cannot have reward or related habit."))
    if data.get('periodicity') < 1 or data.get('periodicity') > 7:
        raise ValidationError("Periodicity must be between 1 and 7 days.")
