from django.shortcuts import render, redirect

from .models import Formdata,Menu,content_for_Menu,carousel_Image
from application.forms import contentform

# A VIEW TO CREATE FORM
def createform(request):
    code=""
    if request.session.has_key('username') and Formdata.objects.filter(username =request.session['username'] ):
        username_f=request.session['username'] 
        form_source_code=""
        list=Formdata.objects.all()
        for element in list:
            if element.username==username_f:
                code=element.code          
                    
    if request.method=='POST':
        var=0
        code=["<div class='container'><div id='yourform'><h2 style='color:white;font-size:25px;font-weight:500;'>FORM:<hr style='height:1px;border:none;color:white;background-color:white;' ></h2><form action="" >"]
        formvaluename=request.POST.get("nameofinput")
        formvaluetype=request.POST.get("typeofinput")
        while formvaluename and formvaluetype:
            addtocode="<div class='form-group'><div style='color:white;font-size:15px;font-weight:500;'>"+formvaluename+": </div>"+ "<input type=" +formvaluetype + "  class='form-control'  ><br></div>"
            code.append(addtocode)
            var+=1
            formvaluename=request.POST.get("nameofinput"+str(var))
            formvaluetype=request.POST.get("typeofinput"+str(var))
        code.append("<input type='submit' value='submit' ><hr style='height:1px;border:none;color:white;background-color:white;' >")
        code.append("</form></div></div>")
        code=" ".join(code)
        username=request.session['username'] 
        dbusername = Formdata.objects.filter(username = username)
        if dbusername:
            Formdata.objects.filter(username = username).delete()
        new_obj=Formdata(username=username,code=code)
        new_obj.save()
        return redirect("createform")

    elif request.session.has_key('username'):
        username = request.session['username']
        navbarcode=" "
        dbusername=Menu.objects.filter(username=username)
        if dbusername:
            list=Menu.objects.all()
            for elements in list:
                if elements.username==username:
                    navbarcode=elements.navbarcode
        return render(request,'createform.html',{'username':username,'navbarcode':navbarcode,'code':code})

    else:
        return redirect("/home/")

