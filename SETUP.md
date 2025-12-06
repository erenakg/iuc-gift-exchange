# 🎄 Complete Setup Instructions

## 📋 Prerequisites Checklist

Before you begin, make sure you have:
- [ ] Python 3.8 or higher installed
- [ ] Internet connection (for downloading Django)
- [ ] Text editor or IDE (VS Code recommended)
- [ ] PowerShell or Terminal access

## 🚀 Installation Steps

### Step 1: Verify Python Installation
Open PowerShell and run:
```powershell
python --version
```
You should see Python 3.8 or higher.

**Don't have Python?** Download from: https://www.python.org/downloads/

### Step 2: Navigate to Project Directory
```powershell
cd C:\gift_exchange
```

### Step 3: Create Virtual Environment
```powershell
python -m venv venv
```
This creates an isolated Python environment for your project.

### Step 4: Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```

**If you get a "script execution" error:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Then try activating again.

**Success indicator:** Your prompt should now show `(venv)` at the beginning.

### Step 5: Install Django and Dependencies
```powershell
pip install -r requirements.txt
```
This installs Django 4.2 and any other required packages.

### Step 6: Initialize the Database
```powershell
python manage.py migrate
```
This creates the SQLite database and tables.

### Step 7: Start the Development Server
```powershell
python manage.py runserver
```

**Alternative method:**
```powershell
python run_server.py
```
This is a helper script that checks everything before starting.

### Step 8: Open in Browser
Visit: **http://127.0.0.1:8000/**

You should see your beautiful New Year's landing page! 🎉

## 📝 What You Should See

### In Your Browser:
1. **Animated snowflakes** falling across the screen
2. **Large festive title**: "New Year's Gift Exchange"
3. **Countdown timer** with days, hours, minutes, seconds
4. **Red "Start Your Exchange" button**
5. **Developer names** in the footer with colorful styling

