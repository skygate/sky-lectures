from typing import OrderedDict

from django.contrib.auth import get_user_model

from presentation.models import Comment, Presentation, Tag
from presentation.serializers import CommentSerializer


PresentationData = list[OrderedDict[str, str]]
User = get_user_model()


class PresentationService:
    def add_tags_to_presentation(
        self, presentation: Presentation, tags: PresentationData, partial: bool
    ) -> Presentation:
        tags_names_set = {tag["name"] for tag in tags}
        existing_tags = Tag.objects.filter(name__in=tags_names_set)
        tags_to_create = tags_names_set.difference(
            set(existing_tags.values_list("name", flat=True))
        )
        if not partial:
            presentation.tags.clear()
        new_tags = Tag.objects.bulk_create(
            Tag(name=tag_name) for tag_name in tags_to_create
        )
        presentation.tags.add(*new_tags, *existing_tags)
        return presentation

    def create_presentation(self, presentation_data: PresentationData, user: User) -> Presentation:
        presentation = Presentation.objects.create(
            title=presentation_data.get("title"),
            description=presentation_data.get("description"),
            scheduled_on=presentation_data.get("scheduled_on"),
            user=user,
        )
        if (tags := presentation_data.pop("tags", None)) is not None:
            presentation = self.add_tags_to_presentation(
                presentation=presentation, tags=tags, partial=False
            )
        presentation.save()
        return presentation

    def update_presentation(
        self,
        presentation: Presentation,
        presentation_data: PresentationData,
        partial: bool,
    ) -> Presentation:
        presentation.title = presentation_data.get("title", presentation.title)
        presentation.description = presentation_data.get(
            "description", presentation.description
        )
        presentation.scheduled_on = presentation_data.get(
            "scheduled_on", presentation.scheduled_on
        )
        presentation.user = presentation_data.get("user", presentation.user)

        if (tags := presentation_data.pop("tags", None)) is not None:
            presentation = self.add_tags_to_presentation(
                presentation=presentation, tags=tags, partial=partial
            )

        presentation.save()
        return presentation


class CommentService:
    def update_comment(self, comment: Comment, validated_data: OrderedDict) -> Comment:
        comment.text = validated_data.get("text", comment.text)
        comment.save(update_fields=["text"])
        return comment

    def set_comment_user(self, serializer: CommentSerializer, user: User) -> None:
        serializer.save(user=user)