from jinja2 import Template
from tasks import load_gift_list
import sys


_, username, password, cal_url = sys.argv

outputliszt = load_gift_list(username, password, cal_url)

#username = sys.argv[1] print(sys.argv)

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


