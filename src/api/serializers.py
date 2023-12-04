from rest_framework import serializers
from .models import eksisozluk_entries

class EksiSozlukEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = eksisozluk_entries
        fields = '__all__'

    def to_representation(self,instance):
        author_data={
            "analyze_body": f"{instance.author} posted an entry about {instance.title}: {instance.content}",
            "author": {
                "author_id": f"eksi_sozluk: {instance.author}",
                "author_id_on_platform": instance.author,
                "delivery_date": {
                    "@type": "datetime",
                    "value": instance.entry_date_from_scape
                },
                "link": f"https://eksisozluk1923.com{instance.author_profile_link}",
                "name": instance.author,
                "platform": "eksi_sozluk",
                "username": instance.author
            },
            "content": {
                "author_id": f"eksi_sozluk:{instance.author}",
                "body": instance.content,
                "content_id": f"eksi_sozluk:{instance.entryId}",
                "content_id_on_platform": instance.entryId,
                "date": {
                    "@type": "datetime",
                    "value": instance.entry_date
                },
                "delivery_date": {
                    "@type": "datetime",
                    "value": instance.entry_date_from_scape
                },
                "platform": "eksi_sozluk",
                "platform_web_link": instance.titleId
            }
        }
        return author_data
