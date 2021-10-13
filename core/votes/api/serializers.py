
from rest_framework import serializers
from votes.models import votesModel,category


class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model=category
        fields=('id','type')
        read_only = ('id')


# yes_opine y no es como los likes y dislikes
# variables creadas para contar cuantos hay 
class votesSerializers(serializers.ModelSerializer):
    categorys=categorySerializer(many=True,read_only=True)
    total_yes=serializers.SerializerMethodField('count_yes')
    total_no=serializers.SerializerMethodField('count_no')
    # si el usuario dio yes o no que me devuelva un none o un true
    user_opine_yes=serializers.SerializerMethodField('user_yes')
    user_opine_no=serializers.SerializerMethodField('user_no')

    def count_yes(self,obj):     
        return obj.yes_opine.count()

    def count_no(self,obj):
        return obj.No_opine.count()


    def user_yes(self,obj):
        # asi obtengo el request para llamar al usuario registrado,por default serializer no lo tiene
        request = self.context.get("request") 
         # obtengo el post y recorro para obtener el user y despues otro ciclo para sacarlo del queryset
        results = votesModel.objects.filter(id=obj.id)
        for vote in results:
            yes_vote=vote.yes_opine.all()
            for yes in yes_vote:
                
                if yes == request.user:
                    return True
                else:
                    return None
        
    def user_no(self,obj):
        # asi obtengo el request para llamar al usuario registrado,por default serializer no lo tiene
        request = self.context.get("request") 
        # obtengo el post y recorro para obtener el user y despues otro ciclo para sacarlo del queryset
        results = votesModel.objects.filter(id=obj.id)
        for vote in results:
            no_vote=vote.No_opine.all()
            for no in no_vote:     
                if no == request.user:
                    return True
                else:
                    return None


    class Meta:
        model=votesModel
        fields=('id','total_yes','total_no','user_opine_yes',
                'user_opine_no','title','body','categorys','user_create')
        read_only = ('id')


class closeSerializer(serializers.ModelSerializer):
    class Meta:
        model=votesModel
        fields=('isclosed',)
        

