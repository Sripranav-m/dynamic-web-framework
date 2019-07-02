function numberofinputfields()
{
	return document.querySelectorAll(".inputtypes").length;
}
function showcarousel_sourcecode()
{
	var code=document.querySelector("#maindivforcarousel").innerHTML;
	if(document.querySelector("#textareacarousel").style.display=="none")
	{
		document.querySelector("#textareacarousel").textContent=code;
		document.querySelector("#textareacarousel").style.display="block";
		document.querySelector("#textareacarousel").style.margin="auto";
	}
	else
	{
		document.querySelector("#textareacarousel").textContent=code;
		document.querySelector("#textareacarousel").style.display="none";
	}
}

function displaycodeforform()
{
	if(document.querySelector("#textarea").style.display=="none")
	{
		document.querySelector("#textarea").style.display="block";
		document.querySelector("#textarea").style.margin="auto"
	}
	else
	{
		document.querySelector("#textarea").style.display="none";
	}
	
}

function myfunction()
{
	var main=document.querySelector(".inputfieldsf").innerHTML;
	document.getElementById("yourformf").insertAdjacentHTML("beforeend",main);
	document.querySelectorAll(".nameofinput")[numberofinputfields()-1].name+=numberofinputfields()-1;
	document.querySelectorAll(".inputtypes")[numberofinputfields()-1].name+=numberofinputfields()-1;
}


function showmenu_code()
{
	if(document.querySelector("#textareamenu").style.display=="none")
	{
		document.querySelector("#textareamenu").style.display="block";
		document.querySelector("#textareamenu").style.margin="auto"
	}
	else
	{
		document.querySelector("#textareamenu").style.display="none";
	}
}

function newitem()
{
	var num=document.getElementById("number").innerHTML;
	num=parseInt(num);
	num+=1;
	document.querySelector("#menu").innerHTML=" ";
	document.querySelector("#menu").insertAdjacentHTML("beforeend",document.querySelector(".listmenu").innerHTML+"<br>");
	document.querySelectorAll(".nameofmenu")[num-1].name=num+"name";
	document.querySelectorAll(".buttonofmenu")[num-1].name=num+"button";
	document.querySelectorAll(".parentofmenu")[num-1].name=num+"parent";
	document.querySelectorAll(".parentofmenu")[num-1].value=0;
	//document.querySelectorAll(".status")[num-1].name=num+"status";
	//document.querySelectorAll(".status")[num-1].value="enabled";
}

function newsubitem(k)
{
	var num=document.getElementById("number").innerHTML;
	num=parseInt(num);
	num+=1;
	k=k.replace("button","");
	document.querySelector("#menu").innerHTML=" ";
	document.getElementById("menu").insertAdjacentHTML("beforeend",document.querySelector(".listmenu").innerHTML+"<br>");
	document.getElementsByClassName("nameofmenu")[num-1].name=num+"name";
	document.querySelectorAll(".buttonofmenu")[num-1].name=num+"button";
	document.querySelectorAll(".parentofmenu")[num-1].name=num+"parent";
	document.querySelectorAll(".parentofmenu")[num-1].value=k;
	document.querySelectorAll(".status")[num-1].name=num+"status";
	document.querySelectorAll(".status")[num-1].value="enabled";
}
function deletemenu(name)
{
	if(document.querySelectorAll(".listmenu").length==1)
	{
		alert("ONLY ONE ITEM IS PRESENT , DELETION IS NOT POSSIBLE , APPEND INSTEAD OF DELETION....");
	}
	else if(name.replace("delbutton","")==1)
	{
		alert("CANNOT BE DELETED , APPEND INSTEAD..")
	}
	else
	{
		if (confirm("do you really want to delete???"))
		{
			int=name.replace("delbutton","");
			document.getElementsByName(int+"status")[0].value="disabled";
			for(var j=1;j<=document.getElementsByClassName("nameofmenu").length;j++)
			{
				if( document.getElementsByName(j+"parent")[0].value==int)
				{
					document.getElementsByName(j+"status")[0].value="disabled";
					deletes(j);
				}
			}
			document.querySelector(".clicktosubmit").click();
			
		}
	}
}
function deletes(j)
{
	if(j<=document.getElementsByClassName("nameofmenu").length)
	{
		for(var k=1;k<=document.getElementsByClassName("nameofmenu").length;k++)
		{
			if( document.getElementsByName(k+"parent")[0].value==j)
			{
				document.getElementsByName(k+"status")[0].value="disabled";
				deletes(k);
			}
		}
	}
}

function showmenucode()
{
	a=document.querySelectorAll(".displaymenu")[0];
	b=document.querySelectorAll(".displaymenu")[1];
	c=document.querySelectorAll(".displaymenu")[2];
	if (a.style.display=="none")
	{
		a.style.display="block";
		b.style.display="block";
		c.style.display="block";
	}
	else
	{
		a.style.display="none";
		b.style.display="none";
		c.style.display="none";
	}

}

