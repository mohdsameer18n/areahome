import asyncio

# 🟢 CHANGED: Added all major Hyderabad areas (50+)
WARD_WATER_SCORES = {
    "Banjara Hills": 8.5, "Jubilee Hills": 8.5, "Gachibowli": 8.0,
    "Madhapur": 7.8, "Hitech City": 7.5, "Kondapur": 7.2,
    "Manikonda": 6.8, "Kukatpally": 6.5, "Nallagandla": 6.2, "Miyapur": 5.8,
    "ECIL": 6.0, "Secunderabad": 7.5, "Begumpet": 7.8, "Ameerpet": 7.0,
    "SR Nagar": 7.0, "Dilsukhnagar": 6.5, "LB Nagar": 6.2, "Uppal": 5.8,
    "Boduppal": 5.5, "Hayathnagar": 5.5, "Vanasthalipuram": 5.8,
    "Saroornagar": 5.8, "Mehdipatnam": 6.8, "Tolichowki": 6.5,
    "Attapur": 6.2, "Rajendra Nagar": 6.0, "Shamshabad": 5.5,
    "Nanakramguda": 7.0, "Kokapet": 7.5, "Narsingi": 7.0, "Gandipet": 6.5,
    "Patancheru": 5.5, "Kompally": 6.0, "Alwal": 6.5, "Malkajgiri": 6.8,
    "Nacharam": 6.0, "Kothapet": 6.2, "Chanda Nagar": 6.8, "Bachupally": 6.5,
    "Nizampet": 6.5, "Pragathi Nagar": 6.2, "Film Nagar": 7.5,
    "Panjagutta": 7.5, "Khairatabad": 7.2, "Masab Tank": 7.0,
    "Nampally": 6.8, "Abids": 7.0, "Himayatnagar": 7.5,
    "Narayanguda": 7.0, "Tarnaka": 6.8,
}

AREA_SAFETY = {
    "Banjara Hills": 9.0, "Jubilee Hills": 9.0, "Gachibowli": 8.5,
    "Madhapur": 7.5, "Hitech City": 7.5, "Kondapur": 7.0,
    "Manikonda": 6.5, "Kukatpally": 6.5, "Nallagandla": 6.0, "Miyapur": 6.0,
    "ECIL": 6.5, "Secunderabad": 7.5, "Begumpet": 8.0, "Ameerpet": 7.0,
    "SR Nagar": 7.0, "Dilsukhnagar": 6.0, "LB Nagar": 6.0, "Uppal": 5.8,
    "Boduppal": 5.5, "Hayathnagar": 5.5, "Vanasthalipuram": 5.8,
    "Saroornagar": 5.8, "Mehdipatnam": 6.5, "Tolichowki": 6.5,
    "Attapur": 6.0, "Rajendra Nagar": 6.2, "Shamshabad": 6.0,
    "Nanakramguda": 7.5, "Kokapet": 7.8, "Narsingi": 7.5, "Gandipet": 7.0,
    "Patancheru": 5.5, "Kompally": 7.0, "Alwal": 7.0, "Malkajgiri": 6.5,
    "Nacharam": 6.0, "Kothapet": 6.2, "Chanda Nagar": 7.0, "Bachupally": 7.0,
    "Nizampet": 7.0, "Pragathi Nagar": 6.5, "Film Nagar": 8.5,
    "Panjagutta": 7.5, "Khairatabad": 7.5, "Masab Tank": 7.2,
    "Nampally": 6.8, "Abids": 7.0, "Himayatnagar": 8.0,
    "Narayanguda": 7.0, "Tarnaka": 7.0,
}

AREA_IT = {
    "Hitech City": 10, "Madhapur": 9.5, "Gachibowli": 9.0,
    "Kondapur": 8.0, "Manikonda": 7.0, "Nallagandla": 6.5,
    "Kukatpally": 5.0, "Banjara Hills": 5.0, "Jubilee Hills": 5.0, "Miyapur": 4.0,
    "Nanakramguda": 8.5, "Kokapet": 8.0, "Narsingi": 7.0, "Begumpet": 6.0,
    "Ameerpet": 6.5, "ECIL": 5.0, "Secunderabad": 5.5, "SR Nagar": 5.0,
    "Dilsukhnagar": 3.0, "LB Nagar": 3.0, "Uppal": 4.5, "Boduppal": 3.5,
    "Hayathnagar": 2.5, "Vanasthalipuram": 3.0, "Saroornagar": 3.0,
    "Mehdipatnam": 5.0, "Tolichowki": 5.5, "Attapur": 4.0, "Rajendra Nagar": 4.0,
    "Shamshabad": 3.0, "Gandipet": 5.0, "Patancheru": 3.0, "Kompally": 4.0,
    "Alwal": 3.5, "Malkajgiri": 4.0, "Nacharam": 5.5, "Kothapet": 4.0,
    "Chanda Nagar": 5.5, "Bachupally": 4.0, "Nizampet": 5.0,
    "Pragathi Nagar": 4.5, "Film Nagar": 4.0, "Panjagutta": 5.5,
    "Khairatabad": 5.0, "Masab Tank": 5.0, "Nampally": 4.0, "Abids": 4.0,
    "Himayatnagar": 5.5, "Narayanguda": 5.0, "Tarnaka": 5.0,
}

