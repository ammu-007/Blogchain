from django import forms
from .models import BlogPost


class BlogPostModelForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "slug", "image", "content", "published_date"]

    def clean_title(self, *args, **kwargs):
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get("title")
        qs = BlogPost.objects.filter(title__iexact=title)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been taken!")
        return title