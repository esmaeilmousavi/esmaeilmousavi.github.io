/* ===================================
   PHOTO ANIMATIONS & GALLERY SYSTEM
   =================================== */

(function() {
  'use strict';

  // List of all photos
  const photos = [
    'IMG_4505.jpg', 'IMG_4506.jpg', 'IMG_4507.jpg', 'IMG_4509.jpg',
    'IMG_4510.jpg', 'IMG_4511.jpg', 'IMG_4512.jpg', 'IMG_4514.jpg',
    'IMG_4515.jpg', 'IMG_4517.jpg', 'IMG_4518.jpg', 'IMG_4520.jpg',
    'IMG_4521.jpg', 'IMG_4522.jpg', 'IMG_4524.jpg', 'IMG_4525.jpg'
  ];

  // ===================================
  // FLOATING PHOTOS BACKGROUND
  // ===================================
  function createFloatingPhotos() {
    const container = document.createElement('div');
    container.className = 'floating-photos';
    document.body.insertBefore(container, document.body.firstChild);

    // Create 8 floating photos at a time
    function spawnFloatingPhoto() {
      const img = document.createElement('img');
      const randomPhoto = photos[Math.floor(Math.random() * photos.length)];
      img.src = `../images/${randomPhoto}`;
      img.className = 'floating-photo';
      img.alt = 'Esmaeil Mousavi';
      
      // Random horizontal position
      const randomLeft = Math.random() * 90; // 0-90% to keep photos on screen
      img.style.left = randomLeft + '%';
      
      // Random animation duration (15-25 seconds)
      const duration = 15 + Math.random() * 10;
      img.style.animationDuration = duration + 's';
      
      // Random delay before starting
      const delay = Math.random() * 5;
      img.style.animationDelay = delay + 's';
      
      // Random size variation
      const size = 100 + Math.random() * 60; // 100-160px
      img.style.width = size + 'px';
      img.style.height = size + 'px';
      
      // Click to expand
      img.addEventListener('click', function() {
        expandPhoto(this.src);
      });
      
      container.appendChild(img);
      
      // Remove after animation completes
      setTimeout(() => {
        if (img.parentNode) {
          img.parentNode.removeChild(img);
        }
      }, (duration + delay) * 1000);
    }

    // Spawn initial batch
    for (let i = 0; i < 6; i++) {
      setTimeout(() => spawnFloatingPhoto(), i * 2000);
    }

    // Continuously spawn new photos
    setInterval(spawnFloatingPhoto, 8000);
  }

  // ===================================
  // PHOTO EXPANSION MODAL
  // ===================================
  function expandPhoto(src) {
    const modal = document.createElement('div');
    modal.style.cssText = `
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9);
      z-index: 10000;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      animation: fadeIn 0.3s ease;
    `;
    
    const img = document.createElement('img');
    img.src = src;
    img.style.cssText = `
      max-width: 90%;
      max-height: 90%;
      border-radius: 10px;
      box-shadow: 0 20px 80px rgba(0, 0, 0, 0.5);
      animation: zoomIn 0.4s ease;
    `;
    
    modal.appendChild(img);
    
    // Add animation keyframes
    const style = document.createElement('style');
    style.textContent = `
      @keyframes zoomIn {
        from { transform: scale(0.5); opacity: 0; }
        to { transform: scale(1); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
    
    modal.addEventListener('click', function() {
      modal.style.animation = 'fadeOut 0.3s ease';
      setTimeout(() => modal.remove(), 300);
    });
    
    document.body.appendChild(modal);
  }

  // ===================================
  // PHOTO GALLERY SECTION
  // ===================================
  function createPhotoGallery() {
    const contentBody = document.getElementById('contentBody');
    if (!contentBody) return;

    // Create gallery section
    const gallerySection = document.createElement('section');
    gallerySection.className = 'photo-gallery-section';
    gallerySection.innerHTML = `
      <h2>📸 Gallery</h2>
      <div class="photo-grid" id="photoGrid"></div>
    `;

    // Insert before the last section
    contentBody.appendChild(gallerySection);

    // Populate grid
    const grid = document.getElementById('photoGrid');
    photos.forEach(photo => {
      const card = document.createElement('div');
      card.className = 'photo-card';
      
      const img = document.createElement('img');
      img.src = `../images/${photo}`;
      img.alt = 'Esmaeil Mousavi - Gallery Photo';
      img.loading = 'lazy';
      
      img.addEventListener('click', function() {
        expandPhoto(this.src);
      });
      
      card.appendChild(img);
      grid.appendChild(card);
    });
  }

  // ===================================
  // SCROLL PROGRESS INDICATOR
  // ===================================
  function createScrollProgress() {
    const progressBar = document.createElement('div');
    progressBar.className = 'scroll-progress';
    document.body.appendChild(progressBar);

    window.addEventListener('scroll', function() {
      const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (window.scrollY / windowHeight) * 100;
      progressBar.style.width = scrolled + '%';
    });
  }

  // ===================================
  // SCROLL ANIMATIONS FOR ELEMENTS
  // ===================================
  function initScrollAnimations() {
    const contentBody = document.getElementById('contentBody');
    if (!contentBody) return;

    contentBody.classList.add('animated');

    const elements = contentBody.querySelectorAll('h1, h2, table, p');
    
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
        }
      });
    }, {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    });

    elements.forEach((el, index) => {
      el.style.transitionDelay = (index * 0.1) + 's';
      observer.observe(el);
    });
  }

  // ===================================
  // PARALLAX EFFECT ON SCROLL
  // ===================================
  function initParallax() {
    const sections = document.querySelectorAll('.main-content > div, section');
    
    window.addEventListener('scroll', function() {
      const scrolled = window.scrollY;
      
      sections.forEach((section, index) => {
        const speed = (index % 2 === 0) ? 0.5 : -0.3;
        const yPos = -(scrolled * speed);
        section.style.transform = `translateY(${yPos}px)`;
      });
    });
  }

  // ===================================
  // SMOOTH SCROLL FOR ANCHOR LINKS
  // ===================================
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#' || href === '') return;
        
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
          });
        }
      });
    });
  }

  // ===================================
  // ADD PULSE EFFECT TO IMPORTANT LINKS
  // ===================================
  function addPulseEffects() {
    const importantLinks = document.querySelectorAll('.fancy-link, .button');
    importantLinks.forEach(link => {
      link.classList.add('pulse-on-hover');
    });
  }

  // ===================================
  // LOADING ANIMATION
  // ===================================
  function createLoadingOverlay() {
    const overlay = document.createElement('div');
    overlay.className = 'loading-overlay';
    overlay.innerHTML = '<div class="loading-spinner"></div>';
    document.body.insertBefore(overlay, document.body.firstChild);
  }

  // ===================================
  // ADD HOVER EFFECTS TO TABLES
  // ===================================
  function enhanceTableAnimations() {
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
      const rows = table.querySelectorAll('tr');
      rows.forEach((row, index) => {
        row.style.animationDelay = (index * 0.05) + 's';
      });
    });
  }

  // ===================================
  // RANDOM DECORATIVE ELEMENTS
  // ===================================
  function addDecorativeElements() {
    // Add subtle animated background patterns
    const mainContent = document.querySelector('.main-content');
    if (!mainContent) return;

    const decorStyle = document.createElement('style');
    decorStyle.textContent = `
      .main-content::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
          radial-gradient(circle at 20% 50%, rgba(82, 45, 128, 0.03) 0%, transparent 50%),
          radial-gradient(circle at 80% 80%, rgba(124, 77, 255, 0.03) 0%, transparent 50%);
        pointer-events: none;
        z-index: -1;
        animation: backgroundShift 20s ease-in-out infinite;
      }
      
      @keyframes backgroundShift {
        0%, 100% { opacity: 0.5; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.1); }
      }
    `;
    document.head.appendChild(decorStyle);
  }

  // ===================================
  // INITIALIZE ALL ANIMATIONS
  // ===================================
  function init() {
    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', init);
      return;
    }

    createLoadingOverlay();
    createFloatingPhotos();
    createPhotoGallery();
    createScrollProgress();
    initScrollAnimations();
    // initParallax(); // Commented out as it might interfere with existing layout
    initSmoothScroll();
    addPulseEffects();
    enhanceTableAnimations();
    addDecorativeElements();

    console.log('🎨 Photo animations and UI enhancements loaded!');
  }

  // Run initialization
  init();

})();

