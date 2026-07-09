import numpy as np
import cv2


from segment_anything import sam_model_registry
from segment_anything import SamAutomaticMaskGenerator
import os

# ===================================================
# LOAD SAM MODEL
# ===================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

checkpoint_path = os.path.join(
    BASE_DIR,
    "models",
    "sam_vit_b_01ec64.pth"
)

sam = sam_model_registry["vit_b"](
    checkpoint=checkpoint_path
)

mask_generator = SamAutomaticMaskGenerator(
    sam,
    points_per_side=32,
    pred_iou_thresh=0.88,
    stability_score_thresh=0.94,
    crop_n_layers=1,
    crop_n_points_downscale_factor=2,
    min_mask_region_area=1500
)


# ===================================================
# MAIN FUNCTION
# ===================================================

def extract_rooftop_sam(img_pil):

    image = np.array(img_pil)

# ------------------------------------------
# IMAGE RESIZE FOR FASTER SAM PROCESSING
# ------------------------------------------

    max_size = 1800

    h_original, w_original = image.shape[:2]

    scale = min(
        max_size / max(h_original, w_original),
        1.0
    )

    new_w = int(w_original * scale)
    new_h = int(h_original * scale)

    image = cv2.resize(
        image,
        (new_w, new_h)
    )

    h, w = image.shape[:2]

    # ===================================================
    # STEP 1 — SAM ROOFTOP MASK
    # (EXACTLY SAME AS FINAL WORKING CODE)
    # ===================================================

    masks = mask_generator.generate(image)

    rooftop_mask = np.zeros(
        (h, w),
        dtype=np.uint8
    )

    for mask_data in masks:

        area = mask_data["area"]

        if area < 1500 or area > (h * w * 0.90):
            continue

        segmentation = mask_data["segmentation"]

        rooftop_mask[segmentation] = 255

    # ===================================================
    # STEP 2 — BETTER OBSTACLE MASK
    # (FROM YOUR 2ND CODE)
    # ===================================================

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    blur = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # better dark object detection
    obstacle_mask = cv2.threshold(
        blur,
        95,
        255,
        cv2.THRESH_BINARY_INV
    )[1]

    dark_kernel = np.ones(
        (9, 9),
        np.uint8
    )

    obstacle_mask = cv2.dilate(
        obstacle_mask,
        dark_kernel,
        iterations=2
    )

    # ===================================================
    # STEP 3 — UNION OF WHITE REGIONS
    # (EXACT SAME FINAL LOGIC)
    # ===================================================

    union_mask = cv2.bitwise_or(
        rooftop_mask,
        obstacle_mask
    )

    # ===================================================
    # STEP 4 — FINAL USABLE AREA
    # black = usable
    # white = unusable
    # ===================================================

    final_mask = cv2.bitwise_not(
        union_mask
    )

    # ===================================================
    # STEP 5 — AREA CALCULATION
    # calculate directly from union image
    # black pixels = usable
    # ===================================================

    usable_pixels = np.sum(
        final_mask == 255
    )

    pixel_to_m2 = 0.0016

    usable_area_m2 = (
        usable_pixels
        * pixel_to_m2
    )

    print(
        f"Usable Area: {usable_area_m2:.2f} m²"
    )

    # ===================================================
    # VISUALIZATION
    # ===================================================

    # plt.figure(figsize=(18, 5))

    # plt.subplot(1, 3, 1)
    # plt.imshow(rooftop_mask, cmap="gray")
    # plt.title("SAM Rooftop Mask")
    # plt.axis("off")

    # plt.subplot(1, 3, 2)
    # plt.imshow(obstacle_mask, cmap="gray")
    # plt.title("Obstacle Mask")
    # plt.axis("off")

    # plt.subplot(1, 3, 3)
    # plt.imshow(final_mask, cmap="gray")
    # plt.title("Union Result (White = Usable)")
    # plt.axis("off")

    # plt.tight_layout()
    # plt.show()

    # ===================================================
    # RETURN
    # ===================================================

    return (
        rooftop_mask,
        obstacle_mask,
        final_mask,
        usable_area_m2
    )