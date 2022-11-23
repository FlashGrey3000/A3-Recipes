from tkinter import *
import mysql.connector as mc

Ingredients =["Bread","Cheese","Milk","Carrot","Rice","Egg","Wheat","Potato","Paneer","Noodle","Meat"]

Dishes = [
    ["Sandwich","Starter","Bread, Cheese","Corn, Mushroom, Onion, Cucumber, Carrot"],
    ["Double Ka Meetha","Dessert","Bread, Milk","Pista, Cashew, Almond"],
    ["Carrot Pudding","Dessert","Carrot","Milk, Cashew, Almond, Pista"],
    ["Rice Pudding","Dessert","Rice, Milk","Casahew, Almond, Pista"],
    ["MilkShake","Beverage","Milk","Vanilla Essence"],
    ["Scrambled Eggs","Main","Egg","Onion, Green Chilli"],
    ["Egg Rice","Main","Egg, Rice","Onion, Green Chilli"],
    ["Potato Paratha","Main","Potato, Wheat","Green Chilli, Onion"],
    ["Biryani","Main","Meat, Rice","Onion, Spices"],
    ["Paneer Tikka","Starter","Paneer","Onion, Capsicum, Tomato"],
    ["Chicken Chilli","Starter","Meat","Onion, Tomato, Green Chilli"],
    ["Egg Bonda","Starter","Egg, Wheat","Sauce"],
    ["Potato Bites","Starter","Potato, Cheese","Sauce"],
    ["Cutlet","Starter","Potato, Carrot, Bread","Green Chilli, Onion, Cheese"],
    ["Paneer Sandwich","Main","Paneer, Bread, Cheese","Green Chilli, Onion, Sauce"],
    ["Noodle","Main","Noodle","Sauce, Onion, Green Chilli"],
    ["Egg Noodle","Main","Egg, Noodle","Sauce, Onion, Green Chilli"],
    ["Cheese Noodle","Main","Noodle, Cheese","Sauce, Onion"],
    ["Paneer Rice","Main","Paneer, Rice","Spices, Sauce, Onion"],
    ["Chicken Noodle","Main","Meat, Noodle","Sauce, Spices, Onion, Green chilli"],
    ["Samosa","Starter","Wheat, Potato","Green Chilli, Onion, Spices"],
    ["Pancake","Dessert","Egg, Milk, Wheat","Honey, Butter"],
    ["Poha","Main","Rice, Potato","Nuts, Onion, Green Chilli"],
    ["Carrot Patties","Main","Carrot, Wheat, Egg","Honey, Green Chilli, Cheese"]
]



def Create_db():
    conn = mc.connect(host='localhost',user='root',passwd='root')
    c = conn.cursor()
    c.execute("CREATE DATABASE IF NOT EXISTS A3Recipe")
    conn.commit()
    
    c.execute("USE A3Recipe")
    c.execute("DROP TABLE IF EXISTS dishes")
    conn.commit()

    c.execute("""CREATE TABLE dishes(
        ID int PRIMARY KEY AUTO_INCREMENT,
        Name varchar(25),
        Course varchar(15),
        Ingredients_main varchar(254),
        Ingredients_optional varchar(254))""")
    conn.commit()

    for name,course,main_ingredients,optional_ingredients in Dishes:
        c.execute("INSERT INTO dishes(Name,Course,Ingredients_main,Ingredients_optional) VALUES ('{}','{}','{}','{}')".format(name,course,main_ingredients,optional_ingredients))
    conn.commit()

    conn.close()

Create_db()

