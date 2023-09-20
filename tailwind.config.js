/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./app/templates/**/*.{html,jinja2}",
        "./app/static/js/**/*.js"
    ],
    theme: {
        extend: {
            backgroundImage: {
                "hero-image": "url('/static/images/bg-hero.jpg')",
            }
        },
    },
    plugins: [],
}
