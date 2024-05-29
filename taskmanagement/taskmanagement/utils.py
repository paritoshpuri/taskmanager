from rest_framework import status


class BaseService:
    def __init__(self):
        self.response = {"code": "", "data": {}, "errors": {}, "message": ""}

    def set_response(
        self, code=status.HTTP_200_OK, data={}, errors={}, message="Success"
    ):
        self.response = {
            "code": code,
            "data": data,
            "errors": errors,
            "message": message,
        }
        return self.response
