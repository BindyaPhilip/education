# Import Django's admin module for admin interface management
from django.contrib import admin
# Import format_html for clickable links
from django.utils.html import format_html
# Import Count for analytics
from django.db.models import Count

# Import the model
from .models import EducationResource

# Register the model with the admin
@admin.register(EducationResource)
class EducationalResourceAdmin(admin.ModelAdmin):
    # Fields to show in the list view
    list_display = ('title', 'disease', 'resource_type', 'url_link', 'created_at')
    
    # Set 'title' as the clickable link to avoid list_editable conflicts
    list_display_links = ('title',)
    
    # Allow inline editing of non-link fields
    list_editable = ('disease', 'resource_type')
    
    # Filter by disease and resource type
    list_filter = ('disease', 'resource_type')
    
    # Search by title and description
    search_fields = ('title', 'description')
    
    # Display URL as a clickable link
    def url_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.url, obj.url)
    # Set column header; suppress Mypy error
    url_link.short_description = 'Resource URL'  # type: ignore[attr-defined]
    
    # Bulk action to update disease
    def mark_as_common_rust(self, request, queryset):
        queryset.update(disease='common_rust')
    mark_as_common_rust.short_description = "Mark selected as Common Rust"  # type: ignore[attr-defined]
    actions = ['mark_as_common_rust']
    
    # Compute resource counts per disease
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        self.disease_counts = qs.values('disease').annotate(count=Count('id'))
        return qs
    
    # Show counts in the admin
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['disease_counts'] = getattr(self, 'disease_counts', [])
        return super().changelist_view(request, extra_context=extra_context)