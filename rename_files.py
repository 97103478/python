import os

def rename_files():
    # Standaard map-pad
    folder_path = r"C:\Users\Silas\.git\movie_posters\movie_posters"
    
    try:
        # Haal alle bestandsnamen op uit de map
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Sorteer bestanden op naam (optioneel, voor consistente nummering)
        files.sort()
        
        # Hernoem bestanden
        for index, old_name in enumerate(files, start=1):
            # Maak nieuwe naam met leading zero voor nummers < 10
            new_number = f"{index:02d}"
            new_name = f"movie_poster_{new_number}{os.path.splitext(old_name)[1]}"
            
            old_path = os.path.join(folder_path, old_name)
            new_path = os.path.join(folder_path, new_name)
            
            # Hernoem het bestand
            os.rename(old_path, new_path)
            print(f"Hernoemd: {old_name} -> {new_name}")
        
        print(f"Alle {len(files)} bestanden zijn succesvol hernoemd!")
        
    except Exception as e:
        print(f"Er is een fout opgetreden: {str(e)}")

if __name__ == "__main__":
    rename_files()