AREA_SCHOOLS = {
    "Jubilee Hills": 9.0, "Banjara Hills": 9.0, "Kondapur": 8.0,
    "Gachibowli": 7.5, "Madhapur": 7.0, "Hitech City": 7.0,
    "Kukatpally": 7.0, "Manikonda": 6.0, "Miyapur": 6.0, "Nallagandla": 6.5,
    "ECIL": 7.0, "Secunderabad": 8.0, "Begumpet": 8.0, "Ameerpet": 7.5,
    "SR Nagar": 7.0, "Dilsukhnagar": 6.5, "LB Nagar": 6.5, "Uppal": 6.0,
    "Boduppal": 5.5, "Hayathnagar": 5.5, "Vanasthalipuram": 5.8,
    "Saroornagar": 5.8, "Mehdipatnam": 7.0, "Tolichowki": 6.5,
    "Attapur": 6.5, "Rajendra Nagar": 7.0, "Shamshabad": 5.5,
    "Nanakramguda": 6.5, "Kokapet": 7.0, "Narsingi": 6.5, "Gandipet": 6.0,
    "Patancheru": 5.5, "Kompally": 7.5, "Alwal": 7.0, "Malkajgiri": 7.0,
    "Nacharam": 6.5, "Kothapet": 6.5, "Chanda Nagar": 7.5, "Bachupally": 7.5,
    "Nizampet": 7.5, "Pragathi Nagar": 7.0, "Film Nagar": 7.5,
    "Panjagutta": 8.0, "Khairatabad": 7.5, "Masab Tank": 7.5,
    "Nampally": 7.0, "Abids": 7.5, "Himayatnagar": 8.5,
    "Narayanguda": 7.5, "Tarnaka": 8.0,
}

AREA_TRANSPORT = {
    "Miyapur": 9.0, "Kukatpally": 9.0, "Hitech City": 8.5,
    "Madhapur": 8.0, "Gachibowli": 7.5, "Banjara Hills": 7.0,
    "Kondapur": 7.5, "Jubilee Hills": 7.0, "Manikonda": 6.0, "Nallagandla": 5.0,
    "Ameerpet": 9.5, "Secunderabad": 9.5, "Begumpet": 9.0, "SR Nagar": 8.5,
    "ECIL": 8.0, "Uppal": 8.0, "Dilsukhnagar": 8.0, "LB Nagar": 8.5,
    "Boduppal": 6.5, "Hayathnagar": 6.0, "Vanasthalipuram": 7.0,
    "Saroornagar": 7.0, "Mehdipatnam": 8.0, "Tolichowki": 7.5,
    "Attapur": 7.0, "Rajendra Nagar": 7.0, "Shamshabad": 6.5,
    "Nanakramguda": 6.0, "Kokapet": 6.5, "Narsingi": 5.5, "Gandipet": 5.0,
    "Patancheru": 6.0, "Kompally": 7.0, "Alwal": 8.0, "Malkajgiri": 8.5,
    "Nacharam": 7.5, "Kothapet": 8.0, "Chanda Nagar": 7.0, "Bachupally": 7.0,
    "Nizampet": 7.5, "Pragathi Nagar": 7.0, "Film Nagar": 7.5,
    "Panjagutta": 8.5, "Khairatabad": 8.5, "Masab Tank": 8.0,
    "Nampally": 9.0, "Abids": 9.0, "Himayatnagar": 8.5,
    "Narayanguda": 8.0, "Tarnaka": 8.0,
}

AREA_GREENNESS = {
    "Jubilee Hills": 9.0, "Banjara Hills": 8.5, "Kondapur": 8.0,
    "Nallagandla": 8.0, "Gachibowli": 7.5, "Miyapur": 6.5,
    "Madhapur": 7.0, "Hitech City": 6.5, "Kukatpally": 5.5, "Manikonda": 6.0,
    "Gandipet": 9.0, "Narsingi": 8.0, "Kokapet": 7.5, "Nanakramguda": 7.5,
    "ECIL": 6.0, "Secunderabad": 6.5, "Begumpet": 6.5, "Ameerpet": 5.0,
    "SR Nagar": 5.0, "Dilsukhnagar": 5.0, "LB Nagar": 5.5, "Uppal": 5.0,
    "Boduppal": 6.0, "Hayathnagar": 6.5, "Vanasthalipuram": 6.0,
    "Saroornagar": 5.5, "Mehdipatnam": 6.0, "Tolichowki": 6.5,
    "Attapur": 6.5, "Rajendra Nagar": 7.0, "Shamshabad": 7.0,
    "Patancheru": 6.5, "Kompally": 7.5, "Alwal": 6.5, "Malkajgiri": 6.0,
    "Nacharam": 5.5, "Kothapet": 5.5, "Chanda Nagar": 7.0, "Bachupally": 7.0,
    "Nizampet": 7.0, "Pragathi Nagar": 6.5, "Film Nagar": 8.0,
    "Panjagutta": 6.0, "Khairatabad": 7.0, "Masab Tank": 6.5,
    "Nampally": 5.5, "Abids": 5.0, "Himayatnagar": 7.0,
    "Narayanguda": 6.0, "Tarnaka": 7.5,
}

# 🟢 NEW: Bachelor/Girl/Family friendliness scores per area
AREA_BACHELOR_SCORE = {
    "Hitech City": 9.5, "Madhapur": 9.0, "Gachibowli": 9.0, "Kondapur": 8.5,
    "Ameerpet": 9.0, "SR Nagar": 8.5, "Kukatpally": 8.0, "Manikonda": 7.5,
    "ECIL": 7.5, "Uppal": 7.5, "Tarnaka": 8.0, "Nacharam": 7.5,
    "Dilsukhnagar": 7.5, "LB Nagar": 7.0, "Secunderabad": 8.0,
    "Begumpet": 8.5, "Nanakramguda": 8.0, "Kokapet": 8.0,
    "Himayatnagar": 8.5, "Narayanguda": 8.0, "Panjagutta": 8.5,
    "Banjara Hills": 6.0, "Jubilee Hills": 5.5, "Kompally": 7.0,
    "Bachupally": 7.5, "Nizampet": 7.5, "Chanda Nagar": 7.5,
}

AREA_GIRL_FRIENDLY_SCORE = {
    "Banjara Hills": 9.5, "Jubilee Hills": 9.0, "Gachibowli": 8.5,
    "Film Nagar": 8.5, "Kondapur": 8.0, "Himayatnagar": 8.5,
    "Secunderabad": 8.0, "Begumpet": 8.0, "Madhapur": 7.5,
    "Hitech City": 7.5, "Kompally": 8.0, "Bachupally": 7.5,
    "Chanda Nagar": 7.5, "Nizampet": 7.5, "Kokapet": 8.0,
    "Nallagandla": 7.5, "Narsingi": 7.5, "Nanakramguda": 8.0,
    "Panjagutta": 8.0, "Narayanguda": 7.5, "Tarnaka": 7.5,
    "Ameerpet": 7.0, "SR Nagar": 7.0, "ECIL": 6.5,
}

AREA_FAMILY_SCORE = {
    "Jubilee Hills": 9.5, "Banjara Hills": 9.5, "Film Nagar": 9.0,
    "Kondapur": 8.5, "Nallagandla": 8.5, "Kompally": 9.0,
    "Bachupally": 8.5, "Nizampet": 8.5, "Chanda Nagar": 8.5,
    "Gachibowli": 8.0, "Secunderabad": 8.0, "Himayatnagar": 8.5,
    "Manikonda": 7.5, "Rajendra Nagar": 8.0, "Alwal": 8.0,
    "Malkajgiri": 7.5, "ECIL": 7.5, "Tarnaka": 8.0,
    "Miyapur": 7.5, "Kukatpally": 7.5, "Narsingi": 8.0, "Gandipet": 8.0,
}

# ✅ FAST VERSION (NO API CALLS)

async def get_water_score(lat: float, lng: float, area_name: str) -> float:
    return round(WARD_WATER_SCORES.get(area_name, 6.0), 1)


async def get_weather_score(lat: float, lng: float) -> tuple:
    weather_score = 7.2

    weather_details = {
        "temperature": "30°C",
        "humidity": "60%",
        "uv_index": 6.5,
        "rainfall": "2mm/day"
    }

    return weather_score, weather_details

def normalize_area(area_name: str):
    return area_name.title().strip()

def get_area_scores(area_name: str) -> dict:
    area_name = normalize_area(area_name)

    return {
        "Safety": AREA_SAFETY.get(area_name, 6.0),
        "IT Hub": AREA_IT.get(area_name, 5.0),
        "Schools": AREA_SCHOOLS.get(area_name, 6.0),
        "Transport": AREA_TRANSPORT.get(area_name, 6.0),
        "Greenness": AREA_GREENNESS.get(area_name, 6.0),
    }


def get_social_scores(area_name: str) -> dict:
    area_name = normalize_area(area_name)

    return {
        "Bachelor Score": AREA_BACHELOR_SCORE.get(area_name, 6.0),
        "Girl Friendly": AREA_GIRL_FRIENDLY_SCORE.get(area_name, 6.0),
        "Family Score": AREA_FAMILY_SCORE.get(area_name, 7.0),
    }