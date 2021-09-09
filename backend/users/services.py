class UserService:
    def update_user_profile(self, profile, validated_data):
        profile.file = validated_data.get("file", profile.file)
        profile.description = validated_data.get("description", profile.description)
        profile.save()
        return profile
