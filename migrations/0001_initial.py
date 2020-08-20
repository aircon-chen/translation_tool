# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-14 02:37
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vhost', models.CharField(default='', max_length=255, verbose_name='target vhost')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('name', models.CharField(help_text='give a naming to this template', max_length=255, verbose_name='template name')),
                ('html', models.TextField(help_text='input html template here...')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_htmltemplate_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_htmltemplate_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vhost', models.CharField(default='', max_length=255, verbose_name='target vhost')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
                ('locale', models.CharField(help_text='format =>  {language_code}_{country_code} ', max_length=10)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_templateresource_set', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('html_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='translation_tool.HtmlTemplate')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_templateresource_set', to=settings.AUTH_USER_MODEL, verbose_name='modified by')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='templateresource',
            unique_together=set([('html_template', 'locale')]),
        ),
    ]