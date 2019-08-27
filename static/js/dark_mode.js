function set_dark_mode() {
    document.querySelector('body').classList.add('dark-mode');

    document.getElementById('mode-toggle').classList.replace('fa-moon-o', 'fa-sun-o');

    Array.from(document.getElementsByClassName('bg-light')).forEach(x => x.classList.replace('bg-light', 'bg-dark'))
}

function set_light_mode() {
    document.querySelector('body').classList.remove('dark-mode');

    document.getElementById('mode-toggle').classList.replace('fa-sun-o', 'fa-moon-o');

    Array.from(document.getElementsByClassName('bg-dark')).forEach(x => x.classList.replace('bg-dark', 'bg-light'))
}

function update_mode() {
    var current = (localStorage.getItem('lighting_display_mode') || 'light');

    if (current == 'dark') {
        set_dark_mode();
    } else {
        set_light_mode();
    }
}

function toggle_mode() {
    var current = (localStorage.getItem('lighting_display_mode') || 'light');
    var target;

    if (current == 'dark') {
        target = 'light';
    } else {
        target = 'dark';
    }

    localStorage.setItem('lighting_display_mode', target);

    update_mode();
}
