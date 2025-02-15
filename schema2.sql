-- Table des livres
DROP TABLE IF EXISTS recettes; 
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,    
    title TEXT NOT NULL,          -- Titre du recette
    date_posted TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    author TEXT NOT NULL,         -- Auteur du recette
    categorie TEXT               -- Genre du recette (optionnel)
    thumbnail TEXT,               -- URL de l'image de couverture
    slug TEXT UNIQUE,             -- Slug (identifiant unique pour les recettes)
    --published_date DATE,          -- Date de publication
    --isbn TEXT UNIQUE,             -- ISBN (identifiant unique pour les recettes)
    --created_at DATETIME DEFAULT CURRENT_TIMESTAMP -- Date d'enregistrement
  );

-- Table des utilisateurs
CREATE TABLE users ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE, -- Nom d'utilisateur
    email TEXT UNIQUE,             -- Adresse email
    phone TEXT,                    -- Numéro de téléphone
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP -- Date d'inscription
);

-- Table des stocks
CREATE TABLE stock (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,     -- Livre (relation avec books)
    total_quantity INTEGER NOT NULL, -- Quantité totale
    available_quantity INTEGER NOT NULL, -- Quantité disponible
    FOREIGN KEY (book_id) REFERENCES books(id)
);

-- Table des emprunts
CREATE TABLE borrowed_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,     -- Utilisateur (relation avec users)
    book_id INTEGER NOT NULL,     -- Livre (relation avec books)
    borrowed_date DATE DEFAULT CURRENT_DATE, -- Date d'emprunt
    return_date DATE,             -- Date de retour
    status TEXT DEFAULT 'borrowed', -- Statut ('borrowed', 'returned')
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id)
);
