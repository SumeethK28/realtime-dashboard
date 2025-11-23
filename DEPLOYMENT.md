# 🚀 Deployment Guide - Render + MongoDB Atlas

## 🎯 Quick Start (10 Minutes)

### Step 1: MongoDB Atlas Setup (3 min)
1. Create free account: https://www.mongodb.com/cloud/atlas/register
2. Create FREE cluster → AWS → Any region
3. Create user + password → Save credentials!
4. Network Access → Allow 0.0.0.0/0
5. Get connection string → Save it!

### Step 2: Push to GitHub (2 min)
```bash
git init
git branch -m main
git add .
git commit -m "Real-Time Dashboard - MongoDB NoSQL"
# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/realtime-dashboard.git
git push -u origin main
```

### Step 3: Deploy to Render (5 min)
1. Sign up: https://render.com
2. New Web Service → Connect GitHub repo
3. Build: `./build.sh` | Start: `gunicorn dashboard_project.wsgi:application`
4. Add environment variables (see below)
5. Deploy! 🎉

**Environment Variables:**
- `MONGODB_URI`: Your Atlas connection string
- `SECRET_KEY`: Generate random (click Generate)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `.onrender.com`
- `MONGODB_DB_NAME`: `realtime_dashboard`

---

## 📚 Detailed Guide

## Prerequisites
- GitHub account
- Render account (free): https://render.com
- MongoDB Atlas account (free): https://mongodb.com/cloud/atlas

---

## Step 1: Setup MongoDB Atlas (Free Tier)

### 1.1 Create MongoDB Atlas Account
1. Go to https://www.mongodb.com/cloud/atlas/register
2. Sign up for a free account
3. Create a new organization (if needed)

### 1.2 Create a Free Cluster
1. Click "Build a Database"
2. Choose **FREE** tier (M0 Sandbox)
3. Select cloud provider: **AWS** (recommended)
4. Select region: Choose one closest to you
5. Cluster Name: `realtime-dashboard-cluster`
6. Click "Create"

### 1.3 Create Database User
1. In Security tab, click "Database Access"
2. Click "Add New Database User"
3. Authentication Method: **Password**
4. Username: `dashboard_user`
5. Password: Generate a secure password (save it!)
6. Database User Privileges: **Read and write to any database**
7. Click "Add User"

### 1.4 Whitelist IP Addresses
1. In Security tab, click "Network Access"
2. Click "Add IP Address"
3. Click "Allow Access from Anywhere" (for Render)
4. IP Address: `0.0.0.0/0`
5. Click "Confirm"

### 1.5 Get Connection String
1. Click "Database" in left sidebar
2. Click "Connect" on your cluster
3. Choose "Connect your application"
4. Driver: **Python**, Version: **3.11 or later**
5. Copy the connection string:
   ```
   mongodb+srv://dashboard_user:<password>@realtime-dashboard-cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
6. Replace `<password>` with your actual password
7. **Save this connection string** - you'll need it for Render!

---

## Step 2: Prepare GitHub Repository

### 2.1 Create .gitignore
```bash
# Create .gitignore file
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
bda/
env/
venv/
ENV/
build/
dist/
*.egg-info/

# Django
*.log
db.sqlite3
staticfiles/
media/

# Environment variables
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF
```

### 2.2 Initialize Git and Push to GitHub
```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Real-Time Dashboard with MongoDB"

# Create repository on GitHub (via web interface):
# 1. Go to https://github.com/new
# 2. Repository name: realtime-dashboard
# 3. Make it Public or Private
# 4. Click "Create repository"

