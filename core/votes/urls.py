from django.urls import path,include
from votes.views import VotesViewApi,UserToUserVotes,createVotes,VotesViewApiDetail

urlpatterns  = [
   path('indexvotes/',VotesViewApi.as_view(),name='votes'),
   path('detailvotes/',VotesViewApiDetail.as_view(),name='detail'),

   path('Mylists/',UserToUserVotes.as_view(),name='mylist'),
   path('newvotes/',createVotes.as_view(),name='newvotes'),

   # api
   path('',include('votes.api.urls'))
]
