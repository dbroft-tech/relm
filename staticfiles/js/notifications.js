class PageNotification {
    constructor() {
        this.notifications = {
            'home': {
                title: 'Welcome to Redeemed Life Church',
                message: 'Join us as we worship, grow, and serve together.',
                icon: 'bxs-church'
            },
            'about': {
                title: 'Our Story',
                message: 'Learn about our journey of faith and community.',
                icon: 'bxs-book-heart'
            },
            'services': {
                title: 'Join Our Services',
                message: 'Experience worship every Sunday at 10:00 AM.',
                icon: 'bxs-bible'
            },
            'events': {
                title: 'Upcoming Events',
                message: 'Stay connected with our church community.',
                icon: 'bxs-calendar-star'
            },
            'sermons': {
                title: 'Latest Sermons',
                message: 'Be inspired by the Word of God.',
                icon: 'bxs-microphone-alt'
            },
            'staff': {
                title: 'Our Leadership',
                message: 'Meet the dedicated team serving our community.',
                icon: 'bxs-group'
            },
            'prayer_request': {
                title: 'Prayer Support',
                message: 'Share your prayer requests with us.',
                icon: 'bxs-hand'
            },
            'donate': {
                title: 'Support Our Ministry',
                message: 'Partner with us in spreading God\'s love.',
                icon: 'bxs-heart'
            },
            'newsletter': {
                title: 'Stay Updated',
                message: 'Subscribe to our newsletter for regular updates.',
                icon: 'bxs-news'
            },
            'contact': {
                title: 'Get in Touch',
                message: 'We\'d love to hear from you.',
                icon: 'bxs-contact'
            }
        };
    }

    show(page) {
        console.log('Showing notification for page:', page);
        const notification = this.notifications[page];
        if (!notification) {
            console.log('No notification found for page:', page);
            return;
        }

        const notifEl = document.createElement('div');
        notifEl.className = 'page-notification glass';
        console.log('Creating notification element');
        notifEl.innerHTML = `
            <i class='bx ${notification.icon}'></i>
            <div class="notification-content">
                <h4>${notification.title}</h4>
                <p>${notification.message}</p>
            </div>
            <button class="notification-close">
                <i class='bx bx-x'></i>
            </button>
        `;

        document.body.appendChild(notifEl);
        console.log('Notification added to DOM');

        // Animate in
        setTimeout(() => {
            notifEl.classList.add('show');
            console.log('Notification shown');
        }, 100);

        // Close button
        const closeBtn = notifEl.querySelector('.notification-close');
        closeBtn.addEventListener('click', () => {
            notifEl.classList.remove('show');
            setTimeout(() => notifEl.remove(), 300);
        });

        // Auto close after 5 seconds
        setTimeout(() => {
            if (notifEl.parentElement) {
                notifEl.classList.remove('show');
                setTimeout(() => notifEl.remove(), 300);
            }
        }, 5000);
    }
} 