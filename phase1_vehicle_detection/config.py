# ============================================================
# AI TRAFFIC SIGNAL OPTIMIZATION SYSTEM
# Phase 1 - Vehicle Detection Configuration
# ============================================================
 
# Input traffic video
VIDEO_PATH = "videos/newtraffic.mp4"
 
# Output processed video
OUTPUT_VIDEO_PATH = "output/detected_traffic.mp4"
 
# YOLO model
MODEL_NAME = "yolo11s.pt"
 
# Minimum confidence for detection
CONFIDENCE_THRESHOLD = 0.25
 
# Vehicle classes from the COCO dataset
# 2  = car
# 3  = motorcycle
# 5  = bus
# 7  = truck
VEHICLE_CLASSES = {
    2: "car",
    3: "motorcycle",
    5: "bus",
    7: "truck"
}
 
# Display settings
SHOW_WINDOW = True
SAVE_OUTPUT = True

# ============================================================
# TRAFFIC ZONES - POLYGON AREAS
# ============================================================
 
# Each point is (x, y)
# Coordinates are based on the current traffic video.
 
NORTH_ZONE = [
    (1000, 40),
    (1230, 40),
    (1200, 300),
    (1050, 300)
]
 
SOUTH_ZONE = [
    (390, 864),
    (900, 864),
    (820, 700),
    (450, 700)
]
 
WEST_ZONE = [
    (0, 300),
    (430, 300),
    (520, 500),
    (0, 500)
]
 
EAST_ZONE = [
    (1280, 300),
    (1536, 330),
    (1536, 700),
    (1280, 680)
]
 