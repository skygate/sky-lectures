from typing import OrderedDict

from presentation.models import Presentation, Tag
from users.models import Profile, User


class UserService:
    def update_user_profile(
        self, profile: Profile, validated_data: OrderedDict
    ) -> Profile:
        profile.file = validated_data.get("file", profile.file)
        profile.description = validated_data.get("description", profile.description)
        profile.save()
        return profile

    def add_to_favourite_tags(self, user: User, validated_data: OrderedDict) -> User:
        new_tags = validated_data.get("favourite_tags")
        added_tags = [
            added_tag for added_tag in user.favourite_tags.values_list("id", flat=True)
        ]
        new_favourite_tags = Tag.objects.filter(id__in=set(new_tags + added_tags))

        user.favourite_tags.set(new_favourite_tags)

        return user

    def add_to_favourite_presentations(
        self, user: User, validated_data: OrderedDict
    ) -> User:
        new_presentations = validated_data.get("favourite_presentations")
        added_presentations = [
            added_presentation
            for added_presentation in user.favourite_presentations.values_list(
                "id", flat=True
            )
        ]
        new_favourite_presentations = Presentation.objects.filter(
            id__in=set(new_presentations + added_presentations)
        )

        user.favourite_presentations.set(new_favourite_presentations)

        return user

    def remove_from_favourite_tags(
        self, user: User, validated_data: OrderedDict
    ) -> User:
        new_tags = validated_data.get("favourite_tags")
        added_tags = [
            added for added in user.favourite_tags.values_list("id", flat=True)
        ]
        new_favourite_tags = Tag.objects.filter(
            id__in=set(added_tags).difference(new_tags)
        )

        user.favourite_tags.set(new_favourite_tags)

        return user

    def remove_from_favourite_presentations(
        self, user: User, validated_data: OrderedDict
    ) -> User:
        new_presentations = set(validated_data.get("favourite_presentations"))
        added_presentations = [
            added for added in user.favourite_presentations.values_list("id", flat=True)
        ]
        new_favourite_presentations = Presentation.objects.filter(
            id__in=set(added_presentations).difference(new_presentations)
        )

        user.favourite_presentations.set(new_favourite_presentations)

        return user
