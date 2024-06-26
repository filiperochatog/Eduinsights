# Generated by Django 5.0 on 2024-05-11 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_usersubmission_categoria_bloom'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersubmission',
            name='componentes_curriculares',
            field=models.CharField(choices=[('MAT', 'Matemática'), ('CIE', 'Ciências'), ('LIT', 'Literatura'), ('HIS', 'História'), ('GEO', 'Geografia')], default=11, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='usersubmission',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='usersubmission',
            name='categoria_bloom',
            field=models.CharField(choices=[('AN', 'Análise'), ('AP', 'Aplicação'), ('CO', 'Compreensão'), ('EV', 'Avaliação'), ('KN', 'Conhecimento'), ('NP', 'Não faz parte da taxonomia'), ('SY', 'Síntese')], default='NP', max_length=2),
        ),
    ]
