from djmoney.contrib.django_rest_framework import MoneyField
from rest_framework import serializers
from school.models import University


class UniversitySerlializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    country_name = serializers.CharField()
    city = serializers.CharField()
    domain = serializers.CharField()
    website = serializers.URLField()
    edu_level_required = serializers.CharField()
    require_score = serializers.DecimalField(default=0.0, max_digits=4, decimal_places=2,)
    programs = serializers.SerializerMethodField()
    documents_fees = MoneyField(max_digits=10, decimal_places=0)
    image = serializers.ImageField()

    def get_programs(self, obj):
        return [
            {
                "id": program.id,
                "name": program.name,
                "duration": program.duration,
                "degree": program.degree
            }
            for program in obj.programs.all()
        ]
    class Meta:
        model = University
        fields = ["id", "name", "country_code", "country_name", "city", "website", "domain", "edu_level_required",  "require_score", "programs", "documents_fees", "image"]
    