#A VIEW TO CREATE MENU AND UPDATE AND DELETE
def createmenu(request):
    if request.session.has_key("username"):
        insertcode="<ul><li><div class='listmenu' name='1div' > "
        insertcode+=" <span style='width:350px;color:black;font-weight:500;font-size:20px;' >NAME:<span><input type='text' class='nameofmenu'  name='1name' required> "
        insertcode+="<input type='button'  value='&#10133;' class='buttonofmenu  btn btn-sm btn-outline-secondary' name='1button' onclick='newsubitem(name)'  data-toggle='modal' data-target='#ModalLongmenu'>"
        insertcode+="<input type='button'  value='&#10008;' class='deletemenu btn btn-sm btn-outline-danger' name='1delbutton' onclick='deletemenu(name)' >"
        insertcode+="<input type='hidden' class='parentofmenu' value=0 name='1parent'>"
        insertcode+="<input type='hidden' value='enabled' class='status' name='1status'>"
        insertcode+="</div></li></ul>"
        displaymenucode=""
        displaycss="<style>\n.dropdown-submenu \n{\nposition: relative;\n}\n.dropdown-submenu .dropdown-menu\n {\ntop: 0;\nleft: 100%;\nmargin-top: -1px;\n}\n</style>"
        displayjs="<script>\n$(document).ready(function(){\n$('.dropdown-submenu a.test').on('click', function(e){\n $(this).next('ul').toggle();\ne.stopPropagation();\ne.preventDefault();\n});\n});\n</script>"
        navbarcode=" "
        num=1
        mainheading=""
        username_f=request.session['username']
        if request.method=="POST" :
            main=[]
            menuid=1
            n=request.POST.get(str(menuid)+"name")
            k=request.POST.get(str(menuid)+"parent")
            status=request.POST.get(str(menuid)+"status")
            counter=1
            while n and k:
                a={'id':0,'name':"",'parent':0,'code':"",'displaycode':"",'status':""}
                a['id']=menuid
                a['name']=n
                a['parent']=int(k)
                a['status']=status
                if a['status']!='disabled' :#a['status']=='enabled':
                    s=str(a['id'])+"div"
                    t=str(a['id'])+"li"
                    a['code']=f"<li name={t} ><div class='listmenu' name={s} >"

                    s=str(counter) +"name"                
                    a['code']+=f" <span style='color:black;font-weight:500;font-size:20px;' >NAME:</span> <input type='text' class='nameofmenu form-control form-horizontal' value= {a['name']} name={s} style='width:350px;display:inline' required>"
                    
                    s=str(counter) +"button"
                    a['code']+=f"<input type='button' value='&#10133;' class='buttonofmenu btn btn-sm btn-outline-secondary' name={s} style='display:inline' onclick='newsubitem(name)' data-toggle='modal' data-target='#ModalLongmenu'>"
                    
                    s=str(counter) +"delbutton"
                    a['code']+=f"<input type='button' value='&#10008;' class='deletemenu btn btn-sm btn-outline-danger' name={s} onclick='deletemenu(name)'> "
                    
                    s=str(counter) +"parent"
                    p=str(a['parent'])
                    a['code']+=f"<input type='hidden' class='parentofmenu' value={p} name={s}></li>"
                    
                    st=str(counter) +"status"
                    a['code']+=f"<input type='hidden' class='status' value={a['status']} name={st}></li>"
                    
                    link="/content/"+a['name']
                    n=a['name']
                    a['displaycode']=f"<li class='dropdown-submenu dropright' ><a href={link} role='button'  class='test dropdown-item btn'>{n}</a></li>"
                    
                    counter+=1
                    main.append(a) 
                menuid+=1
                status=request.POST.get(str(menuid)+"status")
                n=request.POST.get(str(menuid)+"name")
                k=request.POST.get(str(menuid)+"parent")
                #print(status)
            menucode=["<ul>"]
            displaymenucode=["<head>\n<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css'>\n"]
            displaymenucode.append("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.4.0/jquery.min.js'></script>\n")
            displaymenucode.append("<script src='https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js'></script>\n")
            displaymenucode.append("</head>\n<body>\n")
            displaymenucode.append("<div class='dropdown'><a class='dropdown-toggle nav-link dropdown-toggle dropdown-toggle-split navbartext navinsertmenu' aria-haspopup='true' aria-expanded='false'  data-toggle='dropdown'>"+request.POST.get("mainheading")+"   <span class='caret'></span></a>")
            displaymenucode.append("<ul class='dropdown-menu'>")
            mainheading=request.POST.get("mainheading")
            newmain=[]
            num=len(main)
            
            for item in main:#initialise newmain
                newmain.append(item)
            for i in range(0,len(newmain)-1):#sort newmain
                for j in range(0,len(newmain)-1):
                    if newmain[j]['parent']<newmain[j+1]['parent']:
                        newmain[j],newmain[j+1]=newmain[j+1],newmain[j]
            for item in main:
                check=item['id']
                i=0
                for checking in main:
                    if checking['parent']==check:
                        i=1
                if i==1:
                    s=item['name']
                    item['displaycode']=f"<li class='dropdown-submenu dropright'><a id={s} class='test tests dropdown-item btn' style='width:200px;' >{s} <span style='float:right;' > &#10151;</span></a></li>"
                elif i==0:
                    link="/content/"+item['name']
                    s=item['name']
                    item['displaycode']=f"<li ><a href={link} role='button'  class='test dropdown-item btn'>{s}</a></li>"
            for item in newmain:
                c=item['parent']
                if c>0:
                    if not("<ul>" in main[c-1]['code']):
                        s=item['code']
                        main[c-1]['code']=main[c-1]['code']+f"<ul>{s}</ul>"
                    elif ("<ul>" in main[c-1]['code']):
                        s=item['code']
                        main[c-1]['code']=main[c-1]['code'][:-5]+f"{s}</ul>"
            for item in newmain:
                c=item['parent']
                if c>0:
                    if not(("</ul>") in main[c-1]['displaycode']):
                        main[c-1]['displaycode']=main[c-1]['displaycode'][:-9]+'<div style="display:inline;font-weight:900;"></div>'+"</a></li>"
                        s=item['displaycode']
                        main[c-1]['displaycode']=main[c-1]['displaycode'][:-5]+f"<ul class='dropdown-menu'>{s}</ul></li>"
                    elif ("</ul>" in main[c-1]['code']):
                        s=item['displaycode']
                        main[c-1]['displaycode']=main[c-1]['displaycode'][:-10]+f"{s}</ul></li>"                
            for child in main:
                if child['parent']==0:
                    menucode.append(child['code'])
            for child in main:
                if child['parent']==0:
                    displaymenucode.append(child['displaycode'])
            menucode.append("</ul>")
            displaymenucode.append("</ul></div>\n</body>")
            
            menucode=" ".join(menucode)
            displaymenucode=" ".join(displaymenucode)
            navbarcode=displaymenucode.split("<body>")[1]
            navbarcode=navbarcode.split("</body>")[0]
            displaycode=displaymenucode
            dbusername = Menu.objects.filter(username = username_f)
            if dbusername:
                Menu.objects.filter(username = username_f).delete()
            newobj=Menu(mycode=menucode,username=username_f,num=num,displaycode=displaymenucode,displaycss=displaycss,displayjs=displayjs,navbarcode=navbarcode)
            newobj.save()
            a=Menu.objects.all()
            for item in a:
                if item.username==username_f:
                    insertcode=item.mycode
        dbusername = Menu.objects.filter(username = username_f)
        if dbusername:
            list=Menu.objects.all()
            for element in list:
                if element.username==username_f:
                    insertcode=element.mycode
                    num=element.num
                    displaymenucode=element.displaycode
                    displaycss=element.displaycss
                    displayjs=element.displayjs
                    navbarcode=element.navbarcode
        return render(request,"menu.html",{'username':username_f,'insert_code':insertcode,'num':num,'displaycode':displaymenucode,'displaycss':displaycss,'displayjs':displayjs,'navbarcode':navbarcode,'mainheading':mainheading})
    else:
        return redirect("/home/")

