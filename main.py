def save_apod(api_key: str, path: str = ".") -> dict:
    apod_data = get_apod_data(api_key)
    img_url = apod_data["url"]
    img_name = img_url.split("/")[-1]
    response = requests.get(img_url, stream=True)

    with open(f"{path}/{img_name}", "wb+") as img_file:
        shutil.copyfileobj(response.raw, img_file)
    del response
    return apod_data


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    url = "https://images-api.nasa.gov/search"
    return requests.get(url, params={"q": query}).json()
