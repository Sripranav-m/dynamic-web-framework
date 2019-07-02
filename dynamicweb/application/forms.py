from django import forms
from .models import content_for_Menu
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor.widgets import CKEditorWidget

class contentform(forms.Form):
    content=RichTextUploadingFormField()
