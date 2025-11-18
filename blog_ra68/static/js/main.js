// Dark Mode Toggle
const themeToggle = document.getElementById('darkModeToggle');
if (themeToggle) {
    themeToggle.addEventListener('change', () => {
        const isDark = themeToggle.checked;
        document.documentElement.classList.toggle('dark', isDark);
        document.documentElement.classList.toggle('light', !isDark);
        document.cookie = `theme=${isDark ? 'dark' : 'light'}; path=/; max-age=31536000; SameSite=Lax`;
    });
}

// Reading Progress Bar
window.addEventListener('scroll', () => {
    const scrolled = (window.pageYOffset / (document.body.offsetHeight - window.innerHeight)) * 100;
    document.getElementById('readingProgress').style.width = scrolled + '%';
});

// Back to Top Button
const backToTop = document.getElementById('backToTop');
if (backToTop) {
    backToTop.addEventListener('click', (e) => {
        e.preventDefault();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    window.addEventListener('scroll', () => {
        backToTop.classList.toggle('show', window.pageYOffset > 300);
    });
}

// Lazy Load Images
document.addEventListener('DOMContentLoaded', () => {
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src || img.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        document.querySelectorAll('img.lazy').forEach(img => imageObserver.observe(img));
    }
});

// Smooth Scrolling for Anchors
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// Video Autoplay on Viewport (for MP4)
document.querySelectorAll('video').forEach(video => {
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                video.play().catch(() => {}); // Autoplay if allowed
            } else {
                video.pause();
            }
        });
    });
    observer.observe(video);
});

// Search Form Enhancement
const searchForm = document.querySelector('form[role="search"]');
if (searchForm) {
    searchForm.addEventListener('submit', (e) => {
        const query = searchForm.querySelector('input[name="q"]').value.trim();
        if (!query) {
            e.preventDefault();
            alert('Please enter a search term.');
        }
    });
}
