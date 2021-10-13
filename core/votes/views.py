# views
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import View
# model
from votes.models import votesModel
# form
from votes.forms.postvotesform import VotesForm
# redirect
from django.shortcuts import redirect
# templateview
from django.views.generic import TemplateView





# lists
# class VotesView(ListView):
#     model = votesModel
#     template_name="votes/indexvotes.html"

class UserToUserVotes(ListView):
    model = votesModel
    template_name="votes/uservotes.html"
    paginate_by = 10

    def get_queryset(self):
        return votesModel.objects.filter(user_create=self.request.user)
    



# listapi y detail template para api
class VotesViewApi(TemplateView):
    template_name = "votes/indexvotes.html"
    
class VotesViewApiDetail(TemplateView):
    template_name = "votes/detailvotes.html"



# create post votes
class createVotes(View):
    def get(self,request,*args,**kwargs):
        form=VotesForm()
        context={
            'form':form
        }

        return render(request,'votes/postvotes.html',context)

    def post(self,request,*args,**kwargs):
        if request.method == 'POST':
            loggin_user=request.user
            form=VotesForm(request.POST)
            

            if form.is_valid():
                category=form.cleaned_data['categorys']
                votes=form.save(commit=False)
                votes.user_create=loggin_user
                votes.save()

                for c in category:
                    votes.categorys.add(c)
                votes.save()
                return redirect('mylist')
        form=VotesForm()          
        context={
            'form':form,
            'error':'por favor digite los campos correspondiente'
        }
          
        return render(request,'votes/postvotes.html',context)


    
    