

document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript Loaded');

    const toggleButtonEle = document.getElementById('drawer-toggler')
    const drawer = document.getElementById('drawer')
    
    toggleButtonEle.addEventListener('click', e => {
        e.stopPropagation(); // 👈 prevent click from reaching #app
        drawer.classList.add('open')
    })
    drawer.addEventListener('click', e => {
        e.stopPropagation(); // 👈 optional, prevents closing when interacting inside drawer
    });

    document.addEventListener('click', e => {
        drawer.classList.remove('open')
    })
})