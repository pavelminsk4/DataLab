from widgets.models import WidgetsList2, ClippingFeedContentWidget, WidgetDescription, Dimensions, ProjectDimensions
from drf_writable_nested.serializers import WritableNestedModelSerializer
from reports.models import Templates, RegularReport, ReportItem
from project.models import Project, Workspace, Speech, Feedlinks
from accounts.models import Profile, department
from common.post_locator import PostLocator
from django.contrib.auth.models import User
from alerts.models import Alert, AlertItem
from countries_plus.models import Country
from rest_framework import serializers

from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator


class DepartmentSerializer(WritableNestedModelSerializer):
    class Meta:
        model = department
        fields = '__all__'


class ProfileSerializer(WritableNestedModelSerializer):
    department = DepartmentSerializer()
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(WritableNestedModelSerializer):
    user_profile = ProfileSerializer()
    class Meta:
        model = User
        exclude = ['date_joined']


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProjectSerializer(serializers.ModelSerializer):
    members = UserSerializer(many=True, required=False)
    note = serializers.CharField(max_length=1000, allow_blank=True)
    class Meta:
        model = Project
        fields = '__all__'


class WorkspaceSerializer(WritableNestedModelSerializer):
    projects = ProjectSerializer(many=True, required=False)
    description = serializers.CharField(max_length=1000, allow_blank=True, required=False)
    members = UserSerializer(many=True, required=False)
    class Meta:
        model = Workspace
        fields = ['id', 'title', 'description', 'members', 'projects', 'created_at']


class WorkspaceCreateSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, required=False)
    description = serializers.CharField(max_length=1000, allow_blank=True)
    
    class Meta:
        model = Workspace
        fields = '__all__'

    def create(self, validated_data):
        workspace = Workspace.objects.create(title=validated_data['title'], description=validated_data['description'], department=validated_data['department'] or None)
        project = Project.objects.create(**validated_data['projects'][0])
        workspace.members.set(validated_data["members"])
        workspace.projects.add(project)
        return workspace


class CountrySerializer(WritableNestedModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class SpeechSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Speech
        fields = ['language']


class WidgetDescriptionSerializer(WritableNestedModelSerializer):
    class Meta:
        model = WidgetDescription
        fields = '__all__'


class WidgetsListSerializer(WritableNestedModelSerializer):
    summary = WidgetDescriptionSerializer()
    volume = WidgetDescriptionSerializer()
    top_authors = WidgetDescriptionSerializer()
    top_sources = WidgetDescriptionSerializer()
    top_countries = WidgetDescriptionSerializer()
    top_languages = WidgetDescriptionSerializer()
    content_volume_top_sources = WidgetDescriptionSerializer()
    sentiment_top_sources = WidgetDescriptionSerializer()
    sentiment_top_countries = WidgetDescriptionSerializer()
    sentiment_top_authors = WidgetDescriptionSerializer()
    sentiment_top_languages = WidgetDescriptionSerializer()
    sentiment_for_period = WidgetDescriptionSerializer()
    content_volume_top_authors = WidgetDescriptionSerializer()
    content_volume_top_countries = WidgetDescriptionSerializer()
    clipping_feed_content = WidgetDescriptionSerializer()
    top_keywords = WidgetDescriptionSerializer()
    sentiment_top_keywords = WidgetDescriptionSerializer()
    sentiment_number_of_results = WidgetDescriptionSerializer()
    sentiment_diagram = WidgetDescriptionSerializer()
    authors_by_country = WidgetDescriptionSerializer()
    authors_by_language = WidgetDescriptionSerializer()
    authors_by_sentiment = WidgetDescriptionSerializer()
    overall_top_authors = WidgetDescriptionSerializer()
    overall_top_sources = WidgetDescriptionSerializer()
    sources_by_country = WidgetDescriptionSerializer()
    sources_by_language = WidgetDescriptionSerializer()
    top_sharing_sources = WidgetDescriptionSerializer()
    top_keywords_by_country = WidgetDescriptionSerializer()
    languages_by_country = WidgetDescriptionSerializer()


    class Meta:
        model = WidgetsList2
        fields = '__all__'


class ClippingFeedContentWidgetListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        users = [ClippingFeedContentWidget(**item) for item in validated_data]
        return ClippingFeedContentWidget.objects.bulk_create(users)


class ClippingFeedContentWidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClippingFeedContentWidget
        fields = '__all__'
        list_serializer_class = ClippingFeedContentWidgetListSerializer


class DimensionsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Dimensions
        fields = '__all__'


class ProjectDimensionsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = ProjectDimensions
        fields = '__all__'


class ProjectDimensionsListSerializer(WritableNestedModelSerializer):
    dimension = DimensionsSerializer()
    class Meta:
        model = ProjectDimensions
        fields = '__all__'


class TemplatesSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Templates
        fields = '__all__'


class AlertItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertItem
        fields = '__all__'


class AlertCreateSerializer(WritableNestedModelSerializer):
    items = AlertItemSerializer(many=True)
    class Meta:
        model = Alert
        fields = '__all__'
  

class AlertsSerializer(WritableNestedModelSerializer):
    creator = UserSerializer(required=False)
    user = UserSerializer(many=True, required=False)
    class Meta:
        model = Alert
        fields = '__all__'


class PostsSerializer(WritableNestedModelSerializer):
    class Meta:
        model = PostLocator().post
        fields = ['entry_author']


class FeedlinksSerializer(WritableNestedModelSerializer):
    class Meta:
        model = Feedlinks
        fields = ['source1']    


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
      required=True,
      validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProfileUserSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Profile
        fields = '__all__'


class ReportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportItem
        fields = "__all__"


class RegularReportCreateSerializer(WritableNestedModelSerializer):
    items = ReportItemSerializer(many=True)
    class Meta:
        model = RegularReport
        fields = '__all__'
