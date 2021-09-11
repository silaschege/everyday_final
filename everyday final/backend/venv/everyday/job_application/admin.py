from django.contrib import admin

# Register your models here.
from .models import (Applicant,
                    Guarantors,
                    Job_listing,
                    Application_made
                    )



admin.site.register (Applicant)
admin.site.register (Guarantors)
admin.site.register (Job_listing)
admin.site.register (Application_made)