def add_recipe():    

    add_recipe_page = Toplevel(root)
    add_recipe_page.geometry('400x600')

    rname = Entry(add_recipe_page)
    rname.grid(column=1,row=0)
    rcourse = Entry(add_recipe_page)
    rcourse.grid(column=1,row=1)
    rcourse_label = Label(add_recipe_page,text="Enter recipe Course: ")
    rcourse_label.grid(row=1,column=0)
    rname_label = Label(add_recipe_page,text="Enter recipe name: ")
    rname_label.grid(row=0,column=0)
    ing_label = Label(add_recipe_page,text="Select Ingredients:- ")
    ing_label.grid(row=2,column=0)

    var = StringVar()

    bread_rb = Radiobutton(add_recipe_page,text="Bread",variable=var,value="Bread").grid(column=1,row=3)
    cheese_rb = Radiobutton(add_recipe_page,text="Cheese",variable=var,value="Cheese").grid(column=1,row=4)
    milk_rb = Radiobutton(add_recipe_page,text="Milk",variable=var,value="Milk").grid(column=1,row=5)
    carrot_rb = Radiobutton(add_recipe_page,text="Carrot",variable=var,value="Carrot").grid(column=1,row=6)
    rice_rb = Radiobutton(add_recipe_page,text="Rice",variable=var,value="Rice").grid(column=1,row=7)
    egg_rb = Radiobutton(add_recipe_page,text="Egg",variable=var,value="Egg").grid(column=1,row=8)
    wheat_rb = Radiobutton(add_recipe_page,text="Wheat",variable=var,value="Wheat").grid(column=1,row=9)
    potato_rb = Radiobutton(add_recipe_page,text="Potato",variable=var,value="Potato").grid(column=1,row=10)
    paneer_rb = Radiobutton(add_recipe_page,text="Paneer",variable=var,value="Paneer").grid(column=1,row=11)
    noodle_rb = Radiobutton(add_recipe_page,text="Noodle",variable=var,value="Noodle").grid(column=1,row=12)
    meat_rb = Radiobutton(add_recipe_page,text="Meat",variable=var,value="Meat").grid(column=1,row=13)

    

    ings=[]
    def add_ing():
        ing=var.get()
        ings.append(ing)
        ings_label = Label(add_recipe_page,text=ings).grid(column=1,row=14,pady=10)
    print(var.get())
    add_ing_btn = Button(add_recipe_page, text="Add ingredient", command=add_ing)
    add_ing_btn.grid(column=1,row=15)

    
    def confirm_recipe():
        f_ing=''
        for i in ings:
            f_ing+=i+' ,'
        f_ing=f_ing.rstrip(' ,')

        final_recipe = [(rname.get(), rcourse.get(), f_ing, 'None')]

        conn = mc.connect(host='localhost',user='root',passwd='root',database='a3recipe')
        c = conn.cursor()
        for name,course,main_ingredients,optional_ingredients in final_recipe:
            c.execute("INSERT INTO dishes(Name,Course,Ingredients_main,Ingredients_optional) VALUES ('{}','{}','{}','{}')".format(name,course,main_ingredients,optional_ingredients))
        conn.commit()
        conn.close()
        add_recipe_page.destroy()
        print(final_recipe)

    confirm_recipe_btn = Button(add_recipe_page,text="CONFIRM RECIPE", command=confirm_recipe,pady=7.5,padx=15)
    confirm_recipe_btn.grid(column=1,row=17,pady=25)

    

    


def show_recipe():
    conn = mc.connect(host='localhost',user='root',passwd='root',database='a3recipe')
    c = conn.cursor()

    show_recipe_page = Tk()
    show_recipe_page.geometry('1200x600')
    recipe_label=Label(show_recipe_page, text="RECIPES  ",font=('Helvetica Bold',26), pady= 20,padx= 500,bg='#F85757').grid(row=0,column=0,columnspan=6)

    c.execute("SELECT * FROM dishes")
    x = c.fetchall()
    texts=''

    l=[]
    
    for tuple in x:
        l2=[]
        for element in tuple:
            l2.append(element)
        l.append(l2)
    r=1
    for list in l:
        list[0]=str(list[0]).ljust(3)
        list[1]=list[1].ljust(40)
        list[2]=list[2].ljust(20)
        list[3]=list[3].ljust(35)
        list[4]=list[4].ljust(40)
        c=0
        for ele in list:
            kek_label = Label(show_recipe_page, text=ele,justify='left').grid(row=r,column=c)
            c+=1
        r+=1


    

    conn.close()


