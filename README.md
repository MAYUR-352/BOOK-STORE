# 📚 Django Bookstore

A modern, fully-featured online bookstore built with Django. This project includes user authentication, book catalog management, shopping cart functionality, and is deployment-ready for production environments.

## 🚀 Features

- **Book Catalog Management**: Browse and search through a collection of books
- **User Authentication**: User registration, login, and profile management
- **Shopping Cart**: Add books to cart with quantity management
- **Order Processing**: Complete order management system
- **Admin Interface**: Django admin panel for easy content management
- **Media Handling**: Book cover image uploads and management
- **Responsive Design**: Mobile-friendly user interface
- **Production Ready**: Configured for deployment with security best practices

## 🛠️ Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite (development) / PostgreSQL (production)
- **Static Files**: WhiteNoise for static file serving
- **Environment Management**: python-dotenv
- **Deployment**: Gunicorn WSGI server
- **Image Processing**: Pillow for image handling

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8+ installed
- Git (for cloning the repository)
- PostgreSQL (for production deployment)

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd bookstore
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

Create a `.env` file in the project root:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### 5. Database Setup

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to view the application.

## 📁 Project Structure

```
bookstore/
├── bookstore/                 # Project configuration
│   ├── settings.py           # Django settings
│   ├── urls.py              # URL routing
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── store/                    # Main application
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── urls.py              # App URL patterns
│   ├── admin.py             # Admin configuration
│   └── templates/           # HTML templates
│       └── store/
├── static/                   # Static files (CSS, JS, images)
├── media/                    # User-uploaded files
├── requirements.txt          # Python dependencies
├── Procfile                 # Deployment configuration
├── .env                     # Environment variables
└── manage.py                # Django management script
```

## 🗃️ Database Models

### Book
- `title`: Book title
- `author`: Author name
- `price`: Book price (decimal)
- `description`: Book description
- `cover_image`: Book cover upload

### CartItem
- `user`: Associated user
- `book`: Book reference
- `quantity`: Number of items

### Order
- `user`: User who placed the order
- `items`: Cart items in the order
- `created_at`: Order timestamp

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DEBUG` | Enable debug mode | `False` |
| `SECRET_KEY` | Django secret key | Required |
| `DATABASE_URL` | Database connection string | SQLite |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `*` |

### Security Features

- CSRF protection enabled
- XSS filtering
- Content type sniffing protection
- Secure cookies (production)
- HSTS headers (production)
- SSL redirect (production)

## 🚀 Deployment

### Heroku Deployment

1. **Install Heroku CLI** and login:
```bash
heroku login
```

2. **Create Heroku app**:
```bash
heroku create your-bookstore-app
```

3. **Set environment variables**:
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-production-secret-key
heroku config:set ALLOWED_HOSTS=your-bookstore-app.herokuapp.com
```

4. **Add PostgreSQL addon**:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

5. **Deploy**:
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### Railway/Render Deployment

1. Connect your GitHub repository
2. Set environment variables in the dashboard
3. Deploy automatically from your main branch

### Manual Server Deployment

1. **Set up server environment**
2. **Install dependencies**
3. **Configure environment variables**
4. **Set up PostgreSQL database**
5. **Configure reverse proxy (Nginx)**
6. **Set up SSL certificate**

## 🧪 Testing

Run the test suite:

```bash
python manage.py test
```

Check deployment readiness:

```bash
python manage.py check --deploy
```

## 📚 Admin Interface

Access the Django admin at `/admin/` with your superuser credentials to:

- Add/edit books
- Manage users
- View orders
- Configure site settings

## 🔍 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with book list |
| `/book/<id>/` | GET | Book detail view |
| `/cart/` | GET | Shopping cart |
| `/add-to-cart/<id>/` | POST | Add book to cart |
| `/checkout/` | GET/POST | Order checkout |
| `/admin/` | GET | Admin interface |

## 🛡️ Security Considerations

- **Secret Key**: Use a strong, random secret key in production
- **Debug Mode**: Always set `DEBUG=False` in production
- **Database**: Use PostgreSQL for production
- **HTTPS**: Enable SSL/TLS for production deployments
- **Environment Variables**: Never commit sensitive data to version control

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Troubleshooting

### Common Issues

**Static files not loading:**
```bash
python manage.py collectstatic
```

**Database connection errors:**
- Check your `DATABASE_URL` environment variable
- Ensure PostgreSQL is running (production)

**Secret key warnings:**
- Generate a new secret key for production
- Use Django's built-in key generator

**Permission errors:**
- Check file permissions for media uploads
- Ensure proper directory structure

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Search existing issues in the repository
3. Create a new issue with detailed information

## 🔄 Recent Updates

- ✅ Added WhiteNoise for static file serving
- ✅ Configured environment-based settings
- ✅ Added security headers and HTTPS support
- ✅ Deployment-ready configuration
- ✅ PostgreSQL support for production

---

**Made with ❤️ using Django**
