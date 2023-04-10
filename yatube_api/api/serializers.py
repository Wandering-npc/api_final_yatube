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
        model = Group
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True,
                                        slug_field='username')
    author = serializers.SlugRelatedField(queryset=User.objects.all(),
                                          slug_field='username')
    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Вы уже подписаны!'
            )
        ]
    def validate_following(self, value):
        if value == self.context['request'].user:
            raise serializers.ValidationError(
                'Ошибка'
            )
        return value
