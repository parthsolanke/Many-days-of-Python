from bs4 import BeautifulSoup

with open(r"BeautifulSoup for Webscrapping\website.html", encoding="utf8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(f"\nTitle of the page with tag: {soup.title}")
# print(f"\nTitle of the page without tag: {soup.title.string}")
# print(f"\nThe whole page as HTML doc: \n{soup.prettify()}")

# getting the heading with id="name"
heading = soup.find(name="h1", id="name") # find() returns the first found item
print(f"\nHeading with id='name': {heading}")

# getting the heading with class="heading"
heading = soup.find(name="h3", class_="heading")
print(f"\nHeading with class='heading': {heading}")

# grabbing text from tags
print(f"\nHeading with id='name' text: {heading.getText()}")
print(f"\nHeading with id='name' text: {heading.string}")
# getting the name of the tag
print(f"\nHeading with id='name' name: {heading.name}")
# getting the value of an attribute of the tag
print(f"\nHeading with id='name' attribute: {heading.get('class')}")

# get all the anchor tags
all_anchor_tags = soup.find_all(name="a") # find_all() returns a list of all found items
print(f"\nAll anchor tags: {all_anchor_tags}")

# getting the text from the anchor tags
print("\nAll anchor tags text:")
for tag in all_anchor_tags:
    print(tag.getText())

# getting the href attribute from the anchor tags
print("\nAll anchor tags href attribute:")
for tag in all_anchor_tags:
    print(tag.get("href"))
    
# getting elements by CSS selectors
name = soup.select_one(selector="#name")
print(f"\nName: {name.getText()}")
company_url = soup.select_one(selector="p a")
print(f"\nCompany URL: {company_url}")

# getting elements by CSS selectors
print(f"\nAll anchor tags: {soup.select(selector='a')}")