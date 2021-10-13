# views
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.views import APIView
# response y serializers
from rest_framework.response import Response
from votes.api.serializers import votesSerializers,closeSerializer
# model
from votes.models import  votesModel
# error
from django.http import Http404
# pagination
from rest_framework.pagination import PageNumberPagination
# status
from rest_framework import status

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

# list y detail api
class listVotesUser(ListAPIView):    
        serializer_class = votesSerializers
        queryset = votesModel.objects.filter(isclosed=False)
        pagination_class = StandardResultsSetPagination
        

class retrieveVotesUser(RetrieveAPIView):    
        serializer_class = votesSerializers
        queryset = votesModel.objects.all()

        def retrieve(self, request, *args, **kwargs):
                instance = self.get_object()
                serializer = self.get_serializer(instance)
                if instance.isclosed == True:
                        return Response("isclosed",status=203)
                else:
                        return Response(serializer.data)


# votaciones view
class postviewsyes(APIView):
        def post(self, request,pk):
                post=votesModel.objects.get(pk=pk)
               
               
                is_not=False
                for no in post.No_opine.all():
                        if no == request.user:
                                is_not=True 
                                break

                if is_not:
                        post.No_opine.remove(request.user)


                is_yes=False
                for yes in post.yes_opine.all():
                        if yes == request.user:
                                is_yes=True 
                                break

                if not is_yes:
                        post.yes_opine.add(request.user)
                        
                if  is_yes:
                        post.yes_opine.remove(request.user)
                        
                return Response("listo")

class postviewsno(APIView):
        def post(self, request,pk):
                post=votesModel.objects.get(pk=pk)

                is_yes=False
                for yes in post.yes_opine.all():
                        if yes == request.user:
                                is_yes=True 
                                break

                if is_yes:
                        post.yes_opine.remove(request.user)


                is_not=False
                for no in post.No_opine.all():
                        if no == request.user:
                                is_not=True 
                                break

                if not is_not:
                        post.No_opine.add(request.user)
                
                if  is_not:
                        post.No_opine.remove(request.user)
                
                return Response("listo")

# close and open votaciones
class CloseVote(APIView):

        def get_object(self, pk):
                try:
                        return votesModel.objects.get(pk=pk)
                except votesModel.DoesNotExist:
                        raise Http404

        def put(self, request, pk):
                postid=self.get_object(pk)
               
                isclosed=False
                if postid.isclosed == True:
                        isclosed=True
                else:
                        isclosed=False
                        
                if isclosed == True:
                      serializer = closeSerializer(postid, {"isclosed":"False"})
                      if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                else:
                        serializer = closeSerializer(postid, {"isclosed":"True"})
                        if serializer.is_valid():                              
                                serializer.save()
                                return Response(serializer.data)

                return Response(serializer.errors)


    
                                

                

        

    