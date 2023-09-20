/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./app/templates/**/*.{html,jinja2}",
        "./app/static/js/**/*.js"
    ],
    theme: {
        extend: {
            backgroundImage: {
                // Background image for hero section
                "hero-image": "url('/static/images/bg-hero.jpg')",
            }
        },
    },
    plugins: [],
}
