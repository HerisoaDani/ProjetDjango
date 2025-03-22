from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, CategorieViewSet, ObjectifFinancierViewSet, RecommandationViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'categories', CategorieViewSet)
router.register(r'objectifs', ObjectifFinancierViewSet)
router.register(r'recommandations', RecommandationViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
