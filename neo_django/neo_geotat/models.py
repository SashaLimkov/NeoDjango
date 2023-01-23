import neomodel
import django_neomodel


class Region(django_neomodel.DjangoNode):  # noqa - turns off warnings from django
    name = neomodel.StringProperty(max_length=500)
    # languages = neomodel.RelationshipTo("Language", "LANGUAGE")

    def __str__(self):
        return self.name


class Language(django_neomodel.DjangoNode):  # noqa
    lang_code = neomodel.IntegerProperty()
    iso = neomodel.StringProperty(max_length=5)
    lang_name = neomodel.StringProperty(max_length=100)
    regions = neomodel.RelationshipTo("Region", "REGION")

    def __str__(self):
        return self.iso


