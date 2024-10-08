from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Cria um serviço para o ChromeDriver
service = Service(ChromeDriverManager().install())

# Inicialize o WebDriver usando o serviço
driver = webdriver.Chrome(service=service)

# Acesse o site
driver.get("https://www.amazon.com.br")  # URL correta

try:
    # Espera até que a barra de busca esteja presente
    search_bar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "field-keywords"))  # Ajuste para o nome correto
    )
    
    # Insira o termo "camiseta" na barra de pesquisa
    search_bar.send_keys("camiseta")
    search_bar.send_keys(Keys.RETURN)

    # Aguarda que os resultados estejam disponíveis
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot"))  # Ajuste para o seletor correto
    )

    # Verifique os resultados
    results = driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-result-item")  # Ajuste para o seletor CSS correto

    # Lista para armazenar os resultados correspondentes
    corresponding_products = []

    # Verifique se os resultados correspondem ao termo pesquisado
    for result in results:
        if "camiseta" in result.text.lower():  # Ajuste para verificar o termo
            corresponding_products.append(result.text)
            print("Produto correspondente encontrado:", result.text)

    # Verificação final
    if not corresponding_products:
        print("Nenhum produto correspondente encontrado para o termo 'camiseta'.")
    else:
        print(f"{len(corresponding_products)} produtos correspondentes encontrados.")

finally:
    driver.quit()  # Feche o navegador após o teste
