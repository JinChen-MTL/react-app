from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time
app = Flask(__name__)
from flask_cors import CORS
CORS(app)
# Set up the WebDriver (e.g., ChromeDriver)
from selenium.webdriver.support import expected_conditions as EC
def search_flights(departure="JFK", arrival="YUL", date="2025-02-23", one_way=True):
    options = Options()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration (optional)
    options.add_argument("--no-sandbox")  # Disable sandboxing (useful for Docker)
    options.add_argument("--remote-debugging-port=9222")  # Enable debugging (optional)

    # Initialize WebDriver with the headless options
    driver = webdriver.Chrome(options=options)
    try:
         # Open Google Flights
        driver.get("https://www.google.com/travel/flights")
        wait = WebDriverWait(driver, 5)

        if one_way:
            flight_type_button = driver.find_element(By.CLASS_NAME, "VfPpkd-aPP78e")
            flight_type_button.click()
            time.sleep(1)  # Wait for options to appear
            one_way = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "li[data-value='2']")))
            one_way.click()
            time.sleep(1)  # Wait for options to appear
        else:
            print("Round trip selected by default")
            return
        # Step 3: Wait for the departure field to be visible


        departure_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.e5F5td.BGeFcf')))
        departure_input = departure_container.find_element(By.CSS_SELECTOR, 'input[jsname="yrriRe"]')
        actions = ActionChains(driver)
        actions.move_to_element(departure_input)
        actions.click()
        actions.send_keys(departure)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)

        # Then handle arrival separately
        arrival_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.e5F5td.vxNK6d')))
        arrival_input = arrival_container.find_element(By.CSS_SELECTOR, 'input[jsname="yrriRe"]')
        actions = ActionChains(driver)
        actions.move_to_element(arrival_input)
        actions.click()
        actions.send_keys(arrival)
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(1)

        # Then click calender
    
        arrival_container = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.bgJkKe.K0Tsu')))
        arrival_container.click()
        time.sleep(1)  # Wait for the container to fully open

        date_cell = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'div[data-iso="{date}"]')))
        date_cell.click()
        time.sleep(1)  # Wait for the calendar to close

        done_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[jsname="WCieBd"]')))
        done_button.click()
        time.sleep(1)  # Wait for calendar to close

        done_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="xFFcie"]')))
        done_button.click()
        time.sleep(3)  # Wait for calendar to close

        # access the output page , choose price:
        try:
            wait = WebDriverWait(driver, 3)  # Adjust timeout as needed
            container = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="vDyvKd"]')))
            container.click()
        except TimeoutException:
            print("Element not clickable within the given time. Please check the locator or loading conditions.")    

        # Step 2: Wait for the dropdown menu to appear and select the 2nd item (Price)
        dropdown_menu = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.VfPpkd-StrnGf-rymPhb.DMZ54e')))
        price_option = dropdown_menu.find_elements(By.TAG_NAME, "li")[1]  # Index 1 for the second item
        price_option.click()
        time.sleep(5)  # Wait for calendar to close
        def wait_for_expanded_view(driver):
            wait = WebDriverWait(driver, 10)
            try:
                # Find the container first
                flights_container1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Rk10dc")))
                
                # Find the expand button and click the first one if exists
                expand_buttons = flights_container1.find_elements(By.CLASS_NAME, "ZVk93d")
                if expand_buttons and len(expand_buttons) > 0:
                    # Click the first expand button
                    expand_buttons[0].click()
                    time.sleep(4)  # Wait for expansion animation
                else:
                    print("No expand button found - flights may already be expanded")
                    
            except Exception as e:
                print(f"Error handling expand view: {str(e)}")

        # Add this before getting flight info
        wait_for_expanded_view(driver)
        time.sleep(5)  # Wait for calendar to close

        def get_flight_info(driver):
            # Wait for the flight results container
            wait = WebDriverWait(driver, 10)
            flights_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Rk10dc")))
            
            # Get all flight items except the last one (which is "View more")
            flight_items = flights_container.find_elements(By.CLASS_NAME, "pIav2d")
            
            flight_details = []
            for flight in flight_items:
                try:
                    stops_element = flight.find_element(By.CSS_SELECTOR, ".EfT7Ae.AdWm1c.tPgKwe span.ogfYpf").text
                    num_stops = "0" if "Nonstop" in stops_element else stops_element.split()[0]
                    try:
                        baggage_info = flight.find_element(By.CSS_SELECTOR, ".U3gSDe.ETvUZc .BVAVmf.I11szd.POX3ye .YXpkgd div[aria-haspopup='dialog']").get_attribute("aria-label")
                    except:
                        baggage_info = "No baggage info, please contact Airline"

                    info = {
                        'departure_time': flight.find_element(By.CSS_SELECTOR, "div[aria-label^='Departure time']").get_attribute("aria-label").split(": ")[1].strip(".").replace("\u202f", ""),
                        'arrival_time': flight.find_element(By.CSS_SELECTOR, "div[aria-label^='Arrival time']").get_attribute("aria-label").split(": ")[1].replace("\u202f", ""),
                        'departure_airport': flight.find_element(By.CSS_SELECTOR, ".PTuQse.sSHqwe.tPgKwe.ogfYpf .QylvBf:first-child span[jscontroller='cNtv4b']").text,
                        'arrival_airport': flight.find_element(By.CSS_SELECTOR, ".PTuQse.sSHqwe.tPgKwe.ogfYpf .QylvBf:last-child span[jscontroller='cNtv4b']").text,
                        'num_stops': num_stops,
                        'stop_info': flight.find_element(By.CSS_SELECTOR, ".BbR8Ec .sSHqwe.tPgKwe.ogfYpf").get_attribute("aria-label"),
                        'baggage_info': baggage_info,
                        'price': flight.find_element(By.CSS_SELECTOR, ".YMlIz.FpEdX span[data-gs]").get_attribute("aria-label")
                    }

                    flight_details.append(info)
                except Exception as e:
                    print(f"Error extracting details for flight: {str(e)}")
                    continue
                
            return flight_details

        flight_results = get_flight_info(driver)
        print(f"Total flights found: {len(flight_results)}")
        return flight_results
    except Exception as e:
        return {"error": str(e)}
    finally:
        driver.quit()
if __name__ == "__main__":
      search_flights(
        "LHR",
        "YUL",
        "2025-02-23",
        True
    )
@app.route('/api/search-flights', methods=['POST'])
def api_search_flights():
    # Get data from React frontend
    data = request.json
    departure = data.get('departure', 'JFK')
    arrival = data.get('arrival', 'YUL')
    date = data.get('date', '2025-02-23')
    one_way = data.get('one_way', True)

    # Call the flight search function
    results = search_flights(departure, arrival, date, one_way)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)