def update_recipe(r_id):
    update_recipe_page = Tk()
    update_recipe_page.geometry('400x600')

    head_label = Label(update_recipe_page, text= 'New Recipe Details',font=('Helvetica Bold',18), pady= 20,padx=100,bg='#F8E95B').grid(column=0,columnspan=2,row=0)
    n_recipe_label = Label(update_recipe_page, text='Name:     \t').grid(column=0,row=1)
    n_recipe = Entry(update_recipe_page)
    n_recipe.grid(column=1,row=1, padx=50)
    n_course_label = Label(update_recipe_page, text='Course [main/starter/dessert]: ').grid(column=0,row=2)
    n_course = Entry(update_recipe_page)
    n_course.grid(row=2,column=1)
    n_ing_label = Label(update_recipe_page, text= 'Select new Ingredients').grid(row=3,column=0)

    u_var = StringVar()
    u_var.set('Bread')

    def setvar(y):
        u_var.set(y)

    bread_rb = Radiobutton(update_recipe_page,text="Bread",variable=u_var,value="Bread",command=lambda: setvar('Bread')).grid(column=0,row=4,columnspan=2)
    cheese_rb = Radiobutton(update_recipe_page,text="Cheese",variable=u_var,value="Cheese",command=lambda: setvar('Cheese')).grid(column=0,row=5,columnspan=2)
    milk_rb = Radiobutton(update_recipe_page,text="Milk",variable=u_var,value="Milk",command=lambda: setvar('Milk')).grid(column=0,row=6,columnspan=2)
    carrot_rb = Radiobutton(update_recipe_page,text="Carrot",variable=u_var,value="Carrot",command=lambda: setvar('Carrot')).grid(column=0,row=7,columnspan=2)
    rice_rb = Radiobutton(update_recipe_page,text="Rice",variable=u_var,value="Rice",command=lambda: setvar('Rice')).grid(column=0,row=8,columnspan=2)
    egg_rb = Radiobutton(update_recipe_page,text="Egg",variable=u_var,value="Egg",command=lambda: setvar('Egg')).grid(column=0,row=9,columnspan=2)
    wheat_rb = Radiobutton(update_recipe_page,text="Wheat",variable=u_var,value="Wheat",command=lambda: setvar('Wheat')).grid(column=0,row=10,columnspan=2)
    potato_rb = Radiobutton(update_recipe_page,text="Potato",variable=u_var,value="Potato",command=lambda: setvar('Potato')).grid(column=0,row=11,columnspan=2)
    paneer_rb = Radiobutton(update_recipe_page,text="Paneer",variable=u_var,value="Paneer",command=lambda: setvar('Paneer')).grid(column=0,row=12,columnspan=2)
    noodle_rb = Radiobutton(update_recipe_page,text="Noodle",variable=u_var,value="Noodle",command=lambda: setvar('Noodle')).grid(column=0,row=13,columnspan=2)
    meat_rb = Radiobutton(update_recipe_page,text="Meat",variable=u_var,value="Meat",command=lambda: setvar('Meat')).grid(column=0,row=14,columnspan=2)
    
    ingr=[]
    def update_ings():
        ing = u_var.get()
        ingr.append(ing)
        sh_ing_label = Label(update_recipe_page, text=ingr,pady=10).grid(row=15,column=0,columnspan=2)

    update_ings_btn = Button(update_recipe_page, text='Update Ingredients',command=update_ings).grid(row=16,column=0,columnspan=2)

    
    def final_update():
        conn = mc.connect(host='localhost',user='root',passwd='root',database='a3recipe')
        c = conn.cursor()
        f_ing=''
        for i in ingr:
            f_ing+=i+' ,'
        f_ing=f_ing.rstrip(' ,')
        c.execute('UPDATE dishes SET Name = "{}", Course = "{}", Ingredients_main = "{}" WHERE ID = {}'.format(n_recipe.get(), n_course.get(), f_ing, int(r_id)))
        conn.commit()
        conn.close()

        print('RECORD UPDATED')

        update_recipe_page.destroy()

    update_recipe_btn = Button(update_recipe_page, text='UPDATE RECIPE',pady=10,padx=15,command=final_update).grid(row=17,column=0,columnspan=2,pady=25)


        