#A VIEW TO CREATE CONTENT FOR SPECIFIC MENU
def contentformenuview(request,name):
    if request.session.has_key('username') and content_for_Menu.objects.filter(username=request.session['username']) and content_for_Menu.objects.filter(name=name):
        if request.method=="POST":
            form=contentform(request.POST)
            if form.is_valid():
                username=request.session['username']
                dbusername = content_for_Menu.objects.filter(username = username)
                dbname=content_for_Menu.objects.filter(name=name)
                if dbusername and dbname:
	                content_for_Menu.objects.filter(username = username).delete()
                c=form.cleaned_data['content']
                a=content_for_Menu(username=username,content=c,name=name)
                a.save()
        elements=content_for_Menu.objects.all()
        for element in elements:
            if element.username==request.session['username']:
                if element.name==name:
                    code=element.content
                    navbarcode=" "
                    dbusername=Menu.objects.filter(username=request.session['username'])
                    if dbusername:
                        list=Menu.objects.all()
                        for elements in list:
                            if elements.username==request.session['username']:
                                navbarcode=elements.navbarcode
                                form=contentform()
                    return render(request,"content.html",{'username':request.session['username'],'navbarcode':navbarcode,'name':name,'code':code,'form':form})
    elif request.session.has_key('username'):
        if request.method=="POST":
            form=contentform(request.POST)
            if form.is_valid():
                username=request.session['username']
                dbusername = content_for_Menu.objects.filter(username = username)
                dbname=content_for_Menu.objects.filter(name=name)
                if dbusername and dbname:
	                content_for_Menu.objects.filter(username = username).delete()
                c=form.cleaned_data['content']
                a=content_for_Menu(username=username,content=c,name=name)
                a.save()
                return redirect('/content/'+name)
        else:
            form=contentform()
            navbarcode=" "
            dbusername=Menu.objects.filter(username=request.session['username'])
            if dbusername:
                list=Menu.objects.all()
                for elements in list:
                    if elements.username==request.session['username']:
                        navbarcode=elements.navbarcode
            return render(request,'content.html',{'form':form,'username':request.session['username'],'navbarcode':navbarcode,'name':name})
#A VIEW TO CREATE CAROUSEL
def addcarousel(request):
    images=[]
    if request.session.has_key('username') and carousel_Image.objects.filter(username =request.session['username'] ):
        username=request.session['username'] 
        images=carousel_Image.objects.filter(username=username)
    if request.method=='POST':
        username=request.session['username']
        var=0
        code=[]
        name=request.POST.get("textofcarousel")
        file=request.FILES.get("fileofcarousel")
        print(name)
        print(file)
        while name and file:
            img_obj=carousel_Image(username=username,name=name,image=file)
            img_obj.save()
            var+=1
            name=request.POST.get("textofcarousel"+str(var))
            file=request.FILES.get("fileofcarousel"+str(var))
        return redirect(addcarousel)
    elif request.session.has_key('username'):
        username = request.session['username']
        navbarcode=" "
        dbusername=Menu.objects.filter(username=username)
        if dbusername:
            list=Menu.objects.all()
            for elements in list:
                if elements.username==username:
                    navbarcode=elements.navbarcode
        for item in images:
            print(item)
        return render(request,'carousel.html',{'username':username,'navbarcode':navbarcode,'images':images})
    else:
        return redirect("/home/")