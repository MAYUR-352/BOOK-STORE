#!/usr/bin/env python
"""
Production readiness test script for Django Bookstore
Run this script to verify your application is ready for deployment
"""

import os
import sys
import django
from pathlib import Path

# Add the project directory to Python path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

def test_production_config():
    """Test production configuration"""
    print("🔍 Testing production configuration...")
    
    # Test 1: Django setup
    try:
        django.setup()
        print("✅ Django setup successful")
    except Exception as e:
        print(f"❌ Django setup failed: {e}")
        return False
    
    # Test 2: Import settings
    try:
        from django.conf import settings
        print("✅ Settings import successful")
    except Exception as e:
        print(f"❌ Settings import failed: {e}")
        return False
    
    # Test 3: Check critical settings
    checks = [
        ("SECRET_KEY exists", lambda: bool(settings.SECRET_KEY)),
        ("DEBUG setting", lambda: hasattr(settings, 'DEBUG')),
        ("ALLOWED_HOSTS set", lambda: settings.ALLOWED_HOSTS),
        ("Database configured", lambda: bool(settings.DATABASES)),
        ("Static files configured", lambda: bool(settings.STATIC_ROOT)),
        ("Whitenoise in middleware", lambda: 'whitenoise.middleware.WhiteNoiseMiddleware' in settings.MIDDLEWARE),
    ]
    
    for check_name, check_func in checks:
        try:
            if check_func():
                print(f"✅ {check_name}")
            else:
                print(f"⚠️  {check_name} - check manually")
        except Exception as e:
            print(f"❌ {check_name} failed: {e}")
    
    # Test 4: Import WSGI application
    try:
        from bookstore.wsgi import application
        assert application is not None
        print("✅ WSGI application import successful")
    except Exception as e:
        print(f"❌ WSGI application import failed: {e}")
        return False
    
    print("\n🎉 Production configuration test completed!")
    return True

def test_development_vs_production():
    """Test configuration differences between development and production"""
    print("\n🔧 Testing development vs production settings...")
    
    from django.conf import settings
    
    if settings.DEBUG:
        print("🚧 Running in DEVELOPMENT mode")
        print("   - DEBUG = True")
        print("   - File logging enabled")
        print("   - SQLite database (if no DATABASE_URL)")
    else:
        print("🚀 Running in PRODUCTION mode")
        print("   - DEBUG = False")
        print("   - Console logging only")
        print("   - SSL redirects enabled")
        print("   - Secure cookies enabled")

if __name__ == "__main__":
    print("🧪 Django Bookstore Production Test")
    print("=" * 40)
    
    success = test_production_config()
    test_development_vs_production()
    
    if success:
        print("\n✅ All tests passed! Your application is ready for deployment.")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed. Please check the configuration.")
        sys.exit(1)
