document.addEventListener("DOMContentLoaded", function() {
    
    // Handle example prompt clicking
    const prompts = document.querySelectorAll('.prompt-badge');
    const textarea = document.getElementById('user_input');
    
    prompts.forEach(prompt => {
        prompt.addEventListener('click', function() {
            textarea.value = this.innerText;
            textarea.focus();
        });
    });

    // Loading state for form submission
    const form = document.getElementById('mealForm');
    const submitBtn = document.getElementById('submitBtn');

    if(form) {
        form.addEventListener('submit', function() {
            submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Generating...';
            submitBtn.disabled = true;
        });
    }
});
