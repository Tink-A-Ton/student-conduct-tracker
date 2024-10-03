# blue prints are imported
# explicitly instead of using *
# from .user import user_views
from App.views.index import index_views
from App.views.auth import auth

# from .admin import setup_admin


views = [index_views, auth]
# blueprints must be added to this list
