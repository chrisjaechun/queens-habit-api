from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token

from ..models.experience import Experience
from ..serializers import UserSerializer, ExperienceSerializer

class ExperiencesAll(generics.ListCreateAPIView):
    def get(self, request):
        """Index all request"""
        experiences = Experience.objects.all()
        data = ExperienceSerializer(experiences, many=True).data
        return Response(data)

class Experiences(generics.ListCreateAPIView):
    def get(self, request):
        """Index request"""
        experiences = Experience.objects.all()
        data = ExperienceSerializer(experiences, many=True).data
        return Response(data)

    serializer_class = ExperienceSerializer
    def post(self, request):
        """Create request"""
        request.data['experience']['owner'] = request.user.id
        experience = ExperienceSerializer(data=request.data['experience'])
        if experience.is_valid():
            exp = experience.save()
            return Response(experience.data, status=status.HTTP_201_CREATED)
        else:
            return Response(experience.errors, status=status.HTTP_400_BAD_REQUEST)

class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, pk):
        """Show request"""
        experience = get_object_or_404(Experience, pk=pk)

        if not request.user.id == experience.owner.id:
            raise PermissionDenied('Get your own experiences!')
        
        serializer = ExperienceSerializer(experience)
        data = serializer.data
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        experience = get_object_or_404(Experience, pk=pk)

        if not request.user.id == experience.owner.id:
            raise PermissionDenied('Whoa. Stop trying to delete someone else\'s experience')

        experience.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        if "owner" in request.data['experience']:
            del request.data['experience']['owner']
        experience = get_object_or_404(Experience, pk=pk)
        if not request.user.id == experience.owner.id:
            raise PermissionDenied('Get your own experience!')

        request.data['experience']['owner'] = request.user.id
        es = ExperienceSerializer(experience, data=request.data['experience'])

        if es.is_valid():
            es.save()
            return Response(es.data)
        return Response(es.errors, status=status.HTTP_400_BAD_REQUEST)
