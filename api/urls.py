from rest_framework.routers import SimpleRouter
from api.API.resources import PageView


app_name = "api"

router = SimpleRouter()
router.register(r"pages", PageView)

urlpatterns = router.urls
