from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login(request):
    return Response({})

@api_view(['POST'])
def singup(request):
    return Response({})

@api_view(['GET'])
def test_token(request):
    return Response({})