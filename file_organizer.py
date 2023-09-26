import os

user_folder = "XAPC"
main_folder = "Downloads" 
users_folder = "Users"
path = "/{}/{}/{}/".format(users_folder,user_folder,main_folder)

def create_folders():  
    folders = ["pdf","Words","Imagenes","videos","Excel","Ejecutables",
                    "PowerPoint","SQL","Torrents","Extraibles","Draw.io","Python",
                    "Instaladores","Ebook","Java","txt","ISO","SVG","HTML",
                    "PHP", "Packet","Musica","PowerBi", "Visio", "Bash"] 
    
    for folder in folders:
        folder_path = os.path.join(path, folder)

        if not os.path.exists(folder_path):
                try: 
                    os.mkdir(folder_path)
                    print("Carpeta creada: " + folder)
                except Exception as e:
                    print(f"Error al crear la carpeta '{folder}': {e}")
        else: 
            pass

if __name__ == "__main__":
    original_filename = os.listdir(path)
    create_folders()
    for filename in original_filename:
        
        name, extension = os.path.splitext(path + filename)

        if extension in [".pdf"]:
            folder = "/{}/{}/{}/pdf/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".docx", ".doc", ".rtf", ".odt"]:
            folder = "/{}/{}/{}/Words/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".jpg", ".jpeg", ".png", ".PNG", ".JPG"]:
            folder = "/{}/{}/{}/Imagenes/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".mp4", ".MOV", ".mkv"]:
            folder = "/{}/{}/{}/videos/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".xlsx", ".csv", ".xls"]:
            folder = "/{}/{}/{}/Excel/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".exe"]:
            folder = "/{}/{}/{}/Ejecutables/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".pptx"]:
            folder = "/{}/{}/{}/PowerPoint/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".sql"]:
            folder = "/{}/{}/{}/SQL/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".torrent"]:
            folder = "/{}/{}/{}/Torrents/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".rar", ".zip", ".7z"]:
            folder = "/{}/{}/{}/Extraibles/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".drawio"]:
            folder = "/{}/{}/{}/Draw.io/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".py"]:
            folder = "/{}/{}/{}/Python/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".msi"]:
            folder = "/{}/{}/{}/Instaladores/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".epub"]:
            folder = "/{}/{}/{}/Ebook/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".java"]:
            folder = "/{}/{}/{}/Java/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".txt"]:
            folder = "/{}/{}/{}/txt/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".iso"]:
            folder = "/{}/{}/{}/ISO/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".svg"]:
            folder = "/{}/{}/{}/SVG/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".html", ".htm"]:
            folder = "/{}/{}/{}/HTML/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)
        
        elif extension in [".php"]:
            folder = "/{}/{}/{}/PHP/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".pkt"]:
            folder = "/{}/{}/{}/Packet/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)
        
        elif extension in [".mp3", ".ogg"]:
            folder = "/{}/{}/{}/Musica/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)
        
        elif extension in [".pbix"]:
            folder = "/{}/{}/{}/PowerBi/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

        elif extension in [".vsdx"]:
            folder = "/{}/{}/{}/Visio/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)
        
        elif extension in [".sh"]:
            folder = "/{}/{}/{}/Bash/".format(users_folder,user_folder,main_folder)
            os.rename(path + filename, folder + filename)

      
        
        
            

