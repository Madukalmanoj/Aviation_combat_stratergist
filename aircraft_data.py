# Dictionary storing military aircraft details with only primary names (original case format)
aircraft_data = {
    "A-10": {"special_abilities": ["Heavy armor", "GAU-8 Avenger cannon"], "counter": "SAMs, air superiority fighters"},
    "A-400M": {"special_abilities": ["Heavy transport", "Multi-role"], "counter": "Air interceptors"},
    "AG-600": {"special_abilities": ["Amphibious", "Firefighting"], "counter": "Limited combat use"},
    "AH-64": {"special_abilities": ["Advanced sensors", "Tank killer"], "counter": "Anti-air weapons"},
    "AV-8B": {"special_abilities": ["VTOL", "Close air support"], "counter": "Fast interceptors"},
    "An-124": {"special_abilities": ["Heavy transport"], "counter": "Air superiority fighters"},
    "An-225": {"special_abilities": ["Largest cargo aircraft"], "counter": "Air interceptors"},
    "B-1": {"special_abilities": ["Supersonic bomber", "Long-range strike"], "counter": "Advanced SAMs, interceptors"},
    "B-2": {"special_abilities": ["Stealth", "Global strike"], "counter": "Advanced SAMs"},
    "B-21": {"special_abilities": ["Next-gen stealth bomber"], "counter": "Highly classified"},
    "B-52": {"special_abilities": ["Heavy bomber", "Nuclear capable"], "counter": "Fighter interceptors, SAMs"},
    "C-130": {"special_abilities": ["Tactical transport", "Multi-role"], "counter": "Air interceptors"},
    "C-17": {"special_abilities": ["Strategic airlift"], "counter": "Air interceptors"},
    "C-5": {"special_abilities": ["Largest U.S. transport"], "counter": "Air superiority fighters"},
    "F-4": {"special_abilities": ["Fast interceptor", "Multirole"], "counter": "Modern 4th & 5th-gen fighters"},
    "F-14": {"special_abilities": ["Variable-sweep wings", "Fleet defense"], "counter": "Modern stealth fighters"},
    "F-15": {"special_abilities": ["High speed", "Air superiority"], "counter": "Stealth aircraft"},
    "F-16": {"special_abilities": ["Highly maneuverable", "Affordable"], "counter": "5th-gen fighters"},
    "F/A-18": {"special_abilities": ["Carrier-based", "Multi-role"], "counter": "Stealth fighters"},
    "F/A-18E/F": {"special_abilities": ["Advanced Hornet", "Carrier-capable"], "counter": "Stealth aircraft"},
    "F-22": {"special_abilities": ["Stealth", "Supercruise"], "counter": "Advanced SAMs, next-gen fighters"},
    "F-35": {"special_abilities": ["Stealth", "Sensor fusion"], "counter": "Highly advanced air defenses"},
    "MiG-29": {"special_abilities": ["Agility", "Dogfight capability"], "counter": "Stealth fighters"},
    "MiG-31": {"special_abilities": ["High speed", "Interceptor"], "counter": "Stealth aircraft, SAMs"},
    "Su-27": {"special_abilities": ["Supermaneuverability", "Air superiority"], "counter": "Stealth aircraft"},
    "Su-30": {"special_abilities": ["Multi-role", "BVR combat"], "counter": "Stealth fighters"},
    "Su-35": {"special_abilities": ["Thrust vectoring", "Supermaneuverability"], "counter": "Stealth aircraft"},
    "Su-57": {"special_abilities": ["Stealth", "Supermaneuverability"], "counter": "F-22, F-35, advanced SAMs"},
    "J-20": {"special_abilities": ["Stealth", "Advanced radar"], "counter": "F-22, F-35, advanced air defenses"},
    "J-35": {"special_abilities": ["Stealth", "Carrier-capable"], "counter": "F-22, F-35"},
    "Eurofighter": {"special_abilities": ["Agility", "BVR combat"], "counter": "Stealth aircraft"},
    "Rafale": {"special_abilities": ["Carrier-capable", "Advanced electronics"], "counter": "Stealth aircraft, advanced SAMs"},
    "MQ-9": {"special_abilities": ["Long endurance", "Precision strike"], "counter": "Advanced electronic warfare"},
    "TB-2": {"special_abilities": ["Affordable", "Effective against ground targets"], "counter": "Electronic warfare, air defenses"},
    "SR-71": {"special_abilities": ["Extreme speed", "High altitude"], "counter": "No direct counter, extreme SAMs"},
    "Tu-160": {"special_abilities": ["Supersonic bomber", "Nuclear capable"], "counter": "Advanced interceptors, SAMs"},
    "X-47B": {"special_abilities": ["Carrier-based stealth drone"], "counter": "Electronic warfare"},
    "XQ-58": {"special_abilities": ["Loyal wingman drone"], "counter": "Anti-UAV systems"},
    "U-2": {"special_abilities": ["High-altitude reconnaissance"], "counter": "SAMs"},
}

# Function to clean input (remove spaces, hyphens, and make it case-insensitive)
def clean_input(name):
    return name.lower().replace("-", "").replace("/", "").replace("(", "").replace(")", "").strip()

# Convert aircraft database keys into a case-insensitive searchable format
cleaned_aircraft_data = {clean_input(name): name for name in aircraft_data}

# Function to get aircraft details
def get_aircraft_info(aircraft_name):
    cleaned_name = clean_input(aircraft_name)

    if cleaned_name in cleaned_aircraft_data:
        original_name = cleaned_aircraft_data[cleaned_name]  # Get correct casing
        details = aircraft_data[original_name]
        return f"\n **Aircraft**: {original_name}\n🔹 **Special Abilities**: {', '.join(details['special_abilities'])}\n🔹 **Countermeasures**: {details['counter']}\n"
    
    return " Aircraft not found in the database."

# Main execution loop
if __name__ == "__main__":
    print("🔍 **Military Aircraft Database**")
    while True:
        user_input = input("\nEnter aircraft name (or 'exit' to stop): ").strip()
        if not user_input:
            print(" Please enter a valid aircraft name.")
            continue
        if user_input.lower() == "exit":
            print(" Goodbye!")
            break
        print(get_aircraft_info(user_input))
