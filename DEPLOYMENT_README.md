# Portfolio Django App - Vercel Deployment Setup

✅ **Your project is now configured for Vercel deployment!**

## What's Been Done

### 1. **Vercel Configuration**
- ✅ Created `vercel.json` with serverless function configuration
- ✅ Created `api/index.py` as the WSGI handler for Vercel
- ✅ Configured build process with static file collection

### 2. **Security Hardening**
- ✅ Environment variables for all sensitive data
- ✅ Removed hardcoded credentials (SECRET_KEY, database, email)
- ✅ Production-safe DEBUG setting
- ✅ ALLOWED_HOSTS configuration via environment

### 3. **Dependencies Updated**
- ✅ Added `gunicorn` for WSGI server
- ✅ Added `whitenoise` for static file serving
- ✅ Added `django-cors-headers` for API security
- ✅ Production-ready requirements.txt

### 4. **Production Settings**
- ✅ Support for PostgreSQL database (required for production)
- ✅ Email configuration via environment variables
- ✅ CORS configuration for API endpoints
- ✅ Static files handling with WhiteNoise

---

## 🚀 Quick Start Guide

### Phase 1: Local Setup
```bash
# Activate your virtual environment
source env/bin/activate

# Copy environment variables template
cp .env.example .env.local

# Update .env.local with your values
nano .env.local

# Install new dependencies
pip install -r requirements.txt

# Test locally
python manage.py runserver
```

### Phase 2: Database Setup (REQUIRED for Production)

Choose one of these PostgreSQL providers:

**Option A: Neon (Recommended)**
1. Sign up at https://neon.tech
2. Create a database
3. Copy connection string: `postgresql://user:password@host/database`

**Option B: Supabase**
1. Go to https://supabase.com
2. Create a new project
3. Find connection string in Settings → Database

**Option C: AWS RDS**
1. Create PostgreSQL instance
2. Allow Vercel IPs in security group
3. Get connection details

### Phase 3: Vercel Deployment

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Login
vercel login

# 3. Deploy from your project directory
cd portfolio_site
vercel --prod
```

### Phase 4: Environment Variables on Vercel

1. Go to Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add these variables:

```
SECRET_KEY=<your-secret-key-from-python-manage.py-shell>
DEBUG=False
ALLOWED_HOSTS=<your-domain>.vercel.app

DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=<db-name>
DATABASE_USER=<db-user>
DATABASE_PASSWORD=<db-password>
DATABASE_HOST=<db-host>
DATABASE_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=<your-email@gmail.com>
EMAIL_HOST_PASSWORD=<your-app-password>

CORS_ALLOWED_ORIGINS=<your-domain>.vercel.app
```

### Phase 5: Run Migrations

After deployment, run migrations on the production database:

```bash
# Option 1: Using Vercel CLI
vercel --prod env pull .env.production
source .env.production
python manage.py migrate

# Option 2: Via Vercel deployment hook (recommended)
# Add to vercel.json:
{
  "buildCommand": "pip install -r requirements.txt && python manage.py collectstatic --noinput",
  "env": {
    "PYTHONUNBUFFERED": "1"
  }
}
```

---

## 🔧 Configuration Files Created

| File | Purpose |
|------|---------|
| `vercel.json` | Vercel deployment config |
| `api/index.py` | WSGI handler for serverless |
| `.env.example` | Template for environment variables |
| `build.sh` | Build script for deployment |
| `migrate.sh` | Script to run migrations |
| `VERCEL_DEPLOYMENT.md` | Detailed deployment guide |

---

## 📝 Key Environment Variables

### Required
- `SECRET_KEY` - Django secret key
- `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, `DATABASE_PORT` - Database credentials
- `ALLOWED_HOSTS` - Your domain

### Optional
- `DEBUG` - Set to `False` in production (default)
- `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD` - For email functionality
- `CORS_ALLOWED_ORIGINS` - API CORS allowed origins

---

## 🔍 Testing Your Deployment

After deploying to Vercel:

```bash
# Test homepage
curl https://your-domain.vercel.app/

# Test admin panel
curl https://your-domain.vercel.app/admin/

# Test API
curl https://your-domain.vercel.app/api/projects/

# Check logs
vercel logs
```

---

## ⚠️ Important Notes

### Database
- **Never use SQLite in production** - Vercel filesystem is ephemeral
- Must use PostgreSQL or equivalent hosted service
- Initialize database before first deployment

### Static Files
- Handled by WhiteNoise middleware
- Run `python manage.py collectstatic` during build
- Media files should use external storage (S3, Cloudinary)

### Cold Starts
- First request after deployment ~2-3 seconds (normal)
- Subsequent requests are faster
- Consider using scheduler for warm-up

### Media Files (Optional but Recommended)
```bash
# Install S3 support
pip install django-storages boto3

# Then configure in settings.py
USE_S3=True
AWS_ACCESS_KEY_ID=...
```

---

## 🐛 Troubleshooting

### Static files not loading
```bash
# Rebuild locally
python manage.py collectstatic --clear --noinput
```

### Database connection errors
- Verify DATABASE_HOST is accessible
- Check firewall allows Vercel IPs: https://vercel.com/docs/concepts/infrastructure/edge-network#ip-addresses
- Test connection locally first

### Import errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### 500 errors on Vercel
```bash
# Check logs
vercel logs <deployment-id>
```

---

## 📚 Useful Resources

- [Vercel Django Docs](https://vercel.com/docs/examples/django)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Neon PostgreSQL](https://neon.tech/docs)
- [Django Settings Best Practices](https://docs.djangoproject.com/en/4.2/topics/settings/)

---

## ✅ Checklist Before Going Live

- [ ] Generate new SECRET_KEY
- [ ] Set up PostgreSQL database
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Set up email credentials
- [ ] Test migrations
- [ ] Test admin panel login
- [ ] Test API endpoints
- [ ] Set up domain/custom URL
- [ ] Enable HTTPS (automatic with Vercel)
- [ ] Set up error tracking (Sentry)
- [ ] Configure monitoring

---

## Need Help?

Check the detailed guide: `VERCEL_DEPLOYMENT.md`

For Vercel-specific issues: https://vercel.com/support
For Django issues: https://stackoverflow.com/questions/tagged/django
