from django.contrib import admin
from .models import Username, ResponsesModel, SearchRestaurantsModel, PickRestaurantsModel, RecommendationModel, RejectionModel

admin.site.register(Username)
admin.site.register(ResponsesModel)
admin.site.register(SearchRestaurantsModel)
admin.site.register(PickRestaurantsModel)
admin.site.register(RecommendationModel)
admin.site.register(RejectionModel)

