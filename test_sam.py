from segment_anything import sam_model_registry

sam = sam_model_registry["vit_b"](
    checkpoint="models/sam_vit_b_01ec64.pth"
)

print("SAM Loaded Successfully")