

document.addEventListener('DOMContentLoaded', () => {
    console.log('JavaScript Loaded');
    const container = document.querySelector(".container");
    const toggleButtonEle = document.getElementById('drawer-toggler')
    const drawer = document.getElementById('drawer')
    const navLinks = document.querySelectorAll(".nav-link");

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
     const observer = new IntersectionObserver((entries) => {
        // Filter visible entries
        const visible = entries.filter(entry => entry.isIntersecting);

        if (visible.length === 0) return;

        // Sort by vertical position on screen (top-most section first)
        visible.sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);

        // Pick the top-most section
        const topSection = visible[0].target;
        const id = topSection.getAttribute("id");

        // Remove active from all nav links
        navLinks.forEach(link => link.classList.remove("active"));

        // Add active to the matching nav links (both header and drawer)
        const matchingLinks = document.querySelectorAll(`.nav-link[href="#${id}"]`);
        matchingLinks.forEach(link => link.classList.add("active"));
    }, {
        root: container,
        // rootMargin: "-30% 0px -30% 0px",
        threshold: 0.1,
    });

    sections.forEach((section) => {
        console.log('section::', section)
        observer.observe(section);
    });
})