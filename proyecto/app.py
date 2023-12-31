import os
import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

class VideoDownloaderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Tufy Downloader App")
        
        #Crear widgets
        self.label = tk.Label(master, text="Ingrese el enlace del video: ")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(master, width=40)
        self.entry.insert(0, "Ingrese el enlace aquí")
        self.entry.pack(pady=10)
        
        self.download_button = tk.Button(master, text="Descargar", command=self.download_video, bg="red")
        self.download_button.pack(pady=10)
        
    def download_video(self):
        try:
            url = self.entry.get()
            if not url.startswith("http"):
                messagebox.showerror("Error", "Ingrese un enlace válido")
                return
            
            #obtener la información del video
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension="mp4").first()
            
            #descargar el video
            download_folder = os.path.expanduser("~") #carpeta de descargas del usuario
            video.download(download_folder)
            
            messagebox.showinfo("Éxito", f"El video {yt.title} ha sido descargado en {download_folder}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Erro al descargar el video: {str(e)}")
            
def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()