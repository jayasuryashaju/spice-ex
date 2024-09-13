
# SpiceEx

SpiceEx is a Django-based e-commerce platform for selling products. The project is designed to be flexible and scalable, allowing for easy customization and expansion.

## Features

- User authentication and registration
- Product listing by categories
- Product detail pages with image galleries
- Cart and checkout functionality
- Responsive design for mobile and desktop
- Integration with PostgreSQL database
- Smooth scrolling and modern UI/UX

## Project Structure

```bash
.
├── .venv/              # Virtual environment directory
├── media/              # User-uploaded files (e.g., product images)
├── product/            # App for product-related features
├── siteinfo/           # App for site information (logo, contact, etc.)
├── spiceex/            # Main Django project folder
│   ├── __pycache__/    # Compiled Python files
│   ├── settings.py     # Main project settings
│   ├── urls.py         # URL routing
│   ├── asgi.py         # ASGI entry point
│   └── wsgi.py         # WSGI entry point
├── static/             # Static files (CSS, JavaScript, images)
├── store/              # App for store-related features
├── templates/          # HTML templates for the front-end
├── manage.py           # Django management script
└── README.md           # Project documentation (this file)
```

## Technologies Used

- **Django**: Web framework
- **PostgreSQL**: Database
- **HTML/CSS**: Frontend
- **JavaScript**: Frontend interactions
- **AOS.js**: Animations on scroll

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- Virtualenv (recommended)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jayasuryashaju/spiceex.git
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # For Windows: .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file in the project root:
   ```bash
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   ```

5. Run migrations:
   ```bash
   python manage.py migrate
   ```

6. Collect static files:
   ```bash
   python manage.py collectstatic
   ```

7. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Deployment

For production deployment, follow these steps:

1. Ensure `DEBUG = False` in `settings.py`.
2. Use a production-ready database (e.g., PostgreSQL).
3. Configure a web server like **Nginx** and an application server like **Gunicorn**.
4. Make sure static files are served by the web server, not Django.

## Usage

### Adding Products
- Use the Django admin interface to add new products and categories.

### Customization
- Modify the `templates/` directory for front-end changes.
- Update the `static/` directory for CSS, JavaScript, and images.



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to reach out!

- **Email**: jayasuryashaju3031@gmail.com
- **GitHub**: [jayasuryashaju](https://github.com/jayasuryashaju)
