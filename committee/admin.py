"""
Admin interface for the committee application.
"""
################################################################

from django.contrib import admin
from django.urls import NoReverseMatch

from .forms import CommitteeForm
from .models import Committee, Member

################################################################


class MemberInlineBase(admin.TabularInline):
    """
    Fancy inline handling to make people readonly; once they've been added
    as a member.
    """

    model = Member
    extra = 0
    fields = ["active", "person", "start_date", "end_date", "chair", "ex_officio"]
    view_on_site = False

    def get_queryset(self, *args, **kwargs):
        """
        Only current and future people show in the line.
        """
        qs = super(MemberInlineBase, self).get_queryset(*args, **kwargs)
        return qs.current_or_future()


################################################################


class MemberInlineEdit(MemberInlineBase):
    """
    Edit (not add) current and future members.
    """

    readonly_fields = ["person"]
    verbose_name_plural = "Current and future members"

    def has_add_permission(self, *args, **kwargs):
        return False


################################################################


class MemberInlineAdd(MemberInlineBase):
    """
    Add members
    """

    verbose_name_plural = "Add members"

    def has_edit_permission(self, *args, **kwargs):
        return False

    def has_delete_permission(self, *args, **kwargs):
        return False

    def get_queryset(self, *args, **kwargs):
        qs = super(MemberInlineAdd, self).get_queryset(*args, **kwargs)
        return qs.none()


################################################################


class CommitteeAdmin(admin.ModelAdmin):
    """
    Admin for the committee model.
    """

    form = CommitteeForm
    inlines = [MemberInlineEdit, MemberInlineAdd]
    fieldsets = [
        ("", {"fields": ["active", ("name", "ordering")]}),
        (
            "Description",
            {
                "classes": ["collapse"],
                "fields": [
                    "membership",
                    "means_of_selection",
                    "term",
                    "quorum",
                    "terms_of_reference",
                    "remarks",
                ],
            },
        ),
    ]
    list_display = ["name", "slug", "active"]
    list_filter = ["active"]
    save_on_top = True
    search_fields = ["name", "slug"]

    def view_on_site(self, obj):
        try:
            return obj.get_absolute_url()
        except NoReverseMatch:
            return None


admin.site.register(Committee, CommitteeAdmin)


################################################################


class MemberDateFilter(admin.SimpleListFilter):

    title = "members"
    parameter_name = "member-date"

    def lookups(self, request, modelAdmin):
        """
        Returns a list of tuples (coded-value, title).
        """
        return [("current", "Current"), ("past", "Past"), ("future", "Future")]

    def queryset(self, request, queryset):
        """
        Apply the filter to the existing queryset.
        """
        filter = self.value()
        if filter is None:
            return

        if filter == "current":
            return queryset.current()
            # qs = qs.filter(Q(end_date__isnull=True) | Q(end_date__gt=now()))
            # qs = qs.filter(start_date__lte=now())
        if filter == "past":
            return queryset.past()
            # qs = qs.filter(end_date__lt=now())
        if filter == "future":
            return queryset.future()
            # qs = qs.filter(start_date_gt=now())


################################################################


class MemberAdmin(admin.ModelAdmin):
    fields = [
        "active",
        "person",
        "committee",
        "start_date",
        "end_date",
        "chair",
        "ex_officio",
    ]
    list_display = [
        "person",
        "committee",
        "start_date",
        "end_date",
        "chair",
        "ex_officio",
    ]
    list_editable = ["start_date", "end_date", "chair", "ex_officio"]
    list_filter = ["committee", "active", MemberDateFilter, "chair", "ex_officio"]
    ordering = ["committee", "-chair", "person"]
    search_fields = [
        "committee__name",
        "person__cn",
        "person__username",
        "person__emailaddress__email",
    ]
    view_on_site = False

    def get_readonly_fields(self, request, obj=None):
        readonly_dynamic = tuple()
        if obj:  # editing an existing object
            readonly_dynamic += ("person", "committee")
        return self.readonly_fields + readonly_dynamic


admin.site.register(Member, MemberAdmin)


################################################################
