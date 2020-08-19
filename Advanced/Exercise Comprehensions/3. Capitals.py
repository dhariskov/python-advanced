countries = input().split(", ")
capitals = input().split(", ")
combine = dict(zip(countries, capitals))
print("\n".join([f"{k} -> {v}" for k, v in combine.items()]))