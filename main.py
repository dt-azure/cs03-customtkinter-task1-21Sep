import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def render_pack():
    app = customtkinter.CTk()
    app.geometry("500x500")
    
    main_frame1 = customtkinter.CTkFrame(master=app, fg_color="white")
    main_frame1.pack(side="top", expand=True, fill="both")
    main_frame2 = customtkinter.CTkFrame(master=app, fg_color="white")
    main_frame2.pack(side="bottom", expand=True, fill="both")

    frame1 = customtkinter.CTkFrame(master=main_frame1, fg_color="red")
    frame1.pack(side="left", expand=True, fill="both")
    frame2 = customtkinter.CTkFrame(master=main_frame1, fg_color="yellow")
    frame2.pack(side="right", expand=True, fill="both")
    frame2 = customtkinter.CTkFrame(master=main_frame2, fg_color="blue")
    frame2.pack(side="left", expand=True, fill="both")
    frame2 = customtkinter.CTkFrame(master=main_frame2, fg_color="brown")
    frame2.pack(side="right", expand=True, fill="both")

    app.mainloop()
    
def render_place():
    app = customtkinter.CTk()
    app.geometry("500x500")
    
    frame1 = customtkinter.CTkFrame(master=app, fg_color="red")
    frame1.place(relx=0, rely=0, relheight=0.5, relwidth=0.5)
    frame2 = customtkinter.CTkFrame(master=app, fg_color="yellow")
    frame2.place(relx=0.5, rely=0, relheight=0.5, relwidth=0.5)
    frame2 = customtkinter.CTkFrame(master=app, fg_color="blue")
    frame2.place(relx=0, rely=0.5, relheight=0.5, relwidth=0.5)
    frame2 = customtkinter.CTkFrame(master=app, fg_color="brown")
    frame2.place(relx=0.5, rely=0.5, relheight=0.5, relwidth=0.5)
    
    app.mainloop()
    
def render_grid():
    app = customtkinter.CTk()
    app.geometry("500x500")
    app.grid_columnconfigure(0, weight=1)
    app.grid_columnconfigure(1, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_rowconfigure(1, weight=1)

    frame1 = customtkinter.CTkFrame(master=app, fg_color="red")
    frame1.grid(row=0, column=0, sticky="nsew")
    frame2 = customtkinter.CTkFrame(master=app, fg_color="yellow")
    frame2.grid(row=0, column=1, sticky="nsew")
    frame2 = customtkinter.CTkFrame(master=app, fg_color="blue")
    frame2.grid(row=1, column=0, sticky="nsew")
    frame2 = customtkinter.CTkFrame(master=app, fg_color="brown")
    frame2.grid(row=1, column=1, sticky="nsew")
    
    app.mainloop()
    
def main():
    # render_pack()
    # render_place()
    render_grid()


if __name__ == "__main__":
    main()