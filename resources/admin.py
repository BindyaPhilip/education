# Import Django's admin module to manage models via the admin interface
from django.contrib import admin
# Import format_html to create clickable links in the admin
from django.utils.html import format_html
# Import Count for analytics
from django.db.models import Count

# Import the EducationalResource model from the current app
from .models import EducationResource

# Register the model with the admin site
@admin.register(EducationResource)
class EducationalResourceAdmin(admin.ModelAdmin):
    # Display these fields in the list view for a quick overview
    list_display = ('title', 'disease', 'resource_type', 'url_link', 'created_at')
    
    # Allow filtering by disease and resource type in the sidebar
    list_filter = ('disease', 'resource_type')
    # This makes 'title' the clickable link to the edit page
    list_display_links = ('title',)
    # Enable searching by title and description for easy lookup
    search_fields = ('title', 'description')
    
    # Allow inline editing of title and URL for convenience
    list_editable = ('disease','resource_type')
    
    # Custom method to display URL as a clickable link
    def url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    url_link.short_description = 'Resource URL' # type: ignore[attr-defined]
    
    # Custom action to bulk-update disease
    def mark_as_common_rust(self, request, queryset):
        queryset.update(disease='common_rust')
    mark_as_common_rust.short_description = "Mark selected as Common Rust" # type: ignore[attr-defined]
    actions = ['mark_as_common_rust']
    
    # Add analytics for disease counts
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        self.disease_counts = qs.values('disease').annotate(count=Count('id'))
        return qs
    
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['disease_counts'] = getattr(self, 'disease_counts', [])
        return super().changelist_view(request, extra_context=extra_context)