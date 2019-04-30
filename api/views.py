from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.queue import Family
"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""
class ContactsView(APIView):
    def get(self, request, member_id=None):
        return Response("ok", status=status.HTTP_200_OK)

    def post(self, request):
        return Response("ok", status=status.HTTP_200_OK)

    def put(self, request):
        return Response("ok", status=status.HTTP_200_OK)

    def delete(self, request, contact_id):
        return Response("ok", status=status.HTTP_200_OK)
