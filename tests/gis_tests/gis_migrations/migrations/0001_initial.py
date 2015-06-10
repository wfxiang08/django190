from django.db import migrations, models

from ...models import models as gis_models


class Migration(migrations.Migration):
    """
    Used for gis.specific migration tests.
    """
    operations = [
        migrations.CreateModel(
            name='Neighborhood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('geom', gis_models.MultiPolygonField(srid=4326)),
            ],
            options={
                'required_db_features': ['gis_enabled'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('neighborhood', models.ForeignKey(to='gis_migrations.Neighborhood', to_field='id', null=True)),
                ('address', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(null=True, blank=True)),
                ('geom', gis_models.PointField(srid=4326, geography=True)),
            ],
            options={
                'required_db_features': ['gis_enabled'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='household',
            name='family',
            field=models.ForeignKey(blank=True, to='gis_migrations.Family', null=True),
            preserve_default=True,
        ),
    ]
