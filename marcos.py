import requests

def closest_stores(addr, city, state, postal_code):
    link = "https://www.marcos.com/api/stores/searchByStreetAddress"
    params = f"?orderType=Pickup&street={addr}&city={city}&state={state}&zip={postal_code}&radius=25&country=US"
    r = requests.get(link + params).json()

    stores = []
    store_id = ""
    addr = ""

    for x in r["results"]:
        store_id = int(x["id"].split("#")[1])
        addr = x["address"] + " " + x["name"].split(" - ")[1]
        stores.append([addr, store_id])

    return stores

stores = closest_stores(
    "1111 Example Street",
    "Memphis",
    "TN",
    "37501"
)

for x in stores:
    print(f"\nAddress: {x[0]}\nStore ID: {x[1]}")