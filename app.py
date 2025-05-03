from app import create_app

# Point d'entrée de l'application
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
