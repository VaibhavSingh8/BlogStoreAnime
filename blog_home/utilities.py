from django.utils.text import slugify
#importing string and random for generating random strings
import random
import string
# using random.choices()
# generating random strings 
def gen_random_string(N):
    res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return res

def generate_slug(text):
    new_slug = slugify(text)
    #import Blog_pot here to escape from lazy model import or circular imports
    from blog_home.models import Blog_post
    # Check slug value, if already present generate new_slug
    if Blog_post.objects.filter(slug=new_slug).first():
        return generate_slug(text + gen_random_string(5))
    return new_slug 