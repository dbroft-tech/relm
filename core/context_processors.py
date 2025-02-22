from django.conf import settings
from django.urls import resolve, Resolver404
from django.urls.base import get_resolver

def seo_metadata(request):
    """
    Provides SEO metadata for all pages based on current URL
    """
    try:
        # Skip static files and media files
        if request.path.startswith('/static/') or request.path.startswith('/media/'):
            current_url = ''
        else:
            resolver_match = resolve(request.path_info)
            current_url = resolver_match.url_name if resolver_match else ''
    except Resolver404:
        current_url = ''

    # Default metadata
    metadata = {
        'meta_title': 'Redeemed Life Church',
        'meta_description': 'Welcome to Redeemed Life Church - A place of worship, growth, and community.',
        'meta_keywords': 'church, worship, faith, community, Jesus Christ',
        'og_title': 'Redeemed Life Church',
        'og_description': 'Join our community of faith and fellowship.',
        'og_type': 'website',
        'canonical_url': request.build_absolute_uri(),
        'current_url': current_url,
    }
    
    # Page-specific metadata
    page_metadata = {
        'home': {
            'meta_title': f"Welcome to {settings.SITE_NAME} - A Place of Worship and Community",
            'meta_description': "Join our vibrant community for worship, fellowship, and spiritual growth. Experience uplifting sermons, engaging events, and a warm, welcoming atmosphere.",
            'meta_keywords': "church home, worship service, christian community, faith, religion",
        },
        'about': {
            'meta_title': f"About {settings.SITE_NAME} - Our Mission and Values",
            'meta_description': "Learn about our church's mission, values, and history. Discover how we serve our community and spread God's love.",
            'meta_keywords': "church mission, church values, church history, christian faith, religious community",
        },
        'services': {
            'meta_title': f"Church Services at {settings.SITE_NAME}",
            'meta_description': "Join us for worship services, prayer meetings, and bible studies. Experience meaningful worship and spiritual growth.",
            'meta_keywords': "church services, worship times, sunday service, prayer meeting, bible study",
        },
        'events': {
            'meta_title': f"Church Events at {settings.SITE_NAME}",
            'meta_description': "Stay updated with our upcoming events, activities, and gatherings. Join our community in fellowship and celebration.",
            'meta_keywords': "church events, religious activities, community gatherings, christian fellowship",
        },
        'sermons': {
            'meta_title': f"Sermons from {settings.SITE_NAME}",
            'meta_description': "Listen to our latest sermons and messages. Find spiritual guidance and biblical teachings to strengthen your faith.",
            'meta_keywords': "church sermons, christian messages, biblical teaching, spiritual guidance",
        },
        'staff': {
            'meta_title': f"Our Church Staff - {settings.SITE_NAME}",
            'meta_description': "Meet our dedicated church staff and leadership team. Learn about the people who serve our community.",
            'meta_keywords': "church staff, pastoral team, church leadership, ministry team",
        },
        'prayer_request': {
            'meta_title': f"Submit Prayer Requests - {settings.SITE_NAME}",
            'meta_description': "Share your prayer requests with our church community. We believe in the power of prayer and supporting one another.",
            'meta_keywords': "prayer requests, christian prayer, prayer support, church prayer",
        },
        'donate': {
            'meta_title': f"Support Our Ministry - {settings.SITE_NAME}",
            'meta_description': "Support our church's mission and ministry through your generous donations. Help us make a difference in our community.",
            'meta_keywords': "church donations, ministry support, christian giving, church offering",
        },
        'newsletter': {
            'meta_title': f"Church Newsletter - Stay Connected with {settings.SITE_NAME}",
            'meta_description': "Subscribe to our church newsletter and stay updated with weekly devotionals, church events, announcements, and spiritual insights.",
            'meta_keywords': "church newsletter, christian newsletter, weekly devotionals, church updates",
        },
        'contact': {
            'meta_title': f"Contact {settings.SITE_NAME}",
            'meta_description': "Get in touch with our church. We'd love to hear from you and answer any questions you may have.",
            'meta_keywords': "church contact, church location, church phone, church email",
        },
    }
    
    # Update metadata if page-specific data exists
    if current_url in page_metadata:
        metadata.update(page_metadata[current_url])
    
    # Customize metadata based on current URL
    if current_url:
        page_titles = {
            'home': 'Home',
            'about': 'About Us',
            'services': 'Church Services',
            'events': 'Church Events',
            'sermons': 'Sermons',
            'contact': 'Contact Us',
            'staff': 'Our Staff',
            'prayer_request': 'Prayer Requests',
            'donate': 'Support Our Ministry',
            'newsletter': 'Church Newsletter',
        }
        
        if current_url in page_titles:
            metadata['meta_title'] = f"{page_titles[current_url]} - Redeemed Life Church"
    
    return {
        'seo_metadata': metadata,
        'canonical_url': request.build_absolute_uri(),
    } 