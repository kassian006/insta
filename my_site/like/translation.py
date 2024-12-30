from .models import Post
from modeltranslation.translator import TranslationOptions,register

@register(Post)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)