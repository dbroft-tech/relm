from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .models import Staff, Sermon, Event, PrayerRequest, Donation, Newsletter
from .forms import PrayerRequestForm, DonationForm, ContactForm
from django.utils import timezone
from django.core.files.storage import default_storage
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def home(request):
    upcoming_events = Event.objects.filter(date__gte=timezone.now()).order_by('date')[:3]
    latest_sermons = Sermon.objects.order_by('-date')[:3]
    context = {
        'upcoming_events': upcoming_events,
        'latest_sermons': latest_sermons,
    }
    return render(request, 'core/home.html', context)

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def events(request):
    events_list = Event.objects.filter(date__gte=timezone.now()).order_by('date')
    context = {'events': events_list}
    return render(request, 'core/events.html', context)

def sermons(request):
    sermons_list = Sermon.objects.order_by('-date')
    context = {'sermons': sermons_list}
    return render(request, 'core/sermons.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Email to church staff
            html_message = render_to_string('core/emails/contact_email.html', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            })
            
            try:
                # Send email to church staff
                send_mail(
                    subject=f'New Contact Form Submission: {subject}',
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    html_message=html_message,
                    fail_silently=False,
                )
                
                # Send confirmation email to user
                send_mail(
                    subject='Thank you for contacting Redeemed Life Church',
                    message=f'Dear {name},\n\nThank you for reaching out to us. We have received your message and will get back to you soon.\n\nBest regards,\nRedeemed Life Church',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email],
                    fail_silently=False,
                )
                
                messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
                return redirect('contact')
            
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again later.')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})

def prayer_request(request):
    if request.method == 'POST':
        form = PrayerRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your prayer request has been submitted.')
            return redirect('prayer_request')
    else:
        form = PrayerRequestForm()
    return render(request, 'core/prayer_request.html', {'form': form})

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            # Add payment processing logic here (e.g., Stripe)
            donation.save()
            messages.success(request, 'Thank you for your donation!')
            return redirect('home')
    else:
        form = DonationForm()
    return render(request, 'core/donate.html', {'form': form})

def staff(request):
    staff_list = Staff.objects.all()
    context = {'staff': staff_list}
    return render(request, 'core/staff.html', context)

def newsletter(request):
    if request.method == 'POST':
        # Handle newsletter subscription
        messages.success(request, 'Successfully subscribed to the newsletter!')
        return redirect('newsletter')
    
    # Get all published newsletters
    newsletters = Newsletter.objects.filter(is_published=True).order_by('-date_created')
    return render(request, 'core/newsletter.html', {
        'newsletters': newsletters
    })

# Add an admin view to manage newsletters
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'is_published')
    list_filter = ('is_published', 'date_created')
    search_fields = ('title', 'description')
    ordering = ('-date_created',)

def calendar_view(request):
    upcoming_events = Event.objects.filter(
        date__gte=timezone.now()
    ).order_by('date')[:5]
    
    return render(request, 'core/calendar.html', {
        'upcoming_events': upcoming_events
    })

# Add API endpoint for calendar events
def event_api(request):
    events = Event.objects.all()
    event_list = []
    
    for event in events:
        event_list.append({
            'id': event.id,
            'title': event.title,
            'start': event.date.isoformat(),
            'description': event.description,
            'location': event.location,
            'url': f'/events/{event.id}',
            'className': f'event-category-{event.category}' if hasattr(event, 'category') else ''
        })
    
    return JsonResponse(event_list, safe=False)

def handler404(request, exception):
    return render(request, 'core/404.html', status=404) 