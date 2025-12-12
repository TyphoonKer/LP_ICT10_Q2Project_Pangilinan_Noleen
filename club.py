from js import document


clubs = {
   "DM": {
       "name": "Mastering Dungeon Master Club",
       "description": "Sharpen your storytelling, world-building, and improvisation skills as you learn to run unforgettable campaigns. This club guides aspiring Dungeon Masters through creating engaging adventures, managing player dynamics, and bringing epic tales to life behind the screen.",
       "time": "Every Thursday 3:00–5:30 PM",
       "location": "Room 308",
       "advisor": "Mr. Beholder",
       "members": 20,
    
   },
   "Bard": {
       "name": "Bards Instruments Club",
       "description": "Celebrate creativity and performance through the music and magic of the bardic arts. Members explore fantasy-inspired instruments, practice musical storytelling, and enhance role-playing skills that make every in-game moment more vibrant and memorable..",
       "time": "Every Monday 2:30–5:00 PM",
       "location": "Music Room",
       "advisor": "Ms. Blights",
       "members": 20,
   },
   "Cleric": {
       "name": "Clerics Basic Aid Club",
       "description": "Learn the fundamentals of support, strategy, and in-game healing as you step into the role of a devoted cleric. This club teaches essential mechanics, teamwork techniques, and the lore behind divine magic to help you become a reliable and resourceful party protector.",
       "time": "Every Wednesday 3:00–5:00 PM",
       "location": "Gym",
       "advisor": "Coach Treant",
       "members": 20,
    
}
}


def show_info(event):
   selected = document.getElementById("club_select").value
   club = clubs[selected]


   info = (
       f"{club['name']}\n"
       f"Description: {club['description']}\n"
       f"Time: {club['time']}\n"
       f"Location: {club['location']}\n"
       f"Advisor: {club['advisor']}\n"
       f"Number of Members: {club['members']}\n"
    
   )


   box = document.getElementById("club_output")
   box.style.display = "block"
   box.innerText = info

