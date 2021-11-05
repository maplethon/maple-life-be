from datetime import datetime
from flask.wrappers import Response
import jsonpickle


class ApiResponse:
    class Common:
        def __init__(self, message):
            self.timestamp = datetime.now().strftime("%Y%m%d%H%M")
            self.message = message

    def __init__(self, message, data=None):
        self.common = self.Common(message)
        self.data = data

    def __to_json(self):
        return jsonpickle.encode(self, unpicklable=False)

    @classmethod
    def ok(cls, data=None):
        return Response(cls("success", data).__to_json(), mimetype="application/json")

    @classmethod
    def no_content(cls):
        return Response(
            cls("success").__to_json(), mimetype="application/json", status=204
        )

    @classmethod
    def bad_request(cls, message):
        return Response(
            cls(message).__to_json(), mimetype="application/json", status=400
        )

    @classmethod
    def not_found(cls, message):
        return Response(
            cls("not found").__to_json(), mimetype="application/json", status=404
        )

    @classmethod
    def internal_error(cls):
        return Response(
            cls("internal server error").__to_json(),
            mimetype="application/json",
            status=500,
        )
