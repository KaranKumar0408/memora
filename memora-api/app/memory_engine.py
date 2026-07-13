memory_profiles = {}

def create_profile(
    name,
    style,
    asset_type,
    primary_color
):
    memory_profiles[name] = {
        "name": name,
        "style": style,
        "asset_type": asset_type,
        "primary_color": primary_color,
    }

    print(memory_profiles)

    return memory_profiles[name]


def get_profile(name):
    return memory_profiles.get(name)

def get_all_profiles():
    return list(memory_profiles.values())