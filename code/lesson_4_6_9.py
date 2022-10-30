class RetriveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


# здесь объявляйте класс GeneralView
class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        self._check(request)
        method_request = self.__getattribute__(request.get('method').lower())
        return method_request(request)

    def _check(self, request):
        method = request.get('method').upper()
        if method not in self.allowed_methods:
            raise TypeError(f"Метод {request.get['method']} не разрешен.")





class DetailView(RetriveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'POST', )

