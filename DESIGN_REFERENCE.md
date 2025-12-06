# 🎨 Design Reference Guide

## Color Palette

### Primary Colors

#### Christmas Red
```css
--red-primary: #C41E3A    /* Main red - Headers, accents */
--red-dark: #8B0000       /* Deep red - Shadows, depth */
--red-light: #DC143C      /* Bright red - Highlights, separators */
```

🔴 **#C41E3A** - Rich, festive crimson  
🔴 **#8B0000** - Deep burgundy for drama  
🔴 **#DC143C** - Bright crimson for energy  

#### Forest Green
```css
--green-primary: #0F5132  /* Main green - Background accents */
--green-dark: #2D5016     /* Dark green - Depth, shadows */
--green-light: #228B22    /* Bright green - Highlights */
```

🟢 **#0F5132** - Deep forest green  
🟢 **#2D5016** - Dark pine green  
🟢 **#228B22** - Bright festive green  

#### Gold & Light Colors
```css
--gold: #FFD700          /* Primary gold - Main accent */
--gold-light: #FFF4B5    /* Light gold - Subtle highlights */
--white: #FFFFFF         /* Pure white - Text, contrast */
--cream: #FFF8DC         /* Warm cream - Soft text */
--dark: #1a1a1a         /* Deep black - Overlays */
```

🟡 **#FFD700** - Rich metallic gold  
🟡 **#FFF4B5** - Soft golden cream  
⚪ **#FFFFFF** - Pure white for clarity  
⚪ **#FFF8DC** - Warm cornsilk cream  
⚫ **#1a1a1a** - Rich charcoal black  

## Gradient Combinations

### Gradient Red
```css
background: linear-gradient(135deg, #C41E3A 0%, #8B0000 100%);
```
Used for: CTA button, dramatic backgrounds

### Gradient Green
```css
background: linear-gradient(135deg, #0F5132 0%, #2D5016 100%);
```
Used for: Section backgrounds, accents

### Gradient Festive (Main Background)
```css
background: linear-gradient(135deg, #C41E3A 0%, #0F5132 50%, #8B0000 100%);
```
Used for: Body background, hero section

### Gradient Gold
```css
background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
```
Used for: Text effects, countdown numbers

## Typography

### Font Families

#### Playfair Display (Display/Headers)
- **Weight**: 700 (Bold), 900 (Black)
- **Style**: Serif, Elegant, Traditional
- **Use**: Main titles, hero headlines
- **Import**: 
```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&display=swap" rel="stylesheet">
```

#### Poppins (Body/UI)
- **Weights**: 300 (Light), 400 (Regular), 600 (Semi-Bold), 700 (Bold), 800 (Extra-Bold)
- **Style**: Sans-serif, Modern, Clean
- **Use**: Body text, UI elements, countdown
- **Import**: 
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700;800&display=swap" rel="stylesheet">
```

### Typography Scale

```
Hero Title:        clamp(2.5rem, 8vw, 6rem)     [40-96px]
Countdown Title:   clamp(1.5rem, 4vw, 2.5rem)   [24-40px]
Countdown Numbers: clamp(2.5rem, 6vw, 4.5rem)   [40-72px]
Subtitle:          clamp(1rem, 3vw, 1.5rem)     [16-24px]
Button Text:       clamp(1rem, 2.5vw, 1.25rem)  [16-20px]
Body Text:         clamp(1rem, 2.5vw, 1.25rem)  [16-20px]
Footer Names:      clamp(1rem, 2.5vw, 1.5rem)   [16-24px]
```

## Spacing System

### Padding/Margin Scale
```css
--spacing-xs: 0.5rem    /* 8px */
--spacing-sm: 1rem      /* 16px */
--spacing-md: 2rem      /* 32px */
--spacing-lg: 3rem      /* 48px */
--spacing-xl: 4rem      /* 64px */
```

### Component Spacing
- **Hero Section**: 2rem padding
- **Countdown Container**: 3rem vertical, 2rem horizontal
- **CTA Button**: 1.25rem vertical, 3rem horizontal
- **Footer**: 4rem top, 2rem horizontal, 2rem bottom
- **Section Gaps**: 3-4rem between major sections

## Border Styles

### Countdown Container
```css
border: 3px solid var(--gold);
border-radius: 20px;
```

### CTA Button
```css
border: 3px solid var(--gold);
border-radius: 50px;  /* Fully rounded pill shape */
```

### Future Section
```css
border: 2px dashed var(--gold);
border-radius: 20px;
```

## Shadow Styles

### Subtle Depth
```css
box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
```

### Glowing Effect
```css
box-shadow: 
    0 10px 40px rgba(0, 0, 0, 0.5),
    0 0 20px rgba(255, 215, 0, 0.3);
```

### Intense Glow (Hover)
```css
box-shadow: 
    0 15px 40px rgba(196, 30, 58, 0.7),
    0 0 40px rgba(255, 215, 0, 0.6);
