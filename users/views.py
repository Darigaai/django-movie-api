from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi





class RegisterView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Регистрация пользователя",
        operation_description="Создаёт нового пользователя и возвращает JWT refresh/access токены.",
        request_body=RegisterSerializer,
        responses={
            201: openapi.Response(
                description="Пользователь успешно зарегистрирован",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'refresh': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Refresh token'
                        ),
                        'access': openapi.Schema(
                            type=openapi.TYPE_STRING,
                            description='Access token'
                        ),
                        'user': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'email': openapi.Schema(type=openapi.TYPE_STRING),
                                'username': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    }
                )
            ),
            400: "Ошибка валидации"
        }
    )

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())
    

