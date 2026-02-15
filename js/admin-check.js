/**
 * Admin Check Script - Shared across all pages
 * Shows/hides admin elements based on login state
 */

(function() {
    'use strict';

    // Check if admin is logged in
    function isAdminLoggedIn() {
        return sessionStorage.getItem('adminLoggedIn') === 'true';
    }

    // Show/hide admin elements
    function updateAdminUI() {
        const adminElements = document.querySelectorAll('[data-admin-only]');
        const customerElements = document.querySelectorAll('[data-customer-only]');
        
        if (isAdminLoggedIn()) {
            // Show admin-only elements
            adminElements.forEach(el => {
                el.style.display = el.getAttribute('data-admin-display') || 'inline-block';
            });
            // Hide customer-only elements if needed
            customerElements.forEach(el => {
                el.style.display = 'none';
            });
        } else {
            // Hide admin-only elements
            adminElements.forEach(el => {
                el.style.display = 'none';
            });
            // Show customer-only elements
            customerElements.forEach(el => {
                el.style.display = el.getAttribute('data-customer-display') || 'block';
            });
        }
    }

    // Add admin link to navigation
    function addAdminNavLink() {
        const navMenus = document.querySelectorAll('.nav-menu');
        
        navMenus.forEach(menu => {
            // Check if admin link already exists
            if (!menu.querySelector('.admin-nav-link')) {
                const adminLi = document.createElement('li');
                adminLi.className = 'admin-nav-link';
                adminLi.setAttribute('data-admin-only', '');
                adminLi.setAttribute('data-admin-display', 'inline-block');
                adminLi.style.display = 'none';
                adminLi.innerHTML = '<a href="admin.html" title="Admin Panel" style="background: #FFD700; color: #8B0000; padding: 8px 16px; border-radius: 20px; font-weight: 600;">&#128273; Admin</a>';
                
                // Add before the last item or at the end
                menu.appendChild(adminLi);
            }
        });
    }

    // Add admin floating button
    function addAdminFloatingButton() {
        if (document.getElementById('adminFab')) return;
        
        const fab = document.createElement('a');
        fab.id = 'adminFab';
        fab.href = 'admin.html';
        fab.className = 'fab-admin';
        fab.setAttribute('data-admin-only', '');
        fab.setAttribute('data-admin-display', 'flex');
        fab.style.cssText = 'display: none; position: fixed; bottom: 100px; right: 20px; width: 56px; height: 56px; background: #FFD700; color: #8B0000; border-radius: 50%; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.3); z-index: 9998; text-decoration: none; font-size: 1.5rem;';
        fab.title = 'Admin Panel';
        fab.innerHTML = '&#128273;';
        
        document.body.appendChild(fab);
    }

    // Initialize
    function init() {
        addAdminNavLink();
        addAdminFloatingButton();
        updateAdminUI();
        
        // Listen for storage changes (for multi-tab sync)
        window.addEventListener('storage', function(e) {
            if (e.key === 'adminLoggedIn') {
                updateAdminUI();
            }
        });
    }

    // Run on DOM ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    // Expose to global scope for manual triggering
    window.AdminCheck = {
        isLoggedIn: isAdminLoggedIn,
        updateUI: updateAdminUI
    };
})();
