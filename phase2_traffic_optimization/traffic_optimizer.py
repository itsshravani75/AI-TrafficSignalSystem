try:
    from .config import (
        MIN_GREEN_TIME,
        MAX_GREEN_TIME,
        MAX_VEHICLE_COUNT
    )
except ImportError:
    from config import (
        MIN_GREEN_TIME,
        MAX_GREEN_TIME,
        MAX_VEHICLE_COUNT
    )
 
def calculate_density(vehicle_count):
    """
    Convert vehicle count into a density value from 0 to 1.
    """
 
    density = vehicle_count / MAX_VEHICLE_COUNT
 
    # Keep density between 0 and 1
    density = max(0.0, min(1.0, density))
 
    return density
 
 
def calculate_green_time(vehicle_count):
    """
    Calculate green signal duration based on traffic density.
    """
 
    density = calculate_density(vehicle_count)
 
    green_time = (
        MIN_GREEN_TIME
        + density * (MAX_GREEN_TIME - MIN_GREEN_TIME)
    )
 
    return round(green_time)
 
 
def calculate_priority(vehicle_count, waiting_time):
    """
    Calculate traffic priority using vehicle count
    and waiting time.
 
    70% importance is given to traffic density.
    30% importance is given to waiting time.
    """
 
    density = calculate_density(vehicle_count)
 
    # Normalize waiting time to 0-1
    normalized_waiting = min(waiting_time / 60, 1.0)
 
    priority = (
        0.70 * density
        + 0.30 * normalized_waiting
    )
 
    return priority
 
 
def select_next_direction(traffic_counts, waiting_times):
    """
    Select the direction with the highest priority.
    """
 
    priorities = {}
 
    for direction in traffic_counts:
 
        priorities[direction] = calculate_priority(
            traffic_counts[direction],
            waiting_times[direction]
        )
 
    next_direction = max(
        priorities,
        key=priorities.get
    )
 
    return next_direction, priorities
 
 
def optimize_signals(traffic_counts, waiting_times):
    """
    Calculate green time and select the next
    direction using traffic priority.
    """
 
    signal_times = {}
 
    for direction, count in traffic_counts.items():
 
        signal_times[direction] = calculate_green_time(count)
 
    next_direction, priorities = select_next_direction(
        traffic_counts,
        waiting_times
    )
 
    return signal_times, priorities, next_direction
 
 
if __name__ == "__main__":
 
    traffic_counts = {
        "NORTH": 12,
        "SOUTH": 7,
        "EAST": 18,
        "WEST": 4
    }
 
    waiting_times = {
        "NORTH": 20,
        "SOUTH": 35,
        "EAST": 10,
        "WEST": 50
    }
 
    signal_times, priorities, next_direction = optimize_signals(
        traffic_counts,
        waiting_times
    )
 
    print("\nADAPTIVE TRAFFIC SIGNAL OPTIMIZATION")
    print("-" * 50)
 
    for direction, count in traffic_counts.items():
 
        density = calculate_density(count)
        green_time = signal_times[direction]
        priority = priorities[direction]
 
        print(
            f"{direction}: "
            f"{count} vehicles | "
            f"density={density:.2f} | "
            f"waiting={waiting_times[direction]} sec | "
            f"priority={priority:.2f} | "
            f"green={green_time} sec"
        )
 
    print("-" * 50)
 
    print(
        f"NEXT GREEN SIGNAL: {next_direction}"
    )
 