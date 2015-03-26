# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pybb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForumSubscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveSmallIntegerField(help_text="The auto-subscription works like you manually subscribed to watch each topic:\nyou will be notified when a topic will receive an answer. \nYou can choose to be notified only when a new topic is added. It meansyou will be notified only once when the topic is created: you won't be notified for the answers.", verbose_name='Subscription type', choices=[(1, 'New topics only'), (2, 'All new topics and posts')])),
                ('forum', models.ForeignKey(related_name='subscriptions', verbose_name='Forum', to='pybb.Forum')),
                ('user', models.ForeignKey(related_name='forum_subscriptions', verbose_name='Subscriber', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subscription to forum',
                'verbose_name_plural': 'Subscriptions to forums',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='forumsubscription',
            unique_together=set([('user', 'forum')]),
        ),
    ]