from django.contrib import admin
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope
from django import forms


class ScopeInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                main_count += 1

        if main_count != 1:
            raise ValidationError('Основным может быть\
                                  только один раздел.'
                                  )

        super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = ScopeInlineFormset
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    pass
