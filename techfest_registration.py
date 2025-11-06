print("Welcome to SMIT TechFest!")
print("Event organized by [Your Full Name] of APPDAET [Your Section]")


try:
    num_participants = int(input("How many participants will register? "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

if num_participants <= 0:
    print("No participants to register.")
    exit()


participants = []
print("\n--- Register Participants ---")

for i in range(num_participants):
    name = input(f"Enter participant {i + 1} name: ").strip()
    track = input(f"Enter chosen track for {name}: ").strip()
    participants.append({"name": name, "track": track})


print("\nRegistered Participants:")
for idx, p in enumerate(participants, 1):
    print(f"{idx}. {p['name']} - {p['track']}")


unique_tracks = set(p["track"] for p in participants)
print(f"\nTracks offered: {', '.join(sorted(unique_tracks))}")

if len(unique_tracks) < 2:
    print("Warning: Not enough track variety.")


