from rest_framework.response import Response
from rest_framework.views import APIView

import json
import requests
from abc import abstractmethod, ABCMeta


class RouteInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_parameters(self, data: dict) -> None:
        pass

    @abstractmethod
    def get_parameters(self) -> dict:
        pass

    @abstractmethod
    def set_response(self, **data: dict) -> None:
        pass

    @abstractmethod
    def get_response(self) -> dict:
        pass

    @abstractmethod
    def send(self, uri: str, method: str = 'GET') -> None:
        pass


class Route(RouteInterface):
    APP_ID = '2750bc42-702e-4cbe-bae5-798f171389e1'
    _parameters = {}
    _response = {}

    def set_parameters(self, data):
        if data:
            self._parameters = data
        else:
            self._parameters = {}

    def get_parameters(self):
        return self._parameters

    def set_response(self, **data):
        self._response = data

    def get_response(self):
        return self._response

    def send(self, uri: str, method: str = 'GET') -> None:
        params = self.get_parameters()
        url = 'http://core.webstktw.beget.tech/api/v0/apps/' + self.APP_ID + uri
        print(url)
        request = requests.request(method=method, url=url, json=params)
        content = json.loads(request.content)
        status_code = request.status_code
        print(content)
        self.set_response(content=content, status_code=status_code)


class BotList(Route, APIView):
    catalog = '/bots/'

    def get(self, request):
        path = self.catalog
        data = request.body
        self.set_parameters(data)
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])

    def post(self, request):
        path = self.catalog
        data = request.body
        self.set_parameters(data)
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])


class BotDetails(Route, APIView):
    catalog = '/bots/'

    def get(self, request, id):
        uri = str(id)
        path = self.catalog + uri
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])

    def post(self, request, id):
        uri = str(id)
        path = self.catalog + uri
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])


class Register(Route, APIView):
    catalog = '/users/'

    def get(self, request):
        data = request.body
        data = json.loads(data)
        self.set_parameters(data)
        path = self.catalog
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])

    def post(self, request):
        data = request.body
        data = json.loads(data)
        self.set_parameters(data)
        path = self.catalog
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])


class Login(Route, APIView):
    catalog = '/users/login/'

    def get(self, request):
        data = request.body
        data = json.loads(data)
        self.set_parameters(data)
        path = self.catalog
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])

    def post(self, request):
        data = request.body
        data = json.loads(data)
        self.set_parameters(data)
        path = self.catalog
        super().send(method=request.method, uri=path)
        response = self.get_response()
        return Response(data=response['content'], status=response['status_code'])