### In Your Terminal:
```
System check identified no issues (0 silenced).
December 06, 2025 - 12:00:00
Django version 4.2.x, using settings 'gift_exchange.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## 🎯 Testing the Features

### Test 1: Countdown Timer
- Watch the seconds count down
- The countdown automatically targets January 1st
- When New Year arrives, it shows "Happy New Year!"

### Test 2: Responsive Design
- Resize your browser window
- Open on your phone (use your computer's IP address)
- Everything should adjust beautifully

### Test 3: Button Interaction
- Hover over the "Start Your Exchange" button
- Click it - you'll see a placeholder alert
- The button glows and grows on hover

### Test 4: Animations
- Watch the snowflakes fall
- Notice the pulsing glow around the countdown
- See the floating stars/sparkles around the page
- Hover over developer names to see them scale up

## 🔧 Common Issues and Solutions

### Issue 1: "python: command not found"
**Solution:** Python is not installed or not in PATH
- Install Python from https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

### Issue 2: "Execution policy" error when activating venv
**Solution:** PowerShell security settings
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue 3: "No module named 'django'"
**Solution:** Django not installed or wrong environment
```powershell
# Make sure (venv) is shown in your prompt
pip install -r requirements.txt
```

### Issue 4: Port 8000 already in use
**Solution:** Another Django server is running
```powershell
# Option 1: Stop the other server
# Option 2: Use a different port
python manage.py runserver 8080
```
Then visit: http://127.0.0.1:8080/

### Issue 5: Static files (CSS/JS) not loading
**Solution:** Check DEBUG setting
- Open `gift_exchange/settings.py`
- Ensure `DEBUG = True` for development
- Restart the server

### Issue 6: Template not found
**Solution:** Wrong directory or file missing
- Check that `templates/landing/home.html` exists
- Verify you're in the `C:\gift_exchange` directory
- Check `settings.py` has correct TEMPLATES configuration

## 📱 Testing on Mobile Devices

### Method 1: Using Device Emulation (Desktop)
1. Open the page in Chrome/Edge
2. Press F12 to open DevTools
3. Click the device icon (Toggle device toolbar)
4. Select different devices to test

### Method 2: Testing on Real Phone
1. Find your computer's IP address:
   ```powershell
   ipconfig
   ```
   Look for "IPv4 Address" (e.g., 192.168.1.100)

2. Start server allowing external access:
   ```powershell
   python manage.py runserver 0.0.0.0:8000
   ```

3. On your phone's browser, visit:
   ```
   http://YOUR_IP_ADDRESS:8000
   ```
   (Replace YOUR_IP_ADDRESS with the IP from step 1)

4. Make sure your phone and computer are on the same WiFi network

## 🎨 Making Your First Changes

### Change 1: Modify the Title
1. Open `templates/landing/home.html` in your text editor
2. Find this section:
   ```html
   <h1 class="main-title">
       <span class="title-line">New Year's</span>
       <span class="title-line highlight">Gift Exchange</span>
   </h1>
   ```
3. Change the text to whatever you want
4. Save the file
5. Refresh your browser (no need to restart server!)

### Change 2: Adjust Colors
1. Open `static/css/style.css`
2. Find the `:root` section at the top:
   ```css
   :root {
       --red-primary: #C41E3A;
       --green-primary: #0F5132;
       --gold: #FFD700;
   }
   ```
3. Change the color hex codes
4. Save and refresh browser

### Change 3: Button Text
1. Open `templates/landing/home.html`
2. Find:
   ```html
   <button class="cta-button">
       <span class="button-text">Start Your Exchange</span>
       <span class="button-icon">🎉</span>
   </button>
   ```
3. Change "Start Your Exchange" to your preferred text
4. Change the emoji if desired
5. Save and refresh

## 📚 Learning Resources

### Django Documentation
- Official Docs: https://docs.djangoproject.com/
- Tutorial: https://docs.djangoproject.com/en/4.2/intro/tutorial01/
- Templates: https://docs.djangoproject.com/en/4.2/topics/templates/

### CSS & JavaScript
- MDN Web Docs: https://developer.mozilla.org/
- CSS Tricks: https://css-tricks.com/
- JavaScript.info: https://javascript.info/

### This Project's Documentation
- `README.md` - Complete project overview
- `QUICKSTART.md` - Quick start guide
- `FEATURES.md` - Design and features documentation
- `SETUP.md` - This file

## 🎯 Next Steps

### Immediate Tasks:
1. [ ] Get the server running successfully
2. [ ] Test all features (countdown, animations, responsiveness)
3. [ ] Try making small changes to customize the page
4. [ ] Test on mobile device

### Short-term Goals:
1. [ ] Add more sections to the landing page
2. [ ] Customize colors and fonts to your preference
3. [ ] Add your own images or background patterns
4. [ ] Learn Django template syntax

### Long-term Goals:
1. [ ] Create user authentication system
2. [ ] Build gift exchange matching algorithm
3. [ ] Add database models for users and gifts
4. [ ] Implement email notifications
5. [ ] Deploy to a production server

## 💡 Tips for Success

1. **Keep the server running** while you work
   - Changes to HTML/CSS take effect immediately
   - Changes to Python files require a server restart

2. **Use browser DevTools** (F12)
   - Inspect elements
   - Debug CSS
   - Check console for JavaScript errors

3. **Read error messages carefully**
   - Django provides detailed error pages
   - They tell you exactly what's wrong and where

4. **Start small**
   - Make one change at a time
   - Test after each change
   - Learn incrementally

5. **Use version control**
   - Consider learning Git
   - Commit after each working feature
   - Easy to revert mistakes

## 🆘 Getting Help

### Check These First:
1. Error message in terminal
2. Browser console (F12 → Console tab)
3. Django debug page (appears on errors)

### Common Django Commands:
```powershell
# Start server
python manage.py runserver

# Stop server
Ctrl + C

# Check for issues
python manage.py check

# Create admin user
python manage.py createsuperuser

# Open Django shell
python manage.py shell
```

## 🎉 You're Ready!

You now have:
- ✅ A fully functional Django project
- ✅ A beautiful, responsive landing page
- ✅ Understanding of the project structure
- ✅ Knowledge of how to make changes
- ✅ Resources to continue learning

**Happy coding and Happy New Year! 🎊**

---

**Created by:** Mehmet Eren Akgül, Ali Rıza Göçer, Altan Tarı, Ömer Faruk Coşkun, Hakan Tan
