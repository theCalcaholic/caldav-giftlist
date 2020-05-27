from jinja2 import Template

todos = [
    "Geschenk 1",
    "Geschenk 2",
    "Geschenk 3"
]

# read template
wish_handle = open("templates/wishlist.html", "r")
template_text = wish_handle.read()
wish_handle.close()

# render template
template = Template(template_text)
wishprint = template.render(wishlist = todos)

# save output
print(wishprint)
output_handle = open("output/wishlist.html", "w")
output_handle.write(wishprint)
output_handle.close()