def delete_recipe(r_id):
    delete_recipe_page = Tk()
    
    def del_recipe():
        conn = mc.connect(host='localhost',user='root',passwd='root',database='a3recipe')
        c = conn.cursor()

        c.execute('SELECT ID, Name, Course FROM dishes WHERE ID = ' + r_id)
        x=c.fetchall()

        print('RECORD DELETED ',x)

        c.execute('DELETE FROM dishes WHERE ID = ' + r_id)
        conn.commit()

        conn.close()

        delete_recipe_page.destroy()

    del_btn = Button(delete_recipe_page, text="DELETE RECORD", font=('Times New Roman', 14),bg='Red', command= del_recipe, padx=25,pady=15).pack()


def search_recipe():
    search_recipe_page = Tk()
    search_recipe_page.geometry('450x450')

    var = StringVar()

    def setvar(y):
        var.set(y)

    sel_label = Label(search_recipe_page, text="Select ingredients available with you:- ").grid(row=0,column=0)
    bread_rb = Radiobutton(search_recipe_page,text="Bread",variable=var,value="Bread",command=lambda: setvar('Bread')).grid(column=1,row=3)
    cheese_rb = Radiobutton(search_recipe_page,text="Cheese",variable=var,value="Cheese",command=lambda: setvar('Cheese')).grid(column=1,row=4)
    milk_rb = Radiobutton(search_recipe_page,text="Milk",variable=var,value="Milk",command=lambda: setvar('Milk')).grid(column=1,row=5)
    carrot_rb = Radiobutton(search_recipe_page,text="Carrot",variable=var,value="Carrot",command=lambda: setvar('Carrot')).grid(column=1,row=6)
    rice_rb = Radiobutton(search_recipe_page,text="Rice",variable=var,value="Rice",command=lambda: setvar('Rice')).grid(column=1,row=7)
    egg_rb = Radiobutton(search_recipe_page,text="Egg",variable=var,value="Egg",command=lambda: setvar('Egg')).grid(column=1,row=8)
    wheat_rb = Radiobutton(search_recipe_page,text="Wheat",variable=var,value="Wheat",command=lambda: setvar('Wheat')).grid(column=1,row=9)
    potato_rb = Radiobutton(search_recipe_page,text="Potato",variable=var,value="Potato",command=lambda: setvar('Potato')).grid(column=1,row=10)
    paneer_rb = Radiobutton(search_recipe_page,text="Paneer",variable=var,value="Paneer",command=lambda: setvar('Paneer')).grid(column=1,row=11)
    noodle_rb = Radiobutton(search_recipe_page,text="Noodle",variable=var,value="Noodle",command=lambda: setvar('Noodle')).grid(column=1,row=12)
    meat_rb = Radiobutton(search_recipe_page,text="Meat",variable=var,value="Meat",command=lambda: setvar('Meat')).grid(column=1,row=13)

    sings=[]
    def makelabel():
        sings.append(var.get())
        sings_label = Label(search_recipe_page, text=sings).grid(column=1,row=14)

    sel_btn = Button(search_recipe_page, text='Select Ingredient', command=makelabel).grid(column=1,row=15)

    def search():
        final = Tk()
        keke = Label(final,text="The Dishes that can be made with ingredients:-",font=('Calibri',13),pady=25,bg='yellow').grid(row=0,column=0,columnspan=2)
        conn = mc.connect(host='localhost',user='root',passwd='root',database='a3recipe')
        c = conn.cursor()

        c.execute('Select * from dishes')
        x=c.fetchall()

        k=1
        for record in x:
            for i in sings:
                if i in record[3]:
                    sno_label = Label(final, text="SNO",pady=2,).grid(row=0+k,column=0,columnspan=4)
                    sno = Label(final, text=record[0],pady=2).grid(row=0+k,column=1,columnspan=4)
                    name_label = Label(final, text="Name: ",pady=2,).grid(row=1+k,column=0,columnspan=4)
                    name = Label(final, text=record[1],pady=2).grid(row=1+k,column=1,columnspan=4)
                    course_label = Label(final, text="course: ",pady=2,).grid(row=2+k,column=0,columnspan=4)
                    course = Label(final, text=record[2],pady=2).grid(row=2+k,column=1,columnspan=4)
                    ingrs_label = Label(final, text="Ingredients: ",pady=2,).grid(row=3+k,column=0,columnspan=4)
                    ingrs = Label(final, text=record[3],pady=2).grid(row=3+k,column=1,columnspan=4)
                    sep_label = Label(final,text='---*---'*10).grid(row=4+k,column=0,columnspan=4)
                    k+=5

        conn.close()


    confirm_btn = Button(search_recipe_page, text='Confirm Ings', pady=10,padx=15,command=search).grid(column=1,row=16)



