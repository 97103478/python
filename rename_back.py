import os

def rename_back_to_original():
    # Standaard map-pad
    folder_path = r"C:\Users\Silas\.git\movie_posters\movie_posters"
    
    try:
        # Toon menu en vraag om keuze
        print("1. Hernoem en nummer bestanden")
        print("2. Hernoem bestanden naar originele naam")
        choice = input("Kies ? ")
        
        if choice == "1":
            # Vraag om map-pad bij keuze 1
            folder_path = input("Geef de naam van de map met afbeeldingen: ")
            if not os.path.exists(folder_path):
                print(f"De map {folder_path} bestaat niet!")
                return
                
            files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            files.sort()
            
            for index, old_name in enumerate(files, start=1):
                new_number = f"{index:02d}"
                new_name = f"movie_poster_{new_number}{os.path.splitext(old_name)[1]}"
                old_path = os.path.join(folder_path, old_name)
                new_path = os.path.join(folder_path, new_name)
                os.rename(old_path, new_path)
                print(f"Hernoemd: {old_name} -> {new_name}")
            
        elif choice == "2":
            # Hernoem terug naar originele namen met behulp van image_list.txt
            if not os.path.exists(folder_path):
                print(f"De map {folder_path} bestaat niet!")
                return
                
            # Lees originele namen uit image_list.txt (aanname: aangemaakt in Opdracht 1)
            list_file = "image_list.txt"
            if not os.path.exists(list_file):
                print("image_list.txt niet gevonden! Maak eerst Opdracht 1.")
                return
                
            with open(list_file, 'r', encoding='utf-8') as f:
                original_names = [line.strip() for line in f if line.strip()]
            
            current_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
            current_files.sort()
            
            for index, current_name in enumerate(current_files):
                if index < len(original_names):
                    old_path = os.path.join(folder_path, current_name)
                    new_path = os.path.join(folder_path, original_names[index])
                    os.rename(old_path, new_path)
                    print(f"Hernoemd: {current_name} -> {original_names[index]}")
                else:
                    print(f"Geen originele naam beschikbaar voor {current_name}")
            
        else:
            print("Ongeldige keuze!")
            
        print("Klaar!")
        
    except Exception as e:
        print(f"Er is een fout opgetreden: {str(e)}")

if __name__ == "__main__":
    rename_back_to_original()