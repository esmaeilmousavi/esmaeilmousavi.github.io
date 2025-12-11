/**
 * OpenAI-Style Smooth Scroll Animations
 * Handles intersection observer for fade-in effects on photos and content
 */

(function() {
  'use strict';

  // Configuration
  const CONFIG = {
    threshold: 0.15,
    rootMargin: '0px 0px -100px 0px',
    animationClass: 'visible',
    animatedElements: '.animate-on-scroll, .gallery-photo, .mosaic-item, .side-photo'
  };

  // Create intersection observer
  function createObserver() {
    const options = {
      root: null,
      rootMargin: CONFIG.rootMargin,
      threshold: CONFIG.threshold
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Add visible class with slight delay for smoother effect
          setTimeout(() => {
            entry.target.classList.add(CONFIG.animationClass);
            entry.target.classList.add('animate-in');
          }, 100);
          
          // Once element is visible, stop observing it
          observer.unobserve(entry.target);
        }
      });
    }, options);

    return observer;
  }

  // Initialize animations on DOM ready
  function init() {
    // Wait for DOM to be fully loaded
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', startAnimations);
    } else {
      startAnimations();
    }
  }

  // Start observing all animated elements
  function startAnimations() {
    const observer = createObserver();
    const elements = document.querySelectorAll(CONFIG.animatedElements);
    
    elements.forEach((element, index) => {
      // Add slight stagger effect based on index
      element.style.transitionDelay = `${index * 0.05}s`;
      observer.observe(element);
    });

    // Add parallax effect to main profile image
    addParallaxEffect();
    
    // Add smooth scroll to gallery
    setupGalleryScroll();
  }

  // Subtle parallax effect on scroll
  function addParallaxEffect() {
    const parallaxElements = document.querySelectorAll('.parallax-photo');
    
    if (parallaxElements.length === 0) return;

    let ticking = false;

    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          const scrolled = window.pageYOffset;
          
          parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
          });
          
          ticking = false;
        });
        
        ticking = true;
      }
    });
  }

  // Setup smooth scroll behavior for photo gallery
  function setupGalleryScroll() {
    const galleries = document.querySelectorAll('.inline-photo-gallery');
    
    galleries.forEach(gallery => {
      let isDown = false;
      let startX;
      let scrollLeft;

      gallery.addEventListener('mousedown', (e) => {
        isDown = true;
        gallery.style.cursor = 'grabbing';
        startX = e.pageX - gallery.offsetLeft;
        scrollLeft = gallery.scrollLeft;
      });

      gallery.addEventListener('mouseleave', () => {
        isDown = false;
        gallery.style.cursor = 'grab';
      });

      gallery.addEventListener('mouseup', () => {
        isDown = false;
        gallery.style.cursor = 'grab';
      });

      gallery.addEventListener('mousemove', (e) => {
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - gallery.offsetLeft;
        const walk = (x - startX) * 2;
        gallery.scrollLeft = scrollLeft - walk;
      });

      // Add grab cursor
      gallery.style.cursor = 'grab';
    });
  }

  // Shuffle array randomly
  function shuffleArray(array) {
    const newArray = [...array];
    for (let i = newArray.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [newArray[i], newArray[j]] = [newArray[j], newArray[i]];
    }
    return newArray;
  }

  // Get random photos from the available set
  function getRandomPhotos(count) {
    const photos = [
      'IMG_4505.jpg', 'IMG_4506.jpg', 'IMG_4507.jpg', 'IMG_4509.jpg',
      'IMG_4510.jpg', 'IMG_4511.jpg', 'IMG_4512.jpg', 'IMG_4514.jpg',
      'IMG_4515.jpg', 'IMG_4517.jpg', 'IMG_4518.jpg', 'IMG_4520.jpg',
      'IMG_4521.jpg', 'IMG_4522.jpg', 'IMG_4524.jpg', 'IMG_4525.jpg'
    ];
    
    return shuffleArray(photos).slice(0, count);
  }

  // Create photo gallery dynamically
  function createPhotoGallery() {
    // Find the Biography section
    const biographySection = document.querySelector('h2');
    if (!biographySection || biographySection.textContent.trim() !== 'Biography') return;

    // Create gallery container
    const gallery = document.createElement('div');
    gallery.className = 'inline-photo-gallery';
    
    // Get 8 random photos
    const photos = getRandomPhotos(8);
    
    photos.forEach(photo => {
      const photoContainer = document.createElement('div');
      photoContainer.className = 'gallery-photo animate-on-scroll';
      
      const img = document.createElement('img');
      img.src = `../images/${photo}`;
      img.alt = 'Esmaeil Mousavi';
      img.loading = 'lazy';
      
      photoContainer.appendChild(img);
      gallery.appendChild(photoContainer);
    });
    
    // Insert after Work Experience section
    const workExperienceTable = document.querySelector('h2:nth-of-type(2)');
    if (workExperienceTable && workExperienceTable.nextElementSibling) {
      const tableElement = workExperienceTable.nextElementSibling;
      tableElement.parentNode.insertBefore(gallery, tableElement.nextSibling);
    }
  }

  // Create photo mosaic for achievements section
  function createPhotoMosaic() {
    // Find the achievements section
    const achievementsSection = document.querySelector('h2[paraeid*="ACADEMIC"]');
    if (!achievementsSection) return;

    // Create mosaic container
    const mosaic = document.createElement('div');
    mosaic.className = 'photo-mosaic';
    
    // Get remaining photos (different from gallery)
    const photos = getRandomPhotos(8);
    
    photos.forEach(photo => {
      const mosaicItem = document.createElement('div');
      mosaicItem.className = 'mosaic-item animate-on-scroll';
      
      const img = document.createElement('img');
      img.src = `../images/${photo}`;
      img.alt = 'Esmaeil Mousavi - Professional Activities';
      img.loading = 'lazy';
      
      mosaicItem.appendChild(img);
      mosaic.appendChild(mosaicItem);
    });
    
    // Insert before the footer
    const footer = document.querySelector('.footer');
    if (footer) {
      footer.parentNode.insertBefore(mosaic, footer);
    }
  }

  // Public initialization
  window.EsmaeilAnimations = {
    init: init,
    createPhotoGallery: createPhotoGallery,
    createPhotoMosaic: createPhotoMosaic
  };

  // Auto-initialize
  init();
  
  // Add photos after DOM is loaded
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      createPhotoGallery();
      createPhotoMosaic();
    });
  } else {
    createPhotoGallery();
    createPhotoMosaic();
  }

})();

