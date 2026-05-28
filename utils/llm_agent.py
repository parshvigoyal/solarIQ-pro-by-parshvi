import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Hugging Face API URLs
HF_API_URL_PRIMARY = os.getenv("HF_API_URL_PRIMARY")
HF_API_URL_FALLBACK = os.getenv("HF_API_URL_FALLBACK")

# Hugging Face API Key
HF_API_KEY = os.getenv("HF_API_KEY")

# API URL list
HF_API_URLS = [
    HF_API_URL_PRIMARY,
    HF_API_URL_FALLBACK
]


def get_ai_recommendations(rooftop_data):

    # Validate API key
    if not HF_API_KEY:
        raise Exception(
            "Missing HF_API_KEY environment variable."
        )

    # Request headers
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    # AI Prompt
    prompt = (
        f"Given the rooftop solar metrics below, "
        f"provide detailed solar installation "
        f"recommendations, financial outlook "
        f"including ROI, and maintenance tips:\n\n"

        f"Detected Rooftop Area (m2): "
        f"{rooftop_data['detected_area_m2']}\n"

        f"Annual Solar Generation (kWh): "
        f"{rooftop_data['solar_metrics']['annual_generation_kWh']}\n"

        f"System Cost (INR): "
        f"{rooftop_data['solar_metrics']['system_cost_inr']}\n"

        f"Annual Savings (INR): "
        f"{rooftop_data['solar_metrics']['annual_savings_inr']}\n"

        f"ROI Payback Period (Years): "
        f"{rooftop_data['solar_metrics']['roi_years']}\n"
    )

    # Model payload
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.5
        }
    }

    last_error = None

    # Try APIs one by one
    for url in HF_API_URLS:

        if not url:
            continue

        try:

            response = requests.post(
                url,
                headers=headers,
                json=payload,
                timeout=10
            )

            # Successful response
            if response.status_code == 200:

                result = response.json()

                # Hugging Face list response
                if (
                    isinstance(result, list)
                    and len(result) > 0
                    and 'generated_text' in result[0]
                ):
                    return result[0]['generated_text']

                # Hugging Face dict response
                elif (
                    isinstance(result, dict)
                    and 'generated_text' in result
                ):
                    return result['generated_text']

                # Fallback safe conversion
                else:
                    return str(result)

            else:
                last_error = Exception(
                    f"Error {response.status_code}: "
                    f"{response.text} from {url}"
                )

        except Exception as e:
            last_error = e

    # Final failure
    raise last_error or Exception(
        "All Hugging Face API URLs failed."
    )

