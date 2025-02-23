# Redeemed Life Church Website 🏛️

A modern, responsive church website built with Django and Bootstrap, featuring a beautiful glassmorphism design and seamless user experience.

## ✨ Features

- **Modern Design**
  - Glassmorphism UI elements
  - Responsive layout for all devices
  - Smooth animations and transitions
  - Interactive components

- **Core Functionality**
  - 📅 Event Calendar & Management
  - 🎤 Sermon Archive
  - 🙏 Prayer Request System
  - 💌 Newsletter Subscription
  - 💰 Donation System
  - 📞 Contact Forms

- **Technical Features**
  - Server-side rendering with Django
  - Fast loading with Vercel deployment
  - Analytics & Performance monitoring
  - SEO optimized
  - Secure form handling

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip
- virtualenv (recommended)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/redeemed-life-church.git
cd redeemed-life-church
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Environment setup**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Database setup**
```bash
python manage.py migrate
```

6. **Create admin user**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see the website.

## 🌐 Deployment

This project is configured for deployment on Vercel:

1. **Install Vercel CLI**
```bash
npm i -g vercel
```

2. **Deploy**
```bash
vercel
```

## 🔧 Configuration

### Environment Variables

Required environment variables in `.env`:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=.vercel.app,.now.sh,localhost,127.0.0.1

# Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-app-specific-password

# Site Settings
SITE_NAME=Redeemed Life Church
SITE_URL=https://your-domain.vercel.app
```

## 📁 Project Structure

```
redeemed-life-church/
├── config/                 # Project configuration
├── core/                  # Main application
│   ├── management/       # Custom commands
│   ├── templates/        # HTML templates
│   ├── static/          # Static files
│   └── ...
├── static/               # Global static files
│   ├── css/
│   ├── js/
│   └── images/
└── requirements.txt      # Python dependencies
```

## 💻 Development

### Running Tests
```bash
python manage.py test
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Comment complex logic
- Keep functions small and focused

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact & Support

For support and queries:
- Email: redeemedlifem@gmail.com
- Phone: +256 772 400490 (MTN)
- Phone: +256 752 888899 (Airtel)
- Location: Bunamwaya, Ngobe, Kampala, Uganda

## 🙏 Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Boxicons](https://boxicons.com/)
- [AOS Library](https://michalsnik.github.io/aos/)
- [Vercel](https://vercel.com/)

## 🔄 Updates & Maintenance

The website is regularly updated with:
- Security patches
- New features
- Performance improvements
- Content updates

Last updated: March 2024

---
Made with ❤️ for Redeemed Life Church
```