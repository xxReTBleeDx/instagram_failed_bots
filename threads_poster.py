import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.common.action_chains import ActionChains

# *** Informations de connexion ***
username = "username or email"
password = "passowrd"

# *** Initialisation du driver ***
driver = uc.Chrome()

# *** Accéder à Threads.net ***
driver.get('https://www.threads.net/login')

# *** Attendre que la page soit complètement chargée ***
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# *** Pause supplémentaire pour un comportement humain réaliste ***
time.sleep(random.uniform(3, 6))

# *** Remplir le champ nom d'utilisateur avec des délais aléatoires ***
username_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="username"]')))
username_field.clear()
for char in username:
    username_field.send_keys(char)
    time.sleep(random.uniform(0.1, 0.3))  # Pause entre chaque frappe

# *** Remplir le champ mot de passe avec des délais aléatoires ***
password_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//input[@autocomplete="current-password"]')))
password_field.clear()
for char in password:
    password_field.send_keys(char)
    time.sleep(random.uniform(0.1, 0.3))

# *** Clic sur le bouton "Se connecter" ***
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and .//div[contains(text(), "Se connecter")]]'))
)
driver.execute_script("arguments[0].click();", login_button)

# *** Attendre la page d'accueil après connexion ***
time.sleep(5)  # Temps pour que la page soit bien chargée après la connexion

# *** Clic sur le bouton pour commencer un thread ***
try:
    thread_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Commencez un thread…")]'))
    )
    thread_button.click()
except Exception as e:
    print(f"Erreur lors du clic sur le bouton 'Commencez un thread' : {e}")

# *** Attendre un peu pour s'assurer que la boîte d'édition apparaît ***
time.sleep(3)

# *** Remplir le champ texte du thread ***
try:
    thread_textarea = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="textbox"]'))
    )
    thread_message = " hey every one I am a bot LMAO!🤖 "
    for char in thread_message:
        thread_textarea.send_keys(char)
        time.sleep(random.uniform(0.1, 0.2))  # Simuler la frappe humaine
except Exception as e:
    print(f"Erreur lors de la rédaction du thread : {e}")

# *** Clic sur le bouton publier avec ActionChains ***
try:
    publish_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Publier") or contains(text(), "Post")]'))
    )
    
    # Déplacer le curseur sur le bouton pour simuler l'interaction humaine
    actions = ActionChains(driver)
    actions.move_to_element(publish_button).click().perform()
    
    print("Thread publié avec succès !")
except Exception as e:
    print(f"Erreur lors de la tentative de publication : {e}")

# *** Attendre quelques secondes pour voir le résultat ***
time.sleep(10)
driver.quit()
