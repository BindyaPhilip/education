from django.db import models
import uuid
# Create your models here.
class EducationResource(models.Model):

    #define uuid as the primary key
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # choices
    DISEASE = [('common_rust','Common Rust'),('healthy','Healthy'),('other_disease','Other disease')]
    RESOURCE_TYPE = [('article','Article'),('video','Video')] 
    # columns
    title = models.CharField(max_length= 250)
    description = models.TextField(blank=True)
    url = models.CharField(max_length=250)
    disease = models.CharField(max_length=20,choices= DISEASE )
    resource_type = models.CharField(max_length=20,choices= RESOURCE_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title