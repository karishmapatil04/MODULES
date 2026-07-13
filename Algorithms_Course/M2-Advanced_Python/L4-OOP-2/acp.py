# My Art Gallery Collection Manager

class ArtGallery:
    def __init__(self, gallery_name):
        self.gallery_name = gallery_name
        self.artworks = []
        print("Welcome to", self.gallery_name)

    def add_artwork(self):
        art = input("Enter artwork name: ")
        self.artworks.append(art)
        print("Artwork added successfully!")

    def view_artworks(self):
        if len(self.artworks) == 0:
            print("No artworks in the gallery.")
        else:
            print("\nArtworks in the Gallery:")
            for art in self.artworks:
                print("-", art)

    def __del__(self):
        print("Gallery closed. Thank you!")

# Create object
gallery = ArtGallery("Creative Art Gallery")

# Menu
while True:
    print("\n--- Menu ---")
    print("1. Add Artwork")
    print("2. View Artworks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        gallery.add_artwork()
    elif choice == "2":
        gallery.view_artworks()
    elif choice == "3":
        del gallery
        break
    else:
        print("Invalid choice! Please try again.")