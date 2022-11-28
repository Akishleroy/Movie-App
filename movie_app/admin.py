from django.contrib import admin,messages
from .models import Movie,Director,Actor,DressingRoom
from django.db.models import QuerySet
# Register your models here.

# @admin.register(Director)
# class DirectorAdmin(admin.ModelAdmin):
#     list_display=['first_name','last_name']

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoomAdmin(admin.ModelAdmin):
    list_display=['floor','number','actor']





class RatingFilter(admin.SimpleListFilter):
    title="film filter"
    parameter_name="rating filma"
    def lookups(self, request,model_admin):
        return [
            ('<40','Низкий'),
            ('от 40 до 60','средний'),
            ('от 60 до 80','хороший'),
            ('от 80','очень крутой'),
        ]

    def queryset(self,request,queryset:QuerySet):
        if self.value()=='<40':
            return queryset.filter(rating__lt=40)
        if self.value()=='от 40 до 60':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        if self.value()=='от 60 до 80':
            return queryset.filter(rating__gte=60).filter(rating__lte=79)
        if self.value()=='от 80':
            return queryset.filter(rating__gte=80)
      

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields=['name','rating']
    # exclude=['slug']
    filter_horizontal=['actors']
    prepopulated_fields={'slug':('name',)}
    readonly_fields=['year']
    list_display=['name','rating','director','budget','rating_status']
    list_editable=['rating','budget','director']
    ordering=['-rating']
    list_per_page=10
    actions=['set_dollars','set_euros','set_rubles']
    search_fields=['name__startswith','rating']
    list_filter=['name',RatingFilter,'currency']
    @admin.display(ordering='rating',description='status filma')
    def rating_status(self,mov:Movie):
        if mov.rating<50:
            return 'Ochen plohoi film'
        if mov.rating<70:
            return 'plohoi film'
        if mov.rating<=85:
            return 'Horoshyi film'
        return 'topchik'

    @admin.action(description="Установить валюту доллар") 
    def set_dollars(self,request,qs:QuerySet):
        count_updated=qs.update(currency=Movie.DOL)
        self.message_user(
            request,
            f'Было изменено {count_updated} записей',
            messages.ERROR)

    @admin.action(description="Установить валюту евро") 
    def set_euros(self,request,qs:QuerySet):
        count_updated=qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Было изменено {count_updated} записей',
            messages.ERROR)

    @admin.action(description="Установить валюту рубль") 
    def set_rubles(self,request,qs:QuerySet):
        count_updated=qs.update(currency=Movie.RUB)
        self.message_user(
            request,
            f'Было изменено {count_updated} записей',
            messages.ERROR)
# admin.site.register(Movie,MovieAdmin)
