def name_matches_custom_plugin(name):
    has_khm_prefix = name.lower().startswith("khm")
    has_mtap_prefix = name.lower().startswith("mtap")

    return (has_khm_prefix or has_mtap_prefix)


f = open("plugins.txt", "r")

for x in f:
    if name_matches_custom_plugin(x):
        continue

    print("wp plugin install", x)