from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError
from api.family_datastructure import Family
import json

# initialize a 'Doe' family
family = Family(last_name='Doe')

"""
The MembersView will contain the logic on how to:
 GET, POST, PUT or delete family members
"""
class MembersView(APIView):
    def get(self, request, member_id=None):
        if(member_id == None):
            return Response(family.get_all_members(), status=status.HTTP_200_OK)
        else:
            member = family.get_member(member_id)
            if member == None:
                raise Http404
            else:
                return Response(member, status=status.HTTP_200_OK)

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        result = family.add_member(json.loads(body_unicode))
        return Response(result, status=status.HTTP_200_OK)

    def put(self, request, member_id=None):
        if(member_id == None):
            raise ValidationError("You must specify a member_id")
            return Response("You must specify a member_id", status=status.HTTP_400_BAD_REQUEST)

        member = family.get_member(member_id)
        if member == None:
            raise Http404

        body_unicode = request.body.decode('utf-8')
        member = json.loads(body_unicode)
        result = family.update_member(member_id, member)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, member_id=None):
        if(member_id == None):
            raise ValidationError("You must specify a member_id")
            return Response("You must specify a member_id", status=status.HTTP_400_BAD_REQUEST)
        
        member = family.get_member(member_id)
        if member == None:
            raise Http404

        family.delete_member(member_id)
        return Response({ "status": "ok" }, status=status.HTTP_200_OK)