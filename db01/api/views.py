from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, BusService, HotelService
from .serializers import UserSerializer, BusSerializer, HotelSerializer
from rest_framework import status

class UserList(APIView):

    def get(self, request, format = None):
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

class GetUser(APIView):

    def get_object(self, email):
        return User.objects.filter(email = email)

    def get(self, request, format = None):
        user = self.get_object(request.data.get('email'))
        if not user:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(user, many = True)
            return Response(serializer.data)

class InsertUser(APIView):

    def get_object(self, email):
        return User.objects.filter(email = email)

    def post(self, request, format = None):
        user = self.get_object(request.data.get('email'))
        if not user:
            try:
                new_user = User(email = request.data.get('email'),
                                password = request.data.get('password'),
                                token = request.data.get('token'),
                                type = request.data.get('type'))

                new_user.full_clean()
                new_user.save()
                return Response(status = status.HTTP_201_CREATED)
            except Exception as e:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class UpdateUser(APIView):

    def get_object(self, email):
        return User.objects.filter(email = email)

    def post(self, request, format = None):
        user = self.get_object(request.data.get('email'))
        if not user:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            user = user[0]
            try:
                if request.data.get('token') != None:
                    user.token = request.data.get('token')
                if request.data.get('password') != None:
                    user.password = request.data.get('password')
                if request.data.get('type') != None:
                    user.type = request.data.get('type')
                user.full_clean()
                user.save()
                return Response(status = status.HTTP_200_OK)
            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

class BusServiceList(APIView):

    def get(self, request, format = None):
        services = BusService.objects.all()
        serializer = BusSerializer(services, many = True)
        return Response(serializer.data)

class BusServiceListEmail(APIView):

    def post(self, request, format = None):
        services = BusService.objects.filter(provider__contains = list([request.data.get('email')]))
        serializer = BusSerializer(services, many = True)
        return Response(serializer.data)

class NewBusService(APIView):

    def get_object(self, id):
        return BusService.objects.filter(id = id)

    def post(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            try:
                new_service = BusService(   id = request.data.get('id'),
                                            name = request.data.get('name'),
                                            provider = list([request.data.get('provider')]))
                new_service.full_clean()
                new_service.save()
                return Response(status = status.HTTP_201_CREATED)
            except Exception as e:
                print('EXCEPTION THROW')
                print(e)
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class UpdateBusService(APIView):

    def get_object(self, id):
        return BusService.objects.filter(id = id)

    def post(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                if request.data.get('provider') != None and request.data.get('provider_code') == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
                if request.data.get('route') != None and request.data.get('route_code') == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
                if request.data.get('timing') != None and request.data.get('timing_code') == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
                if request.data.get('boarding_point') != None and request.data.get('boarding_code') == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)

                service = service[0]
                if request.data.get('name') != None:
                    service.name = request.data.get('name')
                if request.data.get('price') != None:
                    service.price = int(request.data.get('price'))
                if request.data.get('bus_number') != None:
                    service.bus_number = request.data.get('bus_number')
                if request.data.get('seats') != None:
                    service.seats = request.data.get('seats')
                if request.data.get('is_ready') != None:
                    service.is_ready = request.data.get('is_ready')
                if request.data.get('provider') != None and request.data.get('provider_code') == 'ADD':
                    service.provider.append(request.data.get('provider'))
                if request.data.get('route') != None and request.data.get('route_code') == 'ADD':
                    service.route.append(request.data.get('route'))
                if request.data.get('timing') != None and request.data.get('timing_code') == 'ADD':
                    service.timing.append(request.data.get('timing'))
                if request.data.get('boarding_point') != None and request.data.get('boarding_code') == 'ADD':
                    service.boarding_point.append(request.data.get('boarding_point'))
                if request.data.get('provider') != None and request.data.get('provider_code') == 'REMOVE':
                    service.provider.remove(request.data.get('provider'))
                if request.data.get('route') != None and request.data.get('route_code') == 'REMOVE':
                    service.route.remove(service.route[int(request.data.get('route'))])
                if request.data.get('timing') != None and request.data.get('timing_code') == 'REMOVE':
                    service.timing.remove(service.timing[int(request.data.get('timing'))])
                if request.data.get('boarding_point') != None and request.data.get('boarding_code') == 'REMOVE':
                    service.boarding_point.remove(service.boarding_point[int(request.data.get('boarding_point'))])
                service.full_clean()
                service.save()
                return Response(status = status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(status = status.HTTP_400_BAD_REQUEST)

class GetBusService(APIView):

    def get_object(self, id):
        return BusService.objects.filter(id = id)

    def get(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = BusSerializer(service, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

class DeleteBusService(APIView):

    def get_object(self, id):
        return BusService.objects.filter(id = id)

    def post(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            service = service[0]
            service.delete()
            return Response(status = status.HTTP_200_OK)

class HotelServiceList(APIView):

    def get(self, request, format = None):
        services = HotelService.objects.all()
        serializer = HotelSerializer(services, many = True)
        return Response(serializer.data)

class NewHotelService(APIView):

    def get_object(self, id):
        return HotelService.objects.filter(id = id)

    def post(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            try:
                new_service = HotelService( id = request.data.get('id'),
                                            name = request.data.get('name'),
                                            provider = list([request.data.get('provider')]))
                new_service.full_clean()
                new_service.save()
                return Response(status = status.HTTP_201_CREATED)
            except Exception as e:
                print('EXCEPTION THROW')
                print(e)
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_400_BAD_REQUEST)

class UpdateHotelService(APIView):

    def get_object(self, id):
        return HotelService.objects.filter(id = id)

    def post(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            try:
                if request.data.get('provider') != None and request.data.get('provider_code') == None:
                    return Response(status = status.HTTP_400_BAD_REQUEST)

                service = service[0]
                if request.data.get('name') != None:
                    service.name = request.data.get('name')
                if request.data.get('price') != None:
                    service.price = int(request.data.get('price'))
                if request.data.get('city') != None:
                    service.city = request.data.get('city')
                if request.data.get('area') != None:
                    service.area = request.data.get('area')
                if request.data.get('address') != None:
                    service.address = request.data.get('address')
                if request.data.get('rooms') != None:
                    service.rooms = request.data.get('rooms')
                if request.data.get('is_ready') != None:
                    service.is_ready = request.data.get('is_ready')
                if request.data.get('check_in') != None:
                    service.check_in = request.data.get('check_in')
                if request.data.get('check_out') != None:
                    service.check_out = request.data.get('check_out')
                if request.data.get('provider') != None and request.data.get('provider_code') == 'ADD':
                    service.provider.append(request.data.get('provider'))
                if request.data.get('provider') != None and request.data.get('provider_code') == 'REMOVE':
                    service.provider.remove(request.data.get('provider'))

                service.full_clean()
                service.save()
                return Response(status = status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(status = status.HTTP_400_BAD_REQUEST)

class GetHotelService(APIView):

    def get_object(self, id):
        return HotelService.objects.filter(id = id)

    def get(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            serializer = HotelSerializer(service, many = True)
            return Response(serializer.data, status = status.HTTP_200_OK)

class HotelServiceListEmail(APIView):

    def post(self, request, format = None):
        services = HotelService.objects.filter(provider__contains = list([request.data.get('email')]))
        serializer = HotelSerializer(services, many = True)
        return Response(serializer.data)

class DeleteHotelService(APIView):

    def get_object(self, id):
        return HotelService.objects.filter(id = id)

    def post(self, request, format = None):
        service = self.get_object(request.data.get('id'))
        if not service:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            service = service[0]
            service.delete()
            return Response(status = status.HTTP_200_OK)
