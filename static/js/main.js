// Smooth Scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    if (anchor.getAttribute('href') !== '#') {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    }
});

// Navbar Scroll Effect
const nav = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;
    
    if (currentScroll <= 0) {
        nav.classList.remove('scroll-up');
        return;
    }
    
    if (currentScroll > lastScroll && !nav.classList.contains('scroll-down')) {
        nav.classList.remove('scroll-up');
        nav.classList.add('scroll-down');
    } else if (currentScroll < lastScroll && nav.classList.contains('scroll-down')) {
        nav.classList.remove('scroll-down');
        nav.classList.add('scroll-up');
    }
    lastScroll = currentScroll;
});

// Intersection Observer for Scroll Animations
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, {
    threshold: 0.1
});

document.querySelectorAll('.scroll-section').forEach((section) => {
    observer.observe(section);
});

// Parallax Effect
window.addEventListener('scroll', () => {
    const parallax = document.querySelector('.hero-bg');
    if (parallax) {
        const scrolled = window.pageYOffset;
        parallax.style.transform = `translate3d(0, ${scrolled * 0.5}px, 0)`;
    }
});

// Form Validation Enhancement
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!form.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
            
            // Add custom validation UI
            form.querySelectorAll('input, textarea').forEach(input => {
                if (!input.checkValidity()) {
                    input.classList.add('is-invalid');
                    const feedback = document.createElement('div');
                    feedback.className = 'invalid-feedback';
                    feedback.textContent = input.validationMessage;
                    input.parentNode.appendChild(feedback);
                }
            });
        }
        form.classList.add('was-validated');
    });
});

// Dynamic Loading States
const buttons = document.querySelectorAll('button[type="submit"]');
buttons.forEach(button => {
    button.addEventListener('click', function() {
        if (this.form && this.form.checkValidity()) {
            this.classList.add('loading');
            this.innerHTML = `
                <span class="spinner"></span>
                <span class="loading-text">Processing...</span>
            `;
        }
    });
});

// Toast Notifications
function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type} animate__animated animate__fadeInUp`;
    toast.innerHTML = `
        <div class="toast-content">
            <i class="bx ${type === 'success' ? 'bx-check' : 'bx-x'}"></i>
            <span>${message}</span>
        </div>
    `;
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.remove('animate__fadeInUp');
        toast.classList.add('animate__fadeOutDown');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

// Initialize all Bootstrap tooltips and popovers
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    // Initialize popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })
});

// Scroll to Top Function
function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Show/Hide Scroll to Top button
window.addEventListener('scroll', () => {
    const fab = document.querySelector('.fab');
    if (window.scrollY > 300) {
        fab.classList.add('show');
    } else {
        fab.classList.remove('show');
    }
});

// Initialize AOS (Animate On Scroll)
AOS.init({
    duration: 1000,
    once: true,
    offset: 100
});

// Initialize Swiper for carousels
const swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    autoplay: {
        delay: 5000,
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    breakpoints: {
        640: {
            slidesPerView: 2,
        },
        768: {
            slidesPerView: 3,
        }
    }
});

// Initialize Vanilla Tilt for 3D hover effects
VanillaTilt.init(document.querySelectorAll(".tilt-card"), {
    max: 5,
    speed: 400,
    glare: true,
    "max-glare": 0.2,
});

// Sticky Navbar
const navbar = document.querySelector('.navbar');
let lastScroll = 0;

window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    // Add/remove sticky class
    if (currentScroll > 100) {
        navbar.classList.add('sticky');
    } else {
        navbar.classList.remove('sticky');
    }

    // Hide/show navbar on scroll
    if (currentScroll > lastScroll && currentScroll > 100) {
        navbar.style.transform = 'translateY(-100%)';
    } else {
        navbar.style.transform = 'translateY(0)';
    }

    lastScroll = currentScroll;
});

// Handle mobile navigation animations
document.addEventListener('DOMContentLoaded', function() {
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');

    navbarToggler.addEventListener('click', function() {
        // Toggle icon
        const icon = this.querySelector('i');
        icon.classList.toggle('bx-menu');
        icon.classList.toggle('bx-x');
    });

    // Handle collapse animation
    navbarCollapse.addEventListener('show.bs.collapse', function () {
        this.classList.add('showing');
        setTimeout(() => this.classList.add('show'), 0);
    });

    navbarCollapse.addEventListener('hide.bs.collapse', function () {
        this.classList.remove('show');
        this.classList.remove('showing');
    });

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!navbarCollapse.contains(e.target) && !navbarToggler.contains(e.target)) {
            if (navbarCollapse.classList.contains('show')) {
                navbarToggler.click();
            }
        }
    });
}); 