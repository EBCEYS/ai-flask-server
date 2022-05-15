import json


class ActionResponse(object):
    def __init__(self, answer, value):
        """Constructor"""
        if answer == "OK":
            self.Answer = answer
        else:
            self.Answer = "ERROR"
        self.Value = value

    def ToJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


#Answer types:
#OK
#ERROR
#ERROR_WRONG_ALGORITHM
#ERROR_WRONG_DATASET
#ERROR_WRONG_REQUEST_ID


