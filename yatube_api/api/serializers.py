from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериализация групп."""

    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        read_only_fields = ('post',)
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    """Сериализация подписок"""
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username',
                                        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field='username')
    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Ошибка'
            )
        ]
    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Ошибка'
            )
        return value
