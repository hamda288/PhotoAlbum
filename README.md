# PhotoShare - Photo Album Web Application

PhotoShare is a web application built using Django that allows users to create and manage photo albums. Users can upload their photos and organize them into separate folders, such as nature, food, wedding, and more. It provides a user-friendly interface to view and interact with the uploaded photos.

## Features

- Create Photo Albums: Users can create separate folders or albums to organize their photos.
- Upload Photos: Users can upload photos to their albums.
- View and Manage Albums: Users can view their albums and perform operations like renaming and deleting albums.
- View and Manage Photos: Users can view, and delete individual photos within their albums.
- User-Friendly Interface: The application has a clean and intuitive user interface for easy navigation and interaction.

<h2>Home Page</h2>
<img width="917" alt="p1" src="https://github.com/hamda288/PhotoAlbum/assets/96077150/f91bcf95-0620-44af-ae15-79b8238a37e3">

<h2>Options</h2>
<img width="918" alt="Navbar options" src="https://github.com/hamda288/PhotoAlbum/assets/96077150/8eccc65c-f20f-4d4b-8f42-bae6c8c6351b">

<h2>Add Picture</h2>
<img width="920" alt="add picture" src="https://github.com/hamda288/PhotoAlbum/assets/96077150/dab94774-d56e-473c-9a71-a8802ee1fdd2">

<h2>View Picture</h2>
<img width="908" alt="View picture" src="https://github.com/hamda288/PhotoAlbum/assets/96077150/7633fb6d-7897-4371-ac53-e3be4dcc053f">

## Installation

1. Clone the repository:

```bash
git clone https://github.com/hamda288/PhotoAlbum.git
```

2. Change into the project directory:

```bash
cd PhotoAlbum
```

3. Create and activate a virtual environment (optional, but recommended):

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Access the application by visiting [http://localhost:8000/](http://localhost:8000/) in your web browser.

## Configuration

The application uses a default configuration, but you can modify certain settings by updating the `settings.py` file in the `photoshare` directory.

- Database settings: You can change the database settings by updating the `DATABASES` configuration.

## Contributing

Contributions are welcome! If you'd like to contribute to PhotoShare, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request with a detailed description of your changes.

## Acknowledgments

- The project was developed as a learning exercise and was inspired by the Django web framework and its community.
- We thank all the contributors who have helped to improve this project.

## Contact

For any questions or suggestions, please feel free to open an issue in the [GitHub repository](https://github.com/hamda288/PhotoAlbum/issues).

Enjoy using PhotoShare!
