from django.contrib import admin
from .models import Candidate, Position



# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position','about','year','manifesto','achievements','party','course','total_vote')
    list_filter = ('position',) 
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)

# admin.site.register(Profile)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             ('User role',
#              {
#                 "fields": (
#                     'is_enroll'
#                 ),
#             }
#             ),
#         )
        
#     ) 
# admin.site.register(CustomUser, CustomUserAdmin)

   