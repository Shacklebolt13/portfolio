from django.contrib import admin

from .models import Field, FieldValue, Portfolio


class FieldValueInline(admin.TabularInline):
    model = FieldValue
    extra = 0


class FieldInline(admin.TabularInline):
    model = Field
    extra = 0


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]


@admin.register(FieldValue)
class FieldValueAdmin(admin.ModelAdmin):
    inlines = [FieldValueInline]
