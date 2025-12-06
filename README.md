# 🎄 New Year's Gift Exchange Web Application

A stunning, festive landing page for a New Year's gift exchange application built with Django. Features a beautiful red and green Christmas color palette, animated countdown timer to New Year's, and a fully responsive design optimized for all devices.

## 📚 Documentation

- **[INDEX.md](INDEX.md)** - Navigation guide to all documentation
- **[QUICKSTART.md](QUICKSTART.md)** - Fast 5-minute setup guide
- **[SETUP.md](SETUP.md)** - Detailed step-by-step instructions
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Complete project overview
- **[FEATURES.md](FEATURES.md)** - Design and technical details
- **[DESIGN_REFERENCE.md](DESIGN_REFERENCE.md)** - Color palette and design tokens

## ✨ Features

- **🎊 Festive Design**: Red and green Christmas-themed color palette with gold accents
- **⏰ Live Countdown**: Real-time countdown timer to January 1st showing days, hours, minutes, and seconds
- **❄️ Animated Snowflakes**: Beautiful falling snowflakes animation
- **📱 Fully Responsive**: Optimized for desktop, tablet, and mobile devices
- **🎨 Modern Typography**: Using Poppins and Playfair Display fonts from Google Fonts
- **✨ Smooth Animations**: Floating ornaments, glowing effects, and interactive elements
- **♿ Accessible**: Respects user's motion preferences

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory**:
   ```powershell
   cd C:\gift_exchange
   ```

2. **Create a virtual environment** (recommended):
   ```powershell
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   If you get an execution policy error, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

4. **Install Django**:
   ```powershell
   pip install -r requirements.txt
   ```

5. **Run database migrations**:
   ```powershell
   python manage.py migrate
   ```

6. **Start the development server**:
   ```powershell
   python manage.py runserver
   ```

7. **Open your browser** and visit:
   ```
   http://127.0.0.1:8000/
   ```

## 📁 Project Structure

```
gift_exchange/
├── gift_exchange/           # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   ├── asgi.py
│   └── wsgi.py
├── landing/                # Landing page app
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py            # View functions
│   ├── urls.py             # App URL configuration
│   ├── admin.py
│   └── models.py
├── templates/              # HTML templates
│   └── landing/
│       └── home.html       # Main landing page template
├── static/                 # Static files
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   └── js/
│       └── countdown.js    # Countdown timer logic
├── manage.py               # Django management script
└── requirements.txt        # Python dependencies
```

## 🎨 Design Features

### Color Palette
- **Primary Red**: `#C41E3A` - Deep festive red
- **Dark Red**: `#8B0000` - Rich burgundy
- **Primary Green**: `#0F5132` - Forest green
- **Gold**: `#FFD700` - Festive gold accents
- **Cream**: `#FFF8DC` - Soft warm white

### Typography
- **Headlines**: Playfair Display (Serif) - Elegant and festive
- **Body Text**: Poppins (Sans-serif) - Modern and clean

### Animations
- Falling snowflakes
- Pulsing glow effects
- Floating ornaments
- Gradient color shifts
- Smooth hover transitions

## 📱 Responsive Breakpoints

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: 480px - 767px
- **Small Mobile**: Below 480px

## 🔧 Customization

### Changing Colors
Edit the CSS variables in `static/css/style.css`:
```css
:root {
    --red-primary: #C41E3A;
    --green-primary: #0F5132;
    --gold: #FFD700;
    /* Modify these to change the color scheme */
}
```

### Modifying the Countdown Target
The countdown automatically targets January 1st of the next year. To change this, edit `static/js/countdown.js`:
```javascript
const newYear = new Date(targetYear, 0, 1, 0, 0, 0);
// Change month (0-11) and day as needed
```

### Adding New Sections
Add new sections between the hero section and footer in `templates/landing/home.html`:
```html
<!-- Your new section here -->
<section class="your-section">
    <div class="container">
        <!-- Content -->
    </div>
</section>
```

## 👥 Development Team

- **Mehmet Eren Akgül**
- **Ali Rıza Göçer**
- **Altan Tarı**
- **Ömer Faruk Coşkun**
- **Hakan Tan**

## 🎯 Future Enhancements

- Gift exchange matching algorithm
- User authentication and profiles
- Wishlist creation and management
- Email notifications
- Gift tracking system
- Social sharing features

## 📝 Django Basics for Beginners

### Understanding Django Structure

1. **settings.py**: Configuration file for your Django project
   - Database settings
   - Static files configuration
   - Installed apps
   - Template directories

2. **urls.py**: URL routing - maps URLs to views
   ```python
   path('', views.home, name='home')
   # '' means root URL, calls home() function from views.py
   ```

3. **views.py**: Functions that handle requests and return responses
   ```python
   def home(request):
       return render(request, 'landing/home.html')
   # Renders the template when someone visits the page
   ```

4. **Templates**: HTML files with Django template syntax
   ```html
   {% load static %}  <!-- Load static files -->
   {% static 'css/style.css' %}  <!-- Reference static files -->
   ```

### Static Files in Django

Django serves CSS, JavaScript, and images as "static files":

1. Place files in the `static/` directory
2. Configure `STATIC_URL` in settings.py
3. Use `{% load static %}` in templates
4. Reference files with `{% static 'path/to/file' %}`

### Running Commands

- **Start server**: `python manage.py runserver`
- **Create migrations**: `python manage.py makemigrations`
- **Apply migrations**: `python manage.py migrate`
- **Create superuser**: `python manage.py createsuperuser`
- **Collect static files**: `python manage.py collectstatic`

## 🐛 Troubleshooting

### Port Already in Use
If port 8000 is already in use:
```powershell
python manage.py runserver 8080
```

### Static Files Not Loading
1. Ensure `DEBUG = True` in settings.py for development
2. Check that `STATIC_URL = '/static/'` is set
3. Verify files are in the correct `static/` directory

### Virtual Environment Issues
If activation fails:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📄 License

This project is created for educational purposes.

## 🎉 Happy New Year!

Celebrate the magic of giving with this beautiful gift exchange platform!

---

**Built with ❤️ and Django**
