from django.urls import path
from .views import (
    PlanningDetail,
    PlanningSectionDetail,
    planning_sections,
    plannings,
    profile
)


urlpatterns = [
    path(
        'plannings',
        plannings,
        name='plannings'
    ),
    path(
        'plannings/<int:pk>',
        PlanningDetail.as_view(),
        name='planning'
    ),
    path(
        'planning-sections',
        planning_sections,
        name='planning-sections'
    ),
    path(
        'planning-sections/<int:pk>',
        PlanningSectionDetail.as_view(),
        name='planning-section-detail'
    ),
    path(
        'profiles/<str:profile_id>',
        profile,
        name='profile'
    )
]