def admin():
    admin_page = Toplevel(root)
    admin_page.geometry('450x450')

    admin_label=Label(admin_page, text=" ADMIN",font=('Helvetica Bold',26), pady= 20,padx= 162,bg='#F8E95B').grid(row=0,column=0,columnspan=2)
    

    add_recipe_button = Button(admin_page, text="ADD RECIPE",padx=20,pady=10,command=add_recipe)
    add_recipe_button.place(x=160,y=100)
    show_recipe_button = Button(admin_page, text="SHOW RECIPES", padx=20,pady=10,command=show_recipe)
    show_recipe_button.place(x=151,y=160)
    recipe_id = Entry(admin_page)
    recipe_id.place(x=190,y=245)
    recipe_id_label = Label(admin_page,text="Enter ID:").place(x=135,y=245)
    update_recipe_button = Button(admin_page,text="UPDATE RECIPE",padx=20,pady=10,command=lambda: update_recipe(recipe_id.get()))
    update_recipe_button.place(x=148,y=285)
    delete_recipe_button = Button(admin_page,text="DELETE RECIPE",padx=20,pady=10,command=lambda: delete_recipe(recipe_id.get()))
    delete_recipe_button.place(x=150,y=345)


def guest():
    guest_page = Tk()
    guest_page.geometry('450x450')
    guest_label=Label(guest_page, text=" GUEST",font=('Helvetica Bold',26), pady= 20,padx= 162,bg='#F8E95B').grid(row=0,column=0,columnspan=2)
    show_recipe_button = Button(guest_page, text="SHOW RECIPES", padx=20,pady=10,command=show_recipe)
    show_recipe_button.place(x=151,y=100)
    search_recipe_button = Button(guest_page, text="SEARCH RECIPES", padx=20,pady=10,command=search_recipe)
    search_recipe_button.place(x=145,y=160)



root = Tk()
root.geometry('450x450')
root.title("A3 Recipe")

welcome_label=Label(root, text="WELCOME",font=('Helvetica Bold',26), pady= 20,padx= 135,bg='#95A9DB').grid(row=0,column=0,columnspan=2)

login_label = Label(root, text="LOGIN", font=('Helvetica',16),pady=10).grid(row=1,column=0,columnspan=2)


username = Entry(root)
username.grid(row=2,column=1)
passwd = Entry(root)
passwd.grid(row=3,column=1)

username_label = Label(root, text="Username:").grid(row=2,column=0)
passwd_label = Label(root, text="Password:").grid(row=3,column=0)

def login():
    if (username.get(),passwd.get())==('admin','root'):
        admin()
    else:
        guest()


login_button = Button(root, text="Login", pady=10,padx=20,command=login).grid(row=4,column=0,columnspan=2)



root.mainloop()