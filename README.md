# Ahmed Abdullahi — Django portfolio

A responsive, project-driven portfolio with a home page, three project detail pages, downloadable resume, and real email, LinkedIn, and GitHub links. Content is based on the supplied resume; architecture diagrams are conceptual summaries, not application screenshots. No invented performance metrics or repository links are included.

## Run locally (PowerShell)

```powershell
python -m venv .venv
.venv/Scripts/python -m pip install -r requirements.txt
.venv/Scripts/python manage.py runserver 127.0.0.1:8021
```

Open http://127.0.0.1:8021. No database or migrations are required because this portfolio has no mutable records or contact form; contact opens the visitor's email application.

## Update content

- `portfolio/content.py`: profile, projects, skills, and experience.
- `templates/`: Django page templates.
- `static/styles.css`: responsive visual design.
- `static/Ahmed_Abdullahi_Resume.pdf`: downloadable original resume.

Project-specific repositories and screenshots were not provided. The site links to the verified GitHub profile and uses workflow diagrams. Add project repository URLs and screenshots when available.

## Verify

```powershell
.venv/Scripts/python manage.py check
.venv/Scripts/python manage.py test
.venv/Scripts/python manage.py collectstatic --noinput
.venv/Scripts/python manage.py export_site
```

## Deploy Django on CapRover

The Dockerfile serves the full Django app through Gunicorn and WhiteNoise on port 8021. `captain-definition` supports a CapRover Dockerfile deployment. Set container HTTP port to 8021. Use an HTTPS reverse proxy and configure a random `DJANGO_SECRET_KEY` and exact `DJANGO_ALLOWED_HOSTS`; debug is disabled in the container. The `.env.example` lists the environment settings; settings are read from the process environment, not automatically from this file.

In the CapRover dashboard:

1. Create or select the portfolio app and deploy this directory using `captain-definition`.
2. Under **HTTP Settings**, set **Container HTTP Port** to `8021` and save.
3. Under **App Config**, set `DJANGO_SECRET_KEY` to a long random value, `DJANGO_ALLOWED_HOSTS` to your portfolio hostname (without scheme or port), and `DJANGO_DEBUG=false`.
4. Enable HTTPS for the app. With CapRover's trusted Nginx proxy, set `DJANGO_TRUST_PROXY=true` and retain `DJANGO_SECURE_SSL_REDIRECT=true`.
5. Open the app's HTTPS domain. Public traffic uses HTTPS port 443; the application listens internally on 8021. No host port mapping is needed for domain-based access.

The Dockerfile configures the application port, but it cannot update CapRover's dashboard settings. See [CapRover app configuration](https://caprover.com/docs/app-configuration).

When a trusted reverse proxy terminates HTTPS, configure it to overwrite `X-Forwarded-Proto` and set `DJANGO_TRUST_PROXY=true`. Keep the app port accessible only to that proxy. This avoids redirect loops without trusting arbitrary forwarded headers.

On Windows, install the requirements and serve with `waitress-serve --listen=127.0.0.1:8021 config.wsgi:application` behind your HTTPS proxy, after collecting static assets. Set production environment variables and run `python manage.py check --deploy` before deployment. See the [Django deployment documentation](https://docs.djangoproject.com/en/5.2/howto/deployment/).

## Static hosted preview

`python manage.py export_site` renders the same Django templates into `dist/`. The Sites hosted version serves these exported pages; it does **not** run Python or Django on the server. The full Django source is the primary implementation and can be deployed separately to a Python-capable host. Re-export after editing content before updating the hosted preview. Run exports with local debug settings.

Fonts load from Google Fonts with system sans-serif fallbacks. The site works without JavaScript except for the compact mobile navigation menu.
