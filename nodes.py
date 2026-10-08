"""MVA prompt builder with bilingual dropdown labels and exact English LoRA captions."""

AZIMUTH_CAPTIONS = [
    ("正面 | front view", "front view"),
    ("右前方 | front-right view", "front-right view"),
    ("右前四分之一侧面 | front-right quarter view", "front-right quarter view"),
    ("右侧面 | right side view", "right side view"),
    ("右后四分之一侧面 | back-right quarter view", "back-right quarter view"),
    ("右后方 | back-right view", "back-right view"),
    ("背面 | back view", "back view"),
    ("左后方 | back-left view", "back-left view"),
    ("左后四分之一侧面 | back-left quarter view", "back-left quarter view"),
    ("左侧面 | left side view", "left side view"),
    ("左前四分之一侧面 | front-left quarter view", "front-left quarter view"),
    ("左前方 | front-left view", "front-left view"),
]
ELEVATION_CAPTIONS = [
    ("平视 | eye-level shot", "eye-level shot"),
    ("略微俯视 | elevated shot", "elevated shot"),
    ("高角度俯拍 | high-angle shot", "high-angle shot"),
    ("正上方俯拍 | top-down shot", "top-down shot"),
]
AZIMUTH_MAP = dict(AZIMUTH_CAPTIONS)
ELEVATION_MAP = dict(ELEVATION_CAPTIONS)
AZIMUTH_OPTIONS = list(AZIMUTH_MAP)
ELEVATION_OPTIONS = list(ELEVATION_MAP)


class MVAPromptBuilder:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "azimuth": (AZIMUTH_OPTIONS, {"default": AZIMUTH_OPTIONS[0]}),
            "elevation": (ELEVATION_OPTIONS, {"default": ELEVATION_OPTIONS[0]}),
            "close_up": ("BOOLEAN", {"default": False, "label_on": "特写开", "label_off": "特写关"}),
        }}

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "build_prompt"
    CATEGORY = "MVA"

    def build_prompt(self, azimuth, elevation, close_up):
        # Also accept old workflow values that used English-only selections.
        azimuth_en = AZIMUTH_MAP.get(azimuth, azimuth)
        elevation_en = ELEVATION_MAP.get(elevation, elevation)
        if azimuth_en not in AZIMUTH_MAP.values() or elevation_en not in ELEVATION_MAP.values():
            raise ValueError("Unknown MVA angle option")
        prompt = f"<mva> {azimuth_en}, {elevation_en}"
        if close_up:
            prompt += " close-up"
        return (prompt,)


NODE_CLASS_MAPPINGS = {"MVAPromptBuilder": MVAPromptBuilder}
NODE_DISPLAY_NAME_MAPPINGS = {"MVAPromptBuilder": "MVA 多角度提示词生成器"}
