from presentation.models import Presentation, Tag


class UserService:
    def update_user_profile(self, profile, validated_data):
        profile.file = validated_data.get("file", profile.file)
        profile.description = validated_data.get("description", profile.description)
        profile.save()
        return profile

    def add_to_favourite_tags(self, user, request):
        if "favourite_tags" in request.data:
            dict_req = dict(request.data)
            new_tags = dict_req.get("favourite_tags")

            added_tags = [
                str(added_tag)
                for added_tag in user.favourite_tags.values_list("id", flat=True)
            ]
            all_tags = set(new_tags + added_tags)
            new_favourite_tags = Tag.objects.filter(id__in=all_tags)

            user.favourite_tags.set(new_favourite_tags)

    def add_to_favourite_presentations(self, user, request):
        if "favourite_presentations" in request.data:
            dict_req = dict(request.data)
            new_presentations = dict_req.get("favourite_presentations")
            added_presentations = [
                str(added_presentation)
                for added_presentation in user.favourite_presentations.values_list(
                    "id", flat=True
                )
            ]
            all_presentations = set(new_presentations + added_presentations)
            new_favourite_presentations = Presentation.objects.filter(
                id__in=all_presentations
            )

            user.favourite_presentations.set(new_favourite_presentations)

    def remove_from_favourite_tags(self, user, request):
        if "favourite_tags" in request.data:
            dict_req = dict(request.data)
            new = set(dict_req.get("favourite_tags"))
            added = set(
                [
                    str(added)
                    for added in user.favourite_tags.values_list("id", flat=True)
                ]
            )
            new_favourite_tags = Tag.objects.filter(id__in=added.difference(new))

            user.favourite_tags.set(new_favourite_tags)

    def remove_from_favourite_presentations(self, user, request):
        if "favourite_presentations" in request.data:
            dict_req = dict(request.data)
            new = set(dict_req.get("favourite_presentations"))
            added = set(
                [
                    str(added)
                    for added in user.favourite_presentations.values_list(
                        "id", flat=True
                    )
                ]
            )
            new_favourite_presentations = Presentation.objects.filter(
                id__in=added.difference(new)
            )

            user.favourite_presentations.set(new_favourite_presentations)
