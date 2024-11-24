from core.models import User, OnetimePasscode
from rest_framework import serializers
from student.models import Student


EDUCATION_LEVEL = [
    ("bac", "BAC"),
    ("licence", "Licence"),
    ("master", "Master"),
    ("doctorat", "Doctorat"),
    ("cap", "CAP"),
]

BAC_SERIES = [
        ("Termainal Lettre et Litterature (TLL)", "Termainal Lettre et Litterature (TLL)"),
        ("tseco", "Terminal Science Economique (TSECO)"),
        ("tss", "Terminal Science Exact (TSS)")
    ]

class StudenProfileSerializer(serializers.ModelSerializer):

    # Champs du model user
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)

    # Champs du model student 
    id = serializers.IntegerField(read_only=True)
    profile_picture = serializers.ImageField()
    date_of_birth = serializers.DateField(read_only=True)
    country_origin = serializers.CharField(max_length="100")
    phone_number = serializers.CharField(max_length=8)
    education_level = serializers.ChoiceField(choices=EDUCATION_LEVEL)
    education_level_display = serializers.SerializerMethodField()
    bac_serie = serializers.ChoiceField(choices= BAC_SERIES)
    bac_serie_display = serializers.SerializerMethodField()
    country_wishlist = serializers.SerializerMethodField()
    average_score = serializers.DecimalField(decimal_places=2, max_digits=4)

    def get_education_level_display(self, obj):
        return obj.get_education_level_display()

    def get_bac_serie_display(self, obj):
        return obj.get_bac_serie_display()

    def get_country_wishlist(self, obj):
        return [
            {
                "id": country.id,
                "name": country.name,
            }
            for country in obj.wishlist.all()
        ]

    def update(self, instance, validated_data):
        # Si une donnée n'est pas envoyée, elle ne sera pas mise à jour
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'date_joined', 'profile_picture', 
            'date_of_birth', 'country_origin', 'phone_number', 'education_level', 
            'bac_serie', 'country_wishlist', 'average_score', 'education_level_display', 'bac_serie_display']


    
class StudenPrefrencesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    profile_picture = serializers.ImageField()
    country_origin = serializers.CharField(max_length="60")
    country_wishlist = serializers.SerializerMethodField()


    def get_country_wishlist(self, obj):
        return [
            {
                "id": country.id,
                "name": country.name
            }
            for country in obj.wishlist.all()
        ]

    class Meta:
        model = Student
        fields = ['id', 'profile_picture', 'country_origin', 'country_wishlist']