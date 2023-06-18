import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from linkedin profile,
    Manually scrape the information from the linkedin profile"""

    response = requests.get(linkedin_profile_url)
    data = response.json()

    # remove blanks and unnecessory information from response to reduce token size, there is a hard limit of 4K for gpt-3.5-turbo
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ["people_also_viewed", "certifications"]
    }

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
