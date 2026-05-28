import numpy as np
import cv2

def extract_rooftop(img_pil):

    # Convert PIL image to NumPy array
    img = np.array(img_pil)

    # Convert RGB image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Blur image slightly to reduce noise
    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    # Detect rooftop edges
    edges = cv2.Canny(blur, 25, 110)

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Dilate edges to connect boundaries
    dilated = cv2.dilate(edges, kernel, iterations=2)

    # Close small gaps
    closing = cv2.morphologyEx(
        dilated,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Remove small noise regions
    opening = cv2.morphologyEx(
        closing,
        cv2.MORPH_OPEN,
        kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        opening,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Create black mask
    mask = np.zeros_like(gray)

    largest = None
    max_area = 0

    # Intelligent contour filtering
    for cnt in contours:

        area = cv2.contourArea(cnt)

        # Ignore tiny noise
        if area > 2000:

            perimeter = cv2.arcLength(cnt, True)

            approx = cv2.approxPolyDP(
                cnt,
                0.02 * perimeter,
                True
            )

            # Rooftops usually polygon-like
            if len(approx) >= 4:

                if area > max_area:
                    max_area = area
                    largest = cnt

    # Draw detected rooftop region
    if largest is not None:

        cv2.drawContours(
            mask,
            [largest],
            -1,
            255,
            thickness=cv2.FILLED
        )

    # -----------------------------------
    # USABLE ROOFTOP AREA CALCULATION
    # -----------------------------------

    # White pixels = usable rooftop area
    usable_pixels = np.sum(mask == 255)

    # Approximate area conversion
    # 1 pixel ≈ 0.001 m²
    pixel_to_m2 = 0.002

    solar_usability_factor = 0.65

    usable_area_m2 = usable_pixels * pixel_to_m2 * solar_usability_factor


    # -----------------------------------
    # VISUALIZATION
    # -----------------------------------

    # Invert mask for better visualization
    # White = usable rooftop
    # Black = obstacles/background
    inverted_mask = cv2.bitwise_not(mask)

    # Convert to RGB
    mask_rgb = cv2.cvtColor(
        inverted_mask,
        cv2.COLOR_GRAY2RGB
    )

    return mask_rgb, usable_area_m2