# Module 5 Game: Amapiano Gig Manager

def run_gig_manager():
    print("=" * 45)
    print("🎵  AMAPIANO GIG & PLAYLIST MANAGER  🎵")
    print("=" * 45)
    
    # Sets automatically prevent duplicate VIP ticket entries
    vip_guestlist = {"Sipho", "Lerato", "Thabo"}
    
    # List of dictionaries for track selection
    setlist = [
        {"track": "izinto", "producer": "dj maphorisa", "bpm": 113},
        {"track": "jazzidisciples", "producer": "busta 929", "bpm": 112}
    ]
    
    while True:
        print("\n--- GIG MENU ---")
        print("1. View VIP Guestlist")
        print("2. Add VIP Guest")
        print("3. View Live Setlist")
        print("4. Drop New Track")
        print("5. Exit Gig")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            print("\n📋 Current Unique VIP Guestlist:")
            for guest in vip_guestlist:
                print(f"- {guest}")
                
        elif choice == "2":
            new_guest = input("Enter guest name to add to VIP: ").strip().title()
            if new_guest:
                vip_guestlist.add(new_guest)
                print(f"✨ {new_guest} added to VIP (No duplicates allowed!)")
                
        elif choice == "3":
            print("\n🎧 LIVE SETLIST:")
            for idx, item in enumerate(setlist, start=1):
                # Using string methods for clean formatting
                formatted_track = item["track"].upper()
                formatted_prod = item["producer"].title()
                print(f"{idx}. {formatted_track} produced by {formatted_prod} ({item['bpm']} BPM)")
                
        elif choice == "4":
            t_name = input("Enter track title: ").strip().lower()
            t_prod = input("Enter producer name: ").strip().lower()
            try:
                t_bpm = int(input("Enter BPM speed: ").strip())
                setlist.append({"track": t_name, "producer": t_prod, "bpm": t_bpm})
                print("🎶 Track loaded onto the decks successfully!")
            except ValueError:
                print("❌ Invalid BPM. Please enter a number.")
                
        elif choice == "5":
            print("\n🎉 Gig closed down! Great party vibes everyone!")
            break
        else:
            print("❌ Invalid choice. Pick between 1 and 5.")

if __name__ == "__main__":
    run_gig_manager()