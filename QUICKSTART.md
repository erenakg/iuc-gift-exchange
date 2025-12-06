# 🚀 Quick Start Guide

## Step-by-Step Setup (For Django Beginners)

### 1. Open PowerShell
- Press `Win + X` and select "Windows PowerShell" or "Terminal"

### 2. Navigate to Project
```powershell
cd C:\gift_exchange
```

### 3. Create Virtual Environment
```powershell
python -m venv venv
```

### 4. Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```

**If you see an error about execution policy:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

### 5. Install Django
```powershell
pip install -r requirements.txt
```

### 6. Initialize Database
```powershell
python manage.py migrate
```

### 7. Run the Server
```powershell
python manage.py runserver
```

### 8. Open in Browser
Visit: **http://127.0.0.1:8000/**

---

## 🎉 That's It!

You should now see your beautiful New Year's landing page!

## 📝 Common Commands

### Stop the Server
Press `Ctrl + C` in the terminal

### Restart the Server
```powershell
python manage.py runserver
```

### Deactivate Virtual Environment
```powershell
deactivate
```

### Reactivate Later
```powershell
cd C:\gift_exchange
.\venv\Scripts\Activate.ps1
python manage.py runserver
```

## 🔍 Understanding What You See

### The Landing Page Includes:
1. **Animated snowflakes** falling across the screen
2. **Hero section** with festive title and subtitle
3. **Countdown timer** showing time until New Year's
4. **Call-to-action button** (currently shows an alert)
5. **Developer names** in the footer with beautiful styling

### File Structure You Created:
- `templates/landing/home.html` - The HTML structure
- `static/css/style.css` - All the styling and animations
- `static/js/countdown.js` - Countdown timer logic
- `landing/views.py` - Django view that renders the page
- `landing/urls.py` - URL routing for the landing app

## 🎨 Making Changes

### To Change Text
1. Open `templates/landing/home.html`
2. Find the text you want to change
3. Edit and save
4. Refresh your browser (no need to restart server!)

### To Change Colors
1. Open `static/css/style.css`
2. Find the `:root` section at the top
3. Change color values
4. Save and refresh browser

### To Change Countdown Target Date
1. Open `static/js/countdown.js`
2. Find `const newYear = new Date(targetYear, 0, 1, 0, 0, 0);`
3. Change the date values
4. Save and refresh browser

## ❓ Troubleshooting

### "python is not recognized"
- Make sure Python is installed
- Download from: https://www.python.org/downloads/

### "Port already in use"
- Stop other Django servers
- Or use a different port: `python manage.py runserver 8080`

### "Template does not exist"
- Make sure you're in the `C:\gift_exchange` directory
- Check that `templates/landing/home.html` exists

### CSS/JS Not Loading
- Check that `static/css/style.css` exists
- Check that `static/js/countdown.js` exists
- Make sure `DEBUG = True` in `gift_exchange/settings.py`

## 🎯 Next Steps

1. **Test on Mobile**: Open on your phone to see responsive design
2. **Customize Colors**: Change the color scheme to your preference
3. **Add Sections**: Add new content between hero and footer
4. **Add Features**: When ready, add user authentication and gift exchange logic

---

**Need Help?** Check the full README.md for more detailed information!
