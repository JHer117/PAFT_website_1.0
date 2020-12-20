from config import app
from controller_functions import landing, about_page, packages_page

app.add_url_rule("/", view_func=landing)
app.add_url_rule("/about.html", view_func=about_page)
app.add_url_rule("/packages.html", view_func=packages_page)