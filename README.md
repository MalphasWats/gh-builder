# gh-builder

GitHub Pages Builder - I hate this name, man I'm bad at names.

I started playing around with GitHub Pages, which I think are really handy for chucking stuff out there.

I was a little disappointed though that the auto-generator doesn't attach a style-sheet to the pages it builds from `.markdown` files, I'm still not sure this is how it is supposed to work, really seems like a missed opportunity.

EDIT: I worked out that I was being rather stupid, and I just needed to add the template information to the header at the top of the `.markdown` file.

Anyhow, I threw together a very simple Python script that will build `.markdown` files to templates found in the local directory using the Jinja2 templating engine.

I really like Jinja2, now I know how GH-P uses Jekyll templates, I wish I could use Jinja2 ones instead.

## Requirements

- markdown
- Jinja2