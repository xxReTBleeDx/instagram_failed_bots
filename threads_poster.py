# Importation du module undetected_chromedriver pour éviter la détection par les sites web
import undetected_chromedriver as uc

# Importation de By pour spécifier les sélecteurs comme XPATH, TAG_NAME, etc.
from selenium.webdriver.common.by import By

# Importation de WebDriverWait pour attendre la présence des éléments avant d'interagir
from selenium.webdriver.support.ui import WebDriverWait

# Importation des conditions pré-définies comme "clickable" ou "présent" pour WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Importation de time pour gérer les pauses dans le code
import time

# Importation de random pour générer des délais aléatoires, simulant des actions humaines
import random

# Importation de ActionChains pour effectuer des interactions complexes comme cliquer et déplacer la souris
from selenium.webdriver.common.action_chains import ActionChains

# *** Informations de connexion ***
# Variables contenant les informations de connexion (nom d'utilisateur et mot de passe)
username = "username or email"
password = "password"

# *** Initialisation du driver ***
# Initialise le navigateur Chrome avec undetected_chromedriver
driver = uc.Chrome()

# *** Accéder à Threads.net ***
# Accède à la page de connexion du site Threads.net
driver.get('https://www.threads.net/login')

# *** Attendre que la page soit complètement chargée ***
# Attend que le body de la page soit présent, ce qui signifie que la page est chargée
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# *** Pause supplémentaire pour un comportement humain réaliste ***
# Pause de 3 à 6 secondes pour imiter le comportement humain
time.sleep(random.uniform(3, 6))

# *** Remplir le champ nom d'utilisateur avec des délais aléatoires ***
# Localise le champ nom d'utilisateur par son attribut autocomplete
username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username"]')))
# Vide le champ pour s'assurer qu'il n'y a pas de texte résiduel
username_field.clear()

# Boucle pour taper chaque caractère du nom d'utilisateur avec une pause aléatoire
for char in username:
    username_field.send_keys(char)  # Taper un caractère
    time.sleep(random.uniform(0.1, 0.3))  # Pause de 0.1 à 0.3 secondes entre chaque frappe

# *** Remplir le champ mot de passe avec des délais aléatoires ***
# Localise le champ mot de passe de la même manière que pour le nom d'utilisateur
password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
# Vide le champ mot de passe
password_field.clear()

# Boucle pour taper chaque caractère du mot de passe avec une pause aléatoire
for char in password:
    password_field.send_keys(char)  # Taper un caractère du mot de passe
    time.sleep(random.uniform(0.1, 0.3))  # Pause de 0.1 à 0.3 secondes entre chaque frappe

# *** Clic sur le bouton "Se connecter" ***
# Attend que le bouton "Se connecter" soit cliquable et récupère l'élément
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and .//div[contains(text(), "Se connecter")]]'))
)
# Exécute un clic sur le bouton "Se connecter" avec du JavaScript (parfois plus fiable que `click()`)
driver.execute_script("arguments[0].click();", login_button)

# *** Attendre la page d'accueil après connexion ***
# Attend 5 secondes pour laisser la page d'accueil se charger complètement
time.sleep(5)

# *** Clic sur le bouton pour commencer un thread ***
# Essaie de localiser et cliquer sur le bouton pour démarrer un nouveau thread
try:
    thread_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Commencez un thread…")]'))
    )
    # Si le bouton est trouvé, clique dessus
    thread_button.click()
except Exception as e:
    # Si une erreur se produit, affiche l'erreur
    print(f"Erreur lors du clic sur le bouton 'Commencez un thread' : {e}")

# *** Attendre un peu pour s'assurer que la boîte d'édition apparaît ***
# Pause de 3 secondes pour s'assurer que la boîte de texte du thread est bien visible
time.sleep(3)

# *** Remplir le champ texte du thread ***
# Essaie de localiser la boîte de texte où écrire le thread
try:
    thread_textarea = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
    )
    # Message à écrire dans le thread
    thread_message = " hey every one I am a bot LMAO!🤖 "
    # Boucle pour taper chaque caractère du message avec des pauses aléatoires
    for char in thread_message:
        thread_textarea.send_keys(char)
        time.sleep(random.uniform(0.1, 0.2))  # Simuler une frappe humaine
except Exception as e:
    # Si une erreur se produit, affiche l'erreur
    print(f"Erreur lors de la rédaction du thread : {e}")

# *** Amélioration : Gestion plus robuste du clic sur le bouton "Publier" ***
# Liste des XPaths possibles pour le bouton "Publier"
publish_xpaths = [
    '//div[contains(text(), "Publier")]',
    '//div[contains(text(), "Post")]'
]

# Essaie de localiser et cliquer sur le bouton "Publier" en utilisant plusieurs XPaths
publish_button = None
for xpath in publish_xpaths:
    try:
        publish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        if publish_button:
            break  # Arrête la boucle si le bouton est trouvé
    except Exception as e:
        print(f"Erreur avec le XPath : {xpath}, {e}")

# Simule un mouvement de souris sur le bouton pour imiter un utilisateur humain et publier
if publish_button:
    max_attempts = 3
    attempts = 0
    success = False
    while attempts < max_attempts and not success:
        try:
            # Simule un clic sur le bouton avec ActionChains
            actions = ActionChains(driver)
            actions.move_to_element(publish_button).click().perform()
            success = True
            print("Thread publié avec succès !")
        except Exception as e:
            attempts += 1
            print(f"Tentative {attempts} échouée, réessayer... : {e}")
            time.sleep(2)  # Pause avant de réessayer

    if not success:
        print("Impossible de publier le thread après plusieurs tentatives.")
else:
    print("Le bouton 'Publier' n'a pas pu être trouvé.")

# *** Attendre quelques secondes pour voir le résultat ***
# Attend 10 secondes pour observer le résultat avant de fermer le navigateur
time.sleep(10)

# *** Fermer le navigateur ***
# Quitte et ferme le navigateur
driver.quit()