# Add remote and push (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/realtime-dashboard.git
git branch -M main
git push -u origin main
```

---

## Step 3: Deploy to Render

### 3.1 Create Render Account
1. Go to https://render.com
2. Sign up with GitHub (recommended)

### 3.2 Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `realtime-dashboard`
3. Configure the service:

**Basic Settings:**
- Name: `realtime-dashboard`
- Runtime: `Python 3`
- Build Command: `./build.sh`
- Start Command: `gunicorn dashboard_project.wsgi:application`

**Advanced Settings:**

| Environment Variable | Value |
|---------------------|-------|
| `PYTHON_VERSION` | `3.12.0` |
| `SECRET_KEY` | (Generate random key - click "Generate") |
| `DEBUG` | `False` |
| `MONGODB_URI` | (Paste your MongoDB Atlas connection string) |
| `MONGODB_DB_NAME` | `realtime_dashboard` |
| `ALLOWED_HOSTS` | `.onrender.com` |

### 3.3 Environment Variables Details

**MONGODB_URI Example:**
```
mongodb+srv://dashboard_user:YOUR_PASSWORD@realtime-dashboard-cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority
```

**SECRET_KEY:** Click "Generate" button in Render or use:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3.4 Deploy
1. Click "Create Web Service"
2. Render will automatically:
   - Clone your repository
   - Run `build.sh` (install dependencies, collect static files)
   - Start gunicorn server
3. Wait 3-5 minutes for deployment
4. Your app will be live at: `https://realtime-dashboard.onrender.com`

---

## Step 4: Run Data Generator (Optional)

### Option A: Run Locally and Connect to Cloud MongoDB
```bash
# Update .env file with MongoDB Atlas connection
MONGODB_URI=mongodb+srv://dashboard_user:YOUR_PASSWORD@cluster.mongodb.net/
MONGODB_DB_NAME=realtime_dashboard

# Run data generator locally
source bda/bin/activate
python manage.py generate_data
```

### Option B: Create Background Worker on Render (Paid Plan Required)
1. Go to Render Dashboard
2. Click "New +" → "Background Worker"
3. Select same repository
4. Start Command: `python manage.py generate_data`
5. Use same environment variables
6. Deploy

---

## Step 5: Verify Deployment

### 5.1 Check Application
1. Visit: `https://YOUR_APP_NAME.onrender.com`
2. Dashboard should load (may show "--" values if no data generator running)

### 5.2 Check Logs
1. In Render dashboard, click "Logs" tab
2. Look for:
   ```
   Starting gunicorn...
   Listening at: http://0.0.0.0:10000
   ```

### 5.3 Test API
Visit: `https://YOUR_APP_NAME.onrender.com/api/all-data/`
Should return JSON (empty arrays if no data generated yet)

---

## Troubleshooting

### Issue: Build Failed
- Check `build.sh` has executable permissions
- Check `requirements.txt` is valid
- Review build logs in Render

### Issue: Application Error
- Check environment variables are set correctly
- Verify MongoDB connection string
- Check Django logs in Render

### Issue: Static Files Not Loading
- Ensure `whitenoise` is in requirements.txt
- Verify `STATIC_ROOT` in settings.py
- Check build log for "collectstatic" success

### Issue: MongoDB Connection Failed
- Verify connection string format
- Check MongoDB Atlas network access (allow 0.0.0.0/0)
- Verify database user credentials

---

## Post-Deployment

### Update Application
```bash
# Make changes to code
git add .
git commit -m "Update description"
git push origin main

# Render auto-deploys on push!
```

### View Logs
- Go to Render Dashboard → Your Service → Logs
- Real-time log streaming

### Custom Domain (Optional)
1. Go to Render Dashboard → Your Service → Settings
2. Click "Add Custom Domain"
3. Follow DNS configuration instructions

---

## Free Tier Limitations

### Render Free Tier:
- ✅ 750 hours/month
- ⚠️ Sleeps after 15 min inactivity (cold start ~30s)
- ✅ Automatic HTTPS
- ✅ Auto-deploy on git push

### MongoDB Atlas Free Tier:
- ✅ 512 MB storage
- ✅ Shared RAM
- ✅ Enough for this project
- ⚠️ 100 max connections

---

## Production Checklist

- [x] MongoDB Atlas cluster created
- [x] Database user created with password
- [x] Network access configured (0.0.0.0/0)
- [x] Connection string obtained
- [x] Code pushed to GitHub
- [x] Render web service created
- [x] Environment variables configured
- [x] Build successful
- [x] Application accessible
- [ ] Data generator running (optional)
- [ ] Custom domain configured (optional)

---

## Support Links

- **Render Documentation:** https://render.com/docs
- **MongoDB Atlas Docs:** https://docs.atlas.mongodb.com/
- **Django Deployment:** https://docs.djangoproject.com/en/stable/howto/deployment/

---

**🎉 Your Real-Time Dashboard is now live!**

Dashboard URL: `https://YOUR_APP_NAME.onrender.com`
