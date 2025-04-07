def speed_limit(road_type, weather):
    limits = {
        'CITY': {'CLEAR': 50, 'RAIN': 40, 'FOG': 30},
        'RURAL': {'CLEAR': 100, 'RAIN': 80, 'FOG': 60},
        'HIGHWAY': {'CLEAR': float('inf'), 'RAIN': 130, 'FOG': 100}
    }
    return limits[road_type][weather]

def violation(speed, limit):
    return speed > limit

def faulty(filename):
    faulty_ids = []

    with open(filename, 'r') as file:
        for line in file:
            if not line.strip():
                continue  
            test_id, speed_str, road_type, weather, violation_flag = line.strip().split(';')
            speed = int(speed_str)
            limit = speed_limit(road_type, weather)
            expected_violation = violation(speed, limit)
            actual_violation = violation_flag.upper() == 'TRUE'

            if expected_violation != actual_violation:
                faulty_ids.append(test_id)

    
    return faulty_ids


faulty_tests = faulty('2025CGW Task 5 Input.txt' )

for test_id in faulty_tests:
    print(test_id)
