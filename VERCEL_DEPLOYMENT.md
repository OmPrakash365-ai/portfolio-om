# Vercel Deployment Guide for Django Portfolio

## Prerequisites
1. Vercel account (https://vercel.com)
2. GitHub repository linked to Vercel
3. PostgreSQL database (Neon, Supabase, or AWS RDS)
4. Environment variables configured

## Step-by-Step Deployment

### 1. Prepare Your Repository
```bash
# Make sure all changes are committed
git add .
git commit -m "Setup Vercel deployment"
git push origin main
```

### 2. Generate Secret Key
```bash
python manage.py shell
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
Save this output - you'll need it for the environment variable.

### 3. Set Up Database
Choose one:
- **Neon** (Recommended for Vercel): https://neon.tech
- **Supabase**: https://supabase.com
- **AWS RDS**: https://aws.amazon.com/rds/

Get your database connection string and parse it into:
- DATABASE_ENGINE=django.db.backends.postgresql
- DATABASE_NAME
- DATABASE_USER
- DATABASE_PASSWORD
- DATABASE_HOST
- DATABASE_PORT

### 4. Deploy to Vercel
```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

### 5. Configure Environment Variables in Vercel Dashboard
1. Go to your project settings
2. Add environment variables:
   - `SECRET_KEY` - Generated in step 2
   - `DEBUG` - Set to `False`
   - `ALLOWED_HOSTS` - Your domain (e.g., `portfolio.vercel.app`)
   - Database variables (from step 3)
   - Email configuration

### 6. Run Database Migrations
```bash
# Connect via Vercel environment
vercel env pull .env.local

# Run migrations
python manage.py migrate
```

Or create a migration script:
```bash
vercel --prod env pull .env.production && \
python manage.py migrate --settings=portfolio_site.settings
```

### 7. Test Deployment
- Visit your Vercel URL
- Check admin panel: `https://your-domain.vercel.app/admin`
- Test API endpoints

## Troubleshooting

### Static Files Not Loading
- Ensure `STATIC_ROOT` is set
- Run `python manage.py collectstatic`
- Add to settings.py:
```python
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Database Connection Issues
- Verify DATABASE_HOST is accessible
- Check firewall rules allow Vercel IPs
- Test connection locally first

### Media Files
Consider using AWS S3 or similar for production:
```bash
pip install django-storages boto3
```

### Cold Starts
- Vercel serverless functions have cold starts
- Django startup time ~1-2 seconds is normal
- Consider using a background job service for async tasks

## Monitoring
1. Check Vercel logs: `vercel logs`
2. Monitor function duration and memory usage
3. Set up error tracking (Sentry, etc.)

## CI/CD
Vercel automatically deploys on push to main branch. 
To disable or change:
1. Project Settings → Git
2. Configure deployment branch and conditions
