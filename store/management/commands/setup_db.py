from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User
from store.models import Book


class Command(BaseCommand):
    help = 'Setup database for production deployment'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🔧 Setting up database for production...'))
        
        # Run migrations
        self.stdout.write('📦 Running migrations...')
        call_command('migrate', '--run-syncdb')
        self.stdout.write(self.style.SUCCESS('✅ Migrations completed!'))
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            self.stdout.write('👤 Creating default admin user...')
            User.objects.create_superuser(
                username='admin',
                email='admin@bookstore.com',
                password='bookstore123'  # Change this in production
            )
            self.stdout.write(self.style.SUCCESS('✅ Admin user created! Username: admin, Password: bookstore123'))
        else:
            self.stdout.write('👤 Admin user already exists.')
        
        # Create sample books if none exist
        if not Book.objects.exists():
            self.stdout.write('📚 Creating sample books...')
            Book.objects.create(
                title='Sample Book 1',
                author='Sample Author',
                price=299.99,
                description='This is a sample book to test your bookstore.'
            )
            Book.objects.create(
                title='Sample Book 2', 
                author='Another Author',
                price=399.99,
                description='Another sample book for your bookstore.'
            )
            self.stdout.write(self.style.SUCCESS('✅ Sample books created!'))
        else:
            self.stdout.write('📚 Books already exist in database.')
            
        self.stdout.write(self.style.SUCCESS('🎉 Database setup completed successfully!'))
        self.stdout.write('🌐 Your bookstore is ready to go!')
