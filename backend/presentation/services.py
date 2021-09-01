from typing import OrderedDict

from presentation.models import Presentation, Tag


class PresentationService:
    def create_presentation(self, validated_data: OrderedDict) -> Presentation:
        instance = Presentation.objects.create(
            title=validated_data.get("title"),
            description=validated_data.get("description", ""),
            scheduled_on=validated_data.get("scheduled_on"),
        )
        if validated_data.get("tags", None):
            tags = validated_data.pop("tags")
            tags_set = {tag["name"] for tag in tags}
            tags_query = Tag.objects.filter(name__in=tags_set)
            tags_to_create = tags_set.difference(
                set(tags_query.values_list("name", flat=True))
            )
            new_tags = Tag.objects.bulk_create(
                Tag(name=tag_name) for tag_name in tags_to_create
            )
            tags = set(list(tags_query) + new_tags)
            instance.tags.add(*tags)

        return instance

    def update_presentation(
        self, instance: Presentation, validated_data: OrderedDict, partial: bool
    ) -> Presentation:
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.scheduled_on = validated_data.get(
            "scheduled_on", instance.scheduled_on
        )
        instance.user = validated_data.get("user", instance.user)

        if validated_data.get("tags", None):
            tags = validated_data.pop("tags")
            tags_set = {tag["name"] for tag in tags}
            tags_query = Tag.objects.filter(name__in=tags_set)
            tags_to_create = tags_set.difference(
                set(tags_query.values_list("name", flat=True))
            )
            if not partial:
                instance.tags.clear()
            new_tags = Tag.objects.bulk_create(
                Tag(name=tag_name) for tag_name in tags_to_create
            )
            tags = set(list(tags_query) + new_tags)
            instance.tags.add(*tags)

        instance.save()
        return instance
