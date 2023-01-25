import time
import requests
from bs4 import BeautifulSoup
import smtplib

# URL of webpage to scrape
url = 'https://nekosan.de/collections/alle-hoodies/products/new-harajuku-totoro-kawaii-hoodie-sweatshirt-my-neighbor-coat-cosplay-fleece-overcoat-with-ears-harajuku-cute-jackets-christmas'

# Check webpage twice a day
while True:
    # Scrape webpage
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the specific button on the page
    button = soup.find('button', {'class': 'add-to-cart'})

    # Check if button is disabled
    if 'disabled' not in button.attrs:
      print("Email Sent - Article Good")
      # Send email notification
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login("", "")
      msg = """Subject: Button status\nPullover is avaliable!!!
      https://nekosan.de/collections/alle-hoodies/products/new-harajuku-totoro-kawaii-hoodie-sweatshirt-my-neighbor-coat-cosplay-fleece-overcoat-with-ears-harajuku-cute-jackets-christmas
      """
      server.sendmail("", "", msg)
      server.quit()
    time.sleep(43200)  # sleep for 12 hours