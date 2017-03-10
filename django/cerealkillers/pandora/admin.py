from django.contrib import admin
from .models import Username, ResponsesModel, SearchRestaurantsModel, PickRestaurantsModel, RecommendationModel, RejectionModel, RestartModel

admin.site.register(Username)
admin.site.register(ResponsesModel)
admin.site.register(SearchRestaurantsModel)
#admin.site.register(DietRestrictions)
#admin.site.register(Distance)
#admin.site.register(Address)
#admin.site.register(Time)
#admin.site.register(Hurry)
