import view

hasil = []
hasil_akhir = 0
hasil_str = 0

def reset_view() :
    view.output_var.set("")
    
def button_angka_click(input_user) : 
    ''' menampilkan apa yang di input oleh user '''
    if view.output_var.get() in ("x", "/", "+", "-") :
        
        hasil.append(view.output_var.get())
        reset_view()
        print(hasil)

    if view.output_var.get() == "Erorr" :
        reset_view()

    isi_sekarang = view.output_var.get()
    view.output_var.set(isi_sekarang + str(input_user))

def button_operasi_click(operasi) :
    ''' menampilkan operasi apa yang di input oleh user '''
    if view.output_var.get() not in ("x", "/", "+", "-") :
        hasil.append(view.output_var.get())
        print(hasil)
        
    reset_view()
    view.output_var.set(operasi)

def button_hasil() :
    global hasil
    global hasil_akhir
    global hasil_str
    if view.output_var.get() != "" :
        hasil.append(view.output_var.get())
        reset_view()
        print(hasil)
    
    try : 
        hasil_str = "".join(hasil).replace("x", "*")
        hasil_akhir = eval(hasil_str)
        if hasil_akhir == int(hasil_akhir) :
            view.output_var.set(int(hasil_akhir))
        else :
            view.output_var.set(hasil_akhir)
        hasil = []
        
    except :
        view.output_var.set("Erorr")


def clear() :
    global hasil
    global hasil_akhir
    global hasil_str
    reset_view()
    hasil = []
    hasil_akhir = 0
    hasil_str = 0



