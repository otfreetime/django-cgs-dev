# Generated by Django 3.2.11 on 2022-03-30 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CategoriesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GenerateModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datepart', models.DateField()),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project_related_models', to='devapp.generatemodel')),
                ('relatedIssues1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedIssues1_related_models', to='devapp.generatemodel')),
                ('relatedIssues2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedIssues2_related_models', to='devapp.generatemodel')),
                ('relatedIssues3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relatedIssues3_related_models', to='devapp.generatemodel')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Remarks_related_models', to='devapp.generatemodel')),
                ('thetype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thetype_related_models', to='devapp.generatemodel')),
            ],
        ),
        migrations.CreateModel(
            name='CodesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('endesc', models.CharField(max_length=100)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('ardesc', models.CharField(max_length=100)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Categories', related_query_name='Category', to='devapp.categoriesmodel')),
                ('mytest', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_models', to='devapp.codesmodel')),
            ],
        ),
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('endesc', models.CharField(max_length=100)),
                ('remarks', models.CharField(blank=True, max_length=100, null=True)),
                ('ardesc', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devapp.categories')),
            ],
        ),
    ]