```

### Text Shadow
```css
/* Dramatic depth */
text-shadow: 3px 3px 0 rgba(0, 0, 0, 0.3);

/* Subtle with glow */
text-shadow: 
    2px 2px 4px rgba(0, 0, 0, 0.5),
    0 0 30px rgba(255, 215, 0, 0.5);
```

## Animation Timing

### Duration Guidelines
- **Micro-interactions**: 0.3s (hover, click)
- **UI Transitions**: 0.5s (state changes)
- **Attention-grabbing**: 1-2s (pulse, glow)
- **Atmospheric**: 3-6s (float, sway)
- **Ambient**: 10-19s (snowfall)

### Easing Functions
```css
ease-out      /* Fast start, slow end - for entrances */
ease-in-out   /* Smooth both ends - for continuous loops */
linear        /* Constant speed - for rotations */
```

## Emoji Icons Used

### Decorative Elements
- 🎄 Christmas Tree (ornament-left)
- 🎁 Gift Box (ornament-right)
- ✨ Sparkles (floating-ornament)
- 🌟 Star (floating-ornament)
- ⭐ Five-pointed Star (decorative)
- ❄️ Snowflake (conceptual)
- ❅ Heavy Snowflake (animation)
- ❆ Alternate Snowflake (animation)

### Interactive Elements
- 🎉 Party Popper (button icon)
- 🎊 Confetti Ball (New Year message)
- ❤️ Red Heart (footer decoration)

## Responsive Breakpoints

### Large Desktop (1200px+)
- Full animations and effects
- All decorative elements visible
- Maximum sizing for all elements

### Desktop (768px - 1199px)
- Slight scaling adjustments
- All features maintained
- Optimized spacing

### Tablet (480px - 767px)
- Adjusted font sizes
- Reduced ornament sizes
- Floating elements hidden
- Maintained functionality

### Mobile (<480px)
- Vertical countdown layout
- No time separators
- Minimal decorative elements
- Stack-based layout
- Touch-optimized buttons

## Accessibility Features

### Color Contrast Ratios
- **White on Red**: 4.5:1+ (WCAG AA)
- **Gold on Dark**: 7:1+ (WCAG AAA)
- **Cream on Dark**: 12:1+ (WCAG AAA)

### Motion Preferences
```css
@media (prefers-reduced-motion: reduce) {
    * {
        animation-duration: 0.01ms !important;
        transition-duration: 0.01ms !important;
    }
}
```

### Semantic HTML
- Proper heading hierarchy (h1 → h2 → h3)
- ARIA labels for decorative elements
- Semantic section elements
- Accessible button elements

## Design Principles Applied

### 1. Visual Hierarchy
- **Primary**: Countdown timer (largest, centered, glowing)
- **Secondary**: Hero title (large, gradient)
- **Tertiary**: CTA button (prominent, interactive)
- **Supporting**: Decorative elements (subtle, ambient)

### 2. Color Psychology
- **Red**: Energy, celebration, urgency
- **Green**: Growth, renewal, hope
- **Gold**: Prosperity, luxury, success
- **White/Cream**: Purity, new beginnings

### 3. Consistency
- Repeated border radius (20px for containers)
- Consistent gradient directions (135deg)
- Unified animation easing
- Harmonious color palette

### 4. Balance
- Symmetrical layout
- Balanced color distribution
- Even spacing rhythm
- Centered focal points

### 5. User Experience
- Obvious interactive elements
- Immediate feedback on interaction
- Clear call-to-action
- Intuitive navigation

## Component Patterns

### Glass-morphism Effect
```css
background: rgba(0, 0, 0, 0.4);
backdrop-filter: blur(10px);
border: 3px solid var(--gold);
```

### Gradient Text
```css
background: linear-gradient(135deg, color1, color2);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### Floating Animation
```css
@keyframes float {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-20px) rotate(180deg); }
}
```

### Pulse Glow
```css
@keyframes pulseGlow {
    0%, 100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3); }
    50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.6); }
}
```

---

## Quick Reference: CSS Custom Properties

```css
:root {
    /* Colors */
    --red-primary: #C41E3A;
    --red-dark: #8B0000;
    --red-light: #DC143C;
    --green-primary: #0F5132;
    --green-dark: #2D5016;
    --green-light: #228B22;
    --gold: #FFD700;
    --gold-light: #FFF4B5;
    --white: #FFFFFF;
    --cream: #FFF8DC;
    --dark: #1a1a1a;
    
    /* Gradients */
    --gradient-red: linear-gradient(135deg, #C41E3A 0%, #8B0000 100%);
    --gradient-green: linear-gradient(135deg, #0F5132 0%, #2D5016 100%);
    --gradient-festive: linear-gradient(135deg, #C41E3A 0%, #0F5132 50%, #8B0000 100%);
    --gradient-gold: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
}
```

---

**Use this guide when customizing the design to maintain visual consistency!** 🎨
