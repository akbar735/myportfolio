

document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript Loaded');
    const container = document.querySelector(".container");
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
    
    const sections = document.querySelectorAll(".page-section");
    const navLinks = document.querySelectorAll(".nav-link");
    
    function getVisiblePercentage(el) {
        const rect = el.getBoundingClientRect();
        const containerRect = container === window 
            ? { top: 0, bottom: window.innerHeight }
            : container.getBoundingClientRect();

        const visibleTop = Math.max(rect.top, containerRect.top);
        const visibleBottom = Math.min(rect.bottom, containerRect.bottom);
        const visibleHeight = Math.max(0, visibleBottom - visibleTop);

        return (visibleHeight / rect.height) * 100; // percent visible
    }

    function updateActiveSection() {
        let maxVisibleHeight = 0;
        let activeId = null;
        sections.forEach((section) => {
            const visibleHeight = getVisiblePercentage(section);
            console.log(section.getAttribute("id"), visibleHeight)
            if (visibleHeight > maxVisibleHeight) {
                maxVisibleHeight = visibleHeight;
                activeId = section.getAttribute("id");
            }
        });

        // Remove 'active' from all nav links
        navLinks.forEach((link) => link.classList.remove("active"));

        if (activeId) {
            document.querySelectorAll(`.nav-link[href="#${activeId}"]`)
                .forEach((link) => link.classList.add("active"));
        }
    }

    // Trigger on scroll and on load
    let scrollTimeout;
    container.addEventListener("scroll", () => {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(updateActiveSection, 50);
    });

    container.addEventListener("resize", updateActiveSection);
    updateActiveSection(); // run on initial load
   
})

