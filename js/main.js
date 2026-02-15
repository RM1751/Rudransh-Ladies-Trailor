/**
 * Rudransh Tailoring - Main JavaScript
 */

// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            navToggle.textContent = navMenu.classList.contains('active') ? '✕' : '☰';
        });

        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.textContent = '☰';
            });
        });
    }
});

// Form Validation and WhatsApp Integration
function initBookingForm() {
    const form = document.getElementById('bookingForm');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Validate form
        if (!validateForm(form)) {
            return;
        }

        // Collect form data
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        // Generate WhatsApp message
        const message = generateWhatsAppMessage(data);
        
        // Create WhatsApp URL
        const whatsappUrl = `https://wa.me/918840586403?text=${encodeURIComponent(message)}`;
        
        // Open WhatsApp
        window.open(whatsappUrl, '_blank');

        // Show success message
        showAlert('Form submitted! Opening WhatsApp...', 'success');
        
        // Optional: Reset form
        form.reset();
    });
}

// Form Validation
function validateForm(form) {
    let isValid = true;
    const requiredFields = form.querySelectorAll('[required]');

    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            isValid = false;
            field.style.borderColor = '#dc3545';
            
            // Remove error style on input
            field.addEventListener('input', function() {
                this.style.borderColor = '';
            }, { once: true });
        }
    });

    // Validate phone number (Indian format)
    const phoneField = form.querySelector('input[type="tel"]');
    if (phoneField && phoneField.value) {
        const phoneRegex = /^[6-9]\d{9}$/;
        const cleanPhone = phoneField.value.replace(/\D/g, '');
        
        if (!phoneRegex.test(cleanPhone)) {
            isValid = false;
            phoneField.style.borderColor = '#dc3545';
            showAlert('Please enter a valid 10-digit phone number', 'error');
        }
    }

    return isValid;
}

// Generate WhatsApp Message
function generateWhatsAppMessage(data) {
    const timestamp = new Date().toLocaleString('en-IN');
    
    let message = `*New Booking - Rudransh Tailoring*\n`;
    message += `*Date:* ${timestamp}\n\n`;
    
    message += `*Customer Details:*\n`;
    message += `👤 Name: ${data.customer_name || 'N/A'}\n`;
    message += `📞 Phone: ${data.phone_number || 'N/A'}\n`;
    if (data.email) message += `📧 Email: ${data.email}\n`;
    message += `🏠 Address: ${data.address || 'N/A'}\n\n`;
    
    message += `*Order Details:*\n`;
    message += `👗 Garment Type: ${data.garment_type || 'N/A'}\n`;
    if (data.style_preference) message += `✂️ Style: ${data.style_preference}\n`;
    message += `📏 Measurements:\n`;
    if (data.bust) message += `   • Bust: ${data.bust} ${data.unit || 'inches'}\n`;
    if (data.waist) message += `   • Waist: ${data.waist} ${data.unit || 'inches'}\n`;
    if (data.hip) message += `   • Hip: ${data.hip} ${data.unit || 'inches'}\n`;
    if (data.shoulder) message += `   • Shoulder: ${data.shoulder} ${data.unit || 'inches'}\n`;
    if (data.arm_length) message += `   • Arm Length: ${data.arm_length} ${data.unit || 'inches'}\n`;
    if (data.length) message += `   • Length: ${data.length} ${data.unit || 'inches'}\n`;
    if (data.sleeve_length) message += `   • Sleeve Length: ${data.sleeve_length} ${data.unit || 'inches'}\n`;
    if (data.neck_depth) message += `   • Neck Depth: ${data.neck_depth} ${data.unit || 'inches'}\n`;
    
    message += `\n*Additional Info:*\n`;
    message += `🧵 Fabric Provided: ${data.fabric_provided === 'on' ? 'Yes' : 'No'}\n`;
    message += `🚚 Pickup Required: ${data.pickup_required === 'on' ? 'Yes' : 'No'}\n`;
    message += `📦 Delivery Required: ${data.delivery_required === 'on' ? 'Yes' : 'No'}\n`;
    if (data.preferred_date) message += `📅 Preferred Date: ${data.preferred_date}\n`;
    if (data.special_instructions) message += `📝 Special Instructions: ${data.special_instructions}\n`;
    
    message += `\nThank you for choosing Rudransh Tailoring! 🙏`;
    
    return message;
}

// Show Alert Message
function showAlert(message, type) {
    // Remove existing alerts
    const existingAlert = document.querySelector('.alert');
    if (existingAlert) {
        existingAlert.remove();
    }

    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;

    const form = document.getElementById('bookingForm');
    if (form) {
        form.insertBefore(alert, form.firstChild);
    }

    // Auto remove after 5 seconds
    setTimeout(() => {
        alert.remove();
    }, 5000);
}

// Gallery Filter
function initGalleryFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');

            const filter = this.getAttribute('data-filter');

            galleryItems.forEach(item => {
                const category = item.getAttribute('data-category');
                
                if (filter === 'all' || category === filter) {
                    item.style.display = 'block';
                    item.style.animation = 'fadeIn 0.5s';
                } else {
                    item.style.display = 'none';
                }
            });
        });
    });
}

// Smooth Scroll for anchor links
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Initialize all functions when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initBookingForm();
    initGalleryFilter();
    initSmoothScroll();
});

// Add fadeIn animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);
