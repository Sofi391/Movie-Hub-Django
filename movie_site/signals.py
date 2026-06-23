from django.contrib.auth.models import Group, Permission, User
from django.db.models.signals import post_migrate, post_save
from django.dispatch import receiver
from django.apps import apps
from django.urls import reverse

from .models import Notification
from django.utils import timezone
from datetime import timedelta
import random


@receiver(post_migrate)
def create_editor_group(sender, **kwargs):
    if sender.label != 'movie_site':
        return
    editor_group, created = Group.objects.get_or_create(name='Editors')

    app_label = 'movie_site'

    permissions = Permission.objects.filter(content_type__app_label=app_label,
                                            codename__in=[
                                                'edit_media',
                                                'view_media',
                                            ])
    editor_group.permissions.add(*permissions)
    editor_group.save()
    print('Created editor group')


@receiver(post_migrate)
def create_moderators(sender, **kwargs):
    if sender.label != 'movie_site':
        return

    moderator_group, created = Group.objects.get_or_create(name='Moderators')

    app_label = 'movie_site'

    permissions = Permission.objects.filter(content_type__app_label=app_label,
                                            codename__in=[
                                                'view_user_media',
                                                'edit_user_media',
                                                'delete_user_media',
                                            ])
    moderator_group.permissions.add(*permissions)
    moderator_group.save()
    print('Created moderator group')


@receiver(post_save, sender='movie_site.UserMedia')
def community_activity_notification(sender, instance, created, **kwargs):
    if not created:
        return

    # Rate limiting: max 1 activity notification per user per 30 minutes
    recent_activity = Notification.objects.filter(
        sender=instance.user,
        type='Activity',
        created_at__gte=timezone.now() - timedelta(minutes=30)
    ).exists()
    
    if recent_activity:
        return

    # Random chance: only 65% of activities generate notifications (increased for small user base)
    if random.random() > 0.65:
        return

    # Skip low-rated content (< 6.0) to keep quality high
    if instance.media.rating and instance.media.rating < 6.0:
        return

    # Create vibrant, interactive notification content
    action_emoji = '🎬' if instance.status == 'Watched' else '📌'
    action_text = 'marked as watched' if instance.status == 'Watched' else 'added to watchlist'
    status_path = 'watched' if instance.status == 'Watched' else 'watchlist'

    # Direct clickable URL in the body
    profile_url = f"/my/{status_path}/{instance.media.type}/?user_id={instance.user.id}"
    
    # Rich, engaging title with emojis
    title = f'🔥 <a href="{profile_url}">@{instance.user.username}</a> just {action_emoji} {action_text} {instance.media.name}!'
    
    # Rich, detailed content with rating and encouragement
    rating_text = f"⭐ {instance.media.rating}/10" if instance.media.rating else "Not rated yet"
    genre_text = ", ".join([g.name for g in instance.media.genre.all()[:3]]) if instance.media.genre.exists() else "No genres"
    
    content = f"""🎭 {instance.media.name} ({instance.media.type.title()})
{rating_text} • {genre_text}

{'🏆 Another great watch added to the community!' if instance.status == 'Watched' else '🎯 Someone found their next binge-watch!'}

👀 See what <a href="{profile_url}">@{instance.user.username}</a> is {'watching' if instance.status == 'Watched' else 'planning to watch'}

✨ Discover new content and join the conversation!"""
    
    # Keep action_url as backup
    url = f"/my/{status_path}/{instance.media.type}/?user_id={instance.user.id}"

    recipients = User.objects.exclude(id=instance.user.id).exclude(username='adminsofi').values_list('id', flat=True)
    notifications = [
        Notification(
            sender=instance.user,
            recipient_id=uid,
            type='Activity',
            title=title,
            content=content,
            action_url=url,
        )
        for uid in recipients
    ]
    Notification.objects.bulk_create(notifications)
