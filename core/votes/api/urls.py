from django.urls import path
from votes.api.views import listVotesUser,retrieveVotesUser,postviewsyes,postviewsno,CloseVote

urlpatterns = [
   path('listApi/',listVotesUser.as_view()),
   path('detail/<int:pk>',retrieveVotesUser.as_view()),
   # votar si o no
   path('yes/<int:pk>',postviewsyes.as_view()),
   path('no/<int:pk>',postviewsno.as_view()),
   # update close
    path('closed/<int:pk>',CloseVote.as_view())
]