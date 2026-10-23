/**
 * Main JavaScript for Tamsui Church Shao-nian System
 * Mobile-first web app with bottom navigation
 */

document.addEventListener('DOMContentLoaded', function () {
  console.log('Tamsui Church Shao-nian System loaded');

  // Add fade-in animation to content
  const content = document.querySelector('#app');
  if (content) {
    content.classList.add('fade-in');
  }

  // Handle button clicks with visual feedback
  const buttons = document.querySelectorAll('button');
  buttons.forEach(button => {
    button.addEventListener('click', function () {
      this.style.transform = 'scale(0.95)';
      setTimeout(() => {
        this.style.transform = 'scale(1)';
      }, 100);
    });
  });
});

/**
 * Show toast notification
 */
function showToast(message, duration = 3000) {
  const toast = document.createElement('div');
  toast.className = 'fixed bottom-24 left-1/2 transform -translate-x-1/2 bg-gray-800 text-white px-6 py-3 rounded-lg shadow-lg z-50 fade-in';
  toast.textContent = message;
  document.body.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = '0';
    toast.style.transition = 'opacity 0.3s';
    setTimeout(() => {
      toast.remove();
    }, 300);
  }, duration);
}

/**
 * Format date helper
 */
function formatDate(dateString) {
  const date = new Date(dateString);
  return date.toLocaleDateString('zh-TW', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit'
  });
}

