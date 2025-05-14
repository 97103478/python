import os

def generate_file_list():
    # Vraag om de map met afbeeldingen
    folder_path = input("Voer het pad naar de map met afbeeldingen in (of druk Enter voor standaardpad): ")
    
    # Gebruik standaardpad als niets wordt ingevoerd
    if not folder_path:
        folder_path = r"C:\Users\Silas\.git\movie_posters\movie_posters"
    
    try:
        # Controleer of de map bestaat
        if not os.path.exists(folder_path):
            print(f"De map {folder_path} bestaat niet!")
            return
        
        # Haal alle bestandsnamen op uit de map
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        # Maak een tekstbestand met de bestandsnamen
        output_file = "image_list.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            for file_name in files:
                f.write(file_name + '\n')
        
        print(f"Tekstbestand '{output_file}' is succesvol aangemaakt met {len(files)} bestandsnamen!")
        
    except Exception as e:
        print(f"Er is een fout opgetreden: {str(e)}")

if __name__ == "__main__":
    generate_file_list()