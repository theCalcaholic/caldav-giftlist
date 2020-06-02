from jinja2 import Template
from tasks import load_gift_list

username = "caldav-wishlist"
password = "secret"
# url = "https://cloud.knoeppler.org/remote.php/dav"
cal_url = "https://cloud.knoeppler.org/remote.php/dav/calendars/caldav-wishlist/wedding/"

outputliszt = load_gift_list(username, password, cal_url)



# read template
wish_haendel = open("templates/wishlist.html", "r")
template_text = wish_haendel.read()
wish_haendel.close()

# render template
template = Template(template_text)
wishprint = template.render(wishlist = outputliszt)

# save output
print(wishprint)
output_haendel = open("output/wishlist.html", "w")
output_haendel.write(wishprint)
output_haendel.close()


