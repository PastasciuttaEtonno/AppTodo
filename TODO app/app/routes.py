from re import S
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import ModifyForm, TodoForm
from app.items import Item
from app.list import ListItem
from flask import request

items=[] #oggeto contenente listaoggetti items todo
listItems=ListItem()

#view funtion
@app.route('/')#routing e effuttuato da queste funzioni decorator
@app.route('/index')
def index():

    output=render_template('index.html', title="Home", items=listItems.getList())
    return output


@app.route('/addItem',methods=["GET","POST"])
def login():

    form=TodoForm()
  
    if form.validate_on_submit():
        item=Item(form.text.data,form.title.data)
        listItems.addItem(item)
        listItems.changeId()

        return redirect(url_for("index"))
    return render_template('addItem.html',title="Add TODO", form=form)
    

@app.route('/modifyItem/<id>',methods=["GET","POST"])
def modifyItem(id):
     

    id=int(id)
    list=listItems.getList()
    #item=copy.deepcopy(listItems.getSelectedItem(id))#la funzione non va  cazzo
    form=ModifyForm()

    for i in range(len(list)):
        if list[i].getId()==id:
            print(list[i].getId())
            print (list[i])

    selectedItem=listItems.getSelectedItem(id)
    

    if form.validate_on_submit():
        print("dentro")
        ##set dei nuovi attributi dell item
        # print(selectedItem.getText())
        # print(selectedItem.getTitle())
        # print(selectedItem.getDone())
        # print(selectedItem.getDone())
   
        selectedItem.setText(form.title.data)
        selectedItem.setTitle(form.text.data)
        if selectedItem.getDone()=="completato":
            selectedItem.setDone(False)
        else:
            selectedItem.setDone(True)

        print(form.radio.data)

        return redirect(url_for("index"))

    elif listItems.getSelectedItem(id) is not None:
        form.title.data=selectedItem.getTitle()
        form.text.data=selectedItem.getText()
        form.radio.data=selectedItem.getDone()
   
    return render_template('modifyItem.html',title="Add TODO", form=form)


@app.route('/present/<name>')
def present(name):
    return f"<h1> Buongiorno {name} </h1>"


@app.route('/delete/<id>')
def delete(id):
    
    itemss=listItems.getList()

    if len(itemss)==1:
        itemss.clear()
        return redirect(url_for("index"))
    # del(itemss[int(id)])
    itemss.remove(listItems.getSelectedItem(int(id)))

    return redirect(url_for("